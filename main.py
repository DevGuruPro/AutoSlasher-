import os
import sys
import threading

import schedule
import time
from typing import List, Tuple

from PySide6 import QtCore
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QCursor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QHeaderView, QCheckBox, QWidget, \
    QHBoxLayout, QComboBox, QToolButton, QAbstractItemView

from settings import SERIAL_PORT, BAUD_RATE, POSITION_TOLERANCE, DATABASE_PATH, GPS_STAT_MSG
from ui.ui_as import Ui_AS

from utils.commons import (extract_from_gps, generate_path, calculate_heading_to_waypoint,
                           distance_to_waypoint, clip_speed, find_as_files)
from utils.magnetometer import Magnetometer

from utils.simplertk2b import GPS
from utils.logger import logger

from widget.loadingDlg import LoadingDlg
from widget.nameDlg import NameDlg
from widget.popup import RecordingPopup


class AutoSlasher(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AS()
        self.ui.setupUi(self)
        self.showFullScreen()

        self.del_btn = []

        self.loadingDlg = LoadingDlg(self)
        self.loadingDlg.hide()

        self.recordingDlg = RecordingPopup(self)
        self.recordingDlg.hide()

        # self.ui.centralwidget.setStyleSheet("background-image: url(path_to_your_image.jpg);")

        self.ui.startBoun.clicked.connect(self.start_recording_boundary)
        self.ui.stopBoun.clicked.connect(self.stop_recording)
        self.ui.startObs.clicked.connect(self.start_recording_obstacle)
        self.ui.stopObs.clicked.connect(self.stop_recording)
        self.ui.generateF.clicked.connect(self.save_file)
        self.ui.deleteF.clicked.connect(self.discard_field)
        self.ui.createFieldBtn.clicked.connect(self.to_record_field_page)
        self.ui.m_settingBtn.clicked.connect(self.to_setting_page)
        self.ui.f_manaBtn.clicked.connect(self.to_field_manager_page)
        self.ui.startBtn.clicked.connect(self.on_start_button)
        self.ui.sureYes.clicked.connect(self.on_sure_yes)
        self.ui.sureNo.clicked.connect(self.on_sure_no)
        self.ui.stopGuid.clicked.connect(self.to_start_page)
        self.ui.prevPage.clicked.connect(self.to_prev_page)
        self.ui.nextPage.clicked.connect(self.to_next_page)

        # self.ui.settingTable.setFixedWidth(500)
        self.ui.setting_table.setFixedHeight(463)
        self.ui.setting_table.setColumnWidth(0, 800)
        self.ui.setting_table.setColumnWidth(1, 150)
        # self.ui.setting_table.setColumnWidth(2, 40)

        cell_widget = QWidget()
        combo_box = QComboBox()
        combo_box.addItems(["NO", "YES"])
        combo_box.setMinimumWidth(80)
        font = QFont()
        font.setPointSize(24)  # Set the desired font size
        combo_box.setFont(font)
        layout_inner = QHBoxLayout(cell_widget)
        layout_inner.addWidget(combo_box)
        layout_inner.setAlignment(combo_box, Qt.AlignmentFlag.AlignCenter)  # Center the checkbox
        layout_inner.setContentsMargins(5, 5, 5, 5)  # Remove margins
        self.ui.setting_table.setCellWidget(4, 2, cell_widget)
        self.ui.setting_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        for row in range(self.ui.setting_table.rowCount()):
            item = self.ui.setting_table.item(row, 1)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item = self.ui.setting_table.item(row, 2)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.ui.field_table.setFixedWidth(500)
        self.ui.field_table.setFixedHeight(463)
        self.ui.field_table.setColumnWidth(0, 800)
        self.ui.field_table.setColumnWidth(1, 200)
        self.ui.field_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.ui.settingPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.hide()
        self.ui.startButtons.hide()
        self.ui.movingPage.hide()

        self.field_data: List[List[Tuple[float, float]]] = [[]]
        self.waypoint = []
        self._moving_stop = False
        self.current_filename = ''
        self.is_showing_board = False
        self.field_page_index = 0
        # self.focal = None

        self.gps = GPS(port=SERIAL_PORT, baud_rate=BAUD_RATE)
        self.gps.sig_msg.connect(self.show_gps_status)
        self.gps.start()
        self._recording_stop = threading.Event()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self.path_thread = threading.Thread(target=self.set_generated_path)
        self.current_location_thread = threading.Thread(target=self.set_current_location)
        self.current_location_thread.start()

        self.compass = Magnetometer()
        # self.to_start_page()

    def hide_all_widget(self):
        self.ui.startPage.hide()
        self.ui.settingPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.hide()
        self.ui.movingPage.hide()

    def to_main_page(self):
        self.is_showing_board = False
        self.ui.startPage.show()
        self.ui.startButtons.hide()

    def to_start_page(self):
        self.is_showing_board = False
        self.hide_all_widget()
        self.ui.startButtons.show()
        self.ui.startPage.show()
        self.ui.movingPage.show()
        self.ui.nextPage.hide()
        self.ui.combo_field.clear()
        database = find_as_files()
        for path in database:
            self.ui.combo_field.addItem(path[:-3])

    def to_setting_page(self):
        self.is_showing_board = False
        self.ui.startPage.hide()
        self.ui.settingPage.show()

    def refresh_field_table(self):
        database = find_as_files()
        self.ui.field_table.setRowCount(0)
        self.ui.field_table.setRowCount(8)
        start_idx = self.field_page_index * 8
        for i in range(start_idx, min(start_idx+8, len(database))):
            self.ui.field_table.setItem(i-start_idx, 0, QTableWidgetItem(database[i][:-3]))
            btn = QToolButton(self)
            btn.setObjectName(u"del_btn")
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            btn.setAutoRaise(True)
            btn.setStyleSheet("""  
                                   QToolButton {  
                                       background-color: transparent;  
                                       border: none;  
                                   }  
                                   QToolButton:hover {  
                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                   }  
                               """)
            icon = QIcon()
            icon.addFile(u":/img/regenerate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            btn.setIcon(icon)
            btn.setIconSize(QSize(40, 40))
            btn.clicked.connect(lambda checked, row=i: self.regenerate_btn_clicked(row))
            container_widget = QWidget()
            layout = QHBoxLayout(container_widget)
            layout.addWidget(btn)
            layout.setContentsMargins(5, 5, 5, 5)
            self.ui.field_table.setCellWidget(i-start_idx, 2, container_widget)
            btn1 = QToolButton(self)
            btn1.setObjectName(u"del_btn")
            btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            btn1.setAutoRaise(True)
            btn1.setStyleSheet("""  
                                               QToolButton {  
                                                   background-color: transparent;  
                                                   border: none;  
                                               }  
                                               QToolButton:hover {  
                                                   background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                               }  
                                           """)
            icon1 = QIcon()
            icon1.addFile(u":/img/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            btn1.setIcon(icon1)
            btn1.setIconSize(QSize(40, 40))
            btn1.clicked.connect(lambda checked, row=i: self.del_btn_clicked(row))
            container_widget1 = QWidget()
            layout1 = QHBoxLayout(container_widget1)
            layout1.addWidget(btn1)
            layout1.setContentsMargins(5, 5, 5, 5)
            self.ui.field_table.setCellWidget(i-start_idx, 1, container_widget1)
        if start_idx+8 >= len(database):
            self.ui.nextPage.hide()
            return

    def to_field_manager_page(self):
        self.is_showing_board = False
        # for row in range(self.ui.field_table.rowCount()):
        #     for col in range(self.ui.field_table.columnCount()):
        #         item = self.ui.field_table.item(row, col)
        #         if item is not None:
        #             item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)

        self.ui.startPage.hide()
        self.ui.fieldPage.hide()
        self.ui.fmanagerPage.show()
        self.ui.movingPage.show()
        self.ui.nextPage.show()
        self.field_page_index = 0
        self.refresh_field_table()

    def to_record_field_page(self):
        self.is_showing_board = True
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.show()
        self.ui.movingPage.hide()

        self.ui.naviWidget.hide()
        self.ui.fieldWidget.show()
        self.ui.sureWidget.hide()
        self.ui.recordWidget.show()

        self.ui.displayWidget.clear()
        self.field_data.clear()
        self.field_data.append([])
        self.waypoint.clear()

    def to_open_field_page(self, is_regenerate):
        self.is_showing_board = True
        self.ui.startPage.hide()
        self.ui.movingPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.settingPage.hide()
        self.ui.movingPage.hide()
        self.ui.fieldPage.show()

        self.ui.fieldWidget.hide()
        self.ui.naviWidget.show()
        self.ui.positionWidget.hide()
        self.ui.recordWidget.hide()

        if not is_regenerate:
            self.current_filename = self.ui.combo_field.currentText() + '.as'
        self.load_file(is_regenerate)

    def to_prev_page(self):
        if self.ui.startPage.isVisible():
            self.ui.startButtons.hide()
            self.ui.movingPage.hide()
        elif self.ui.settingPage.isVisible() or self.ui.fmanagerPage.isVisible():
            self.to_start_page()
        elif self.ui.positionWidget.isVisible():
            self.to_open_field_page(False)

    def discard_field(self):
        self.ui.sureWidget.show()

    def on_sure_yes(self):
        self.to_field_manager_page()

    def on_sure_no(self):
        self.ui.sureWidget.hide()

    def to_next_page(self):
        self.field_page_index = self.field_page_index + 1
        self.refresh_field_table()
        pass

    def del_btn_clicked(self, row):
        database = find_as_files()
        file_path = DATABASE_PATH + '/' + database[row]
        if os.path.exists(file_path):
            # Attempt to delete the file
            try:
                os.remove(file_path)
                logger.info(f"File '{file_path}' has been deleted successfully.")
            except Exception as e:
                logger.error(f"Error deleting file '{file_path}': {e}")
        else:
            logger.error(f"File '{file_path}' does not exist.")
        self.refresh_field_table()

    def regenerate_btn_clicked(self, row):
        database = find_as_files()
        self.current_filename = database[row]
        self.to_open_field_page(True)

    def on_start_button(self):
        if self.ui.startButtons.isVisible():
            self.field_data.clear()
            self.waypoint.clear()
            self.ui.displayWidget.clear()
            self.to_open_field_page(False)
        else:
            self.to_start_page()

    def start_scheduler(self, index):
        schedule.clear()
        schedule.every(1).seconds.do(lambda: self.save_gps_data(index))
        while not self._recording_stop.is_set():
            schedule.run_pending()
            time.sleep(0.1)

    def set_current_location(self):
        while self.gps.isRunning():
            if self.is_showing_board:
                x, y = self.get_position()
                heading = self.compass.read_heading()
                self.ui.displayWidget.init_current()
                if x is None or y is None:
                    logger.error("Cannot get gps data.")
                    continue
                elif heading is None:
                    logger.error("Cannot get magnetometer data.")
                    continue
                self.ui.displayWidget.set_location((x, y), heading)
            time.sleep(0.1)

    def get_position(self):
        gps_data = self.gps.get_data()
        return extract_from_gps(gps_data)

    def start_recording_boundary(self):
        logger.info('Starting recording boundary...')
        self.recordingDlg.set_type("boundary")
        self.recordingDlg.show()
        self.field_data[0].clear()
        self.ui.displayWidget.clear_bnd_point()
        self._recording_stop.clear()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(0,))
        self.scheduler_thread.start()

    def start_recording_obstacle(self):
        logger.info('Starting recording obstacle...')
        self.recordingDlg.set_type("obstacle")
        self.recordingDlg.show()
        self.field_data.append([])
        self.ui.displayWidget.add_new_obs()
        self._recording_stop.clear()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(len(self.field_data) - 1,))
        self.scheduler_thread.start()

    def stop_recording(self):
        if not self._recording_stop.is_set():
            logger.info('Stopping recording...')
            self._recording_stop.set()
            self.scheduler_thread.join()
            logger.info('Schedule stopped')
            self.recordingDlg.hide()

    def save_gps_data(self, index):
        x, y = self.get_position()
        if x is not None and y is not None:
            logger.info(f"Extracted coordinates: X = {x}, Y = {y}")
            self.field_data[index].append((x, y))
            if index == 0:
                self.ui.displayWidget.add_bnd_point(int(x), int(y))
            else:
                self.ui.displayWidget.add_obs_point(int(x), int(y))
        else:
            logger.error("Cannot get gps data.")

    def load_file(self, is_regenerate):
        print(is_regenerate)
        self.field_data.clear()
        self.waypoint.clear()
        self.ui.displayWidget.clear()
        filename = DATABASE_PATH + '/' + self.current_filename
        logger.info(f'Loading {filename}...')
        with open(filename, 'r') as file:
            current_list: List[Tuple[float, float]] = []
            is_path = False
            for line in file:
                line = line.strip()
                if line == '###' or line == 'PATH':
                    if current_list:
                        self.field_data.append(current_list)
                    current_list = []
                    if line == 'PATH':
                        if is_regenerate:
                            break
                        is_path = True
                else:
                    line = line.strip('()')
                    parts = line.split(',')
                    if len(parts) == 2:
                        a, b = float(parts[0]), float(parts[1])
                        tuple_data: Tuple[float, float] = (a, b)
                        current_list.append(tuple_data)
            if current_list:
                if not is_path:
                    self.field_data.append(current_list)
                else:
                    self.waypoint = current_list
        if len(self.waypoint) == 0:
            self.path_thread = threading.Thread(target=self.set_generated_path, args=(filename,), daemon=True)
            self.path_thread.start()
            self.ui.guidWidget.setDisabled(True)
            self.loadingDlg.setModal(True)
            self.loadingDlg.exec()
        else:
            self.ui.displayWidget.load_field_data(self.field_data, self.waypoint)

    def set_generated_path(self, filename):
        ma_width = int(self.ui.setting_table.item(2, 2).text())
        offset = int(self.ui.setting_table.item(3, 2).text())
        self.waypoint = generate_path(self.field_data, ma_width, offset)
        combo_box = self.ui.setting_table.cellWidget(4, 2).layout().itemAt(0).widget()
        selected_text = combo_box.currentText()
        print(f"Selected Text: {selected_text}")
        if selected_text == "YES":
            arr = self.field_data[0]
            arr.append(self.field_data[0][0])
            self.waypoint = arr + self.waypoint
        self.save_database(filename)
        self.ui.displayWidget.load_field_data(self.field_data, self.waypoint)
        self.loadingDlg.close()
        self.ui.guidWidget.setEnabled(True)

    def save_file(self):
        name_dlg = NameDlg(self)
        if name_dlg.exec() != QDialog.accepted:
            logger.info("Name Input Dialog Closed.")
            return
        filename = name_dlg.get_name() + ".as"
        logger.debug(f"File name : {filename}")
        self.save_database(filename)

    def save_database(self, filename):
        with open(filename, 'w') as file:
            for i in range(len(self.field_data)):
                file.write('###\n')
                for j in range(len(self.field_data[i])):
                    file.write(f"{self.field_data[i][j]}\n")
            if len(self.waypoint):
                file.write('PATH\n')
            for i in range(len(self.waypoint)):
                file.write(f"{self.waypoint[i]}\n")

    def show_gps_status(self, status):
        logger.info(f'STAT:{status}')
        self.ui.gps_sts.setText(status)
        if status != GPS_STAT_MSG[0]:
            self.ui.displayWidget.init_current()

    def closeEvent(self, event):
        self.gps.stop()
        self._recording_stop.set()
        if self.scheduler_thread.is_alive():
            self.scheduler_thread.join(.1)
        schedule.clear()
        if self.path_thread.is_alive():
            self.path_thread.join(.1)
        return super().closeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    window.show()
    sys.exit(app.exec())
