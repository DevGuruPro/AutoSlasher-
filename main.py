import sys
import threading

import schedule
import time
from typing import List, Tuple

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QHeaderView

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
        # self.showFullScreen()

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

        self.ui.settingTable.setFixedWidth(500)
        self.ui.settingTable.setFixedHeight(400)
        self.ui.settingTable.setColumnWidth(0, 250)
        self.ui.settingTable.setColumnWidth(1, 60)
        self.ui.settingTable.setColumnWidth(2, 40)

        self.ui.field_table.setFixedWidth(500)
        self.ui.field_table.setFixedHeight(400)
        self.ui.field_table.setColumnWidth(0, 200)
        self.ui.field_table.setColumnWidth(1, 98)

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

    def to_field_manager_page(self):
        self.is_showing_board = False
        database = find_as_files()
        for i in range(len(database)):
            self.ui.field_table.setItem(i, 0, QTableWidgetItem(database[i][:-3]))
        self.ui.startPage.hide()
        self.ui.fieldPage.hide()
        self.ui.fmanagerPage.show()
        self.ui.movingPage.show()

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

    def to_open_field_page(self):
        print(self.gps.isRunning())
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

        self.current_filename = self.ui.combo_field.currentText() + '.as'
        logger.info(self.current_filename)
        self.load_file()

    def to_prev_page(self):
        if self.ui.startPage.isVisible():
            self.ui.startButtons.hide()
            self.ui.movingPage.hide()
        elif self.ui.settingPage.isVisible() or self.ui.fmanagerPage.isVisible():
            self.to_start_page()
        elif self.ui.positionWidget.isVisible():
            self.to_open_field_page()

    def discard_field(self):
        self.ui.sureWidget.show()

    def on_sure_yes(self):
        self.to_field_manager_page()

    def on_sure_no(self):
        self.ui.sureWidget.hide()

    def to_next_page(self):
        pass

    def on_start_button(self):
        if self.ui.startButtons.isVisible():
            self.to_open_field_page()
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

    def load_file(self):
        self.field_data.clear()
        self.waypoint.clear()
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
        self.waypoint = generate_path(self.field_data)
        with open(filename, 'a') as file:
            file.write('PATH\n')
            for i in range(len(self.waypoint)):
                file.write(f"{self.waypoint[i]}\n")
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
        with open(filename, 'w') as file:
            for i in range(len(self.field_data)):
                file.write('###\n')
                for j in range(len(self.field_data[i])):
                    file.write(f"{self.field_data[i][j]}\n")

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
