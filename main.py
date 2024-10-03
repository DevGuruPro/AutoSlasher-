import sys
import threading

import schedule
import time
from typing import List, Tuple

from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from settings import serial_port, baud_rate
from ui.ui_as import Ui_AS

from utils.commons import extract_from_gps, generate_path
from utils.simplertk2b import GPS
from utils.logger import logger
from widget.displayBoard import DisplayBoard

from widget.loadingDlg import LoadingDlg
from widget.nameDlg import NameDlg
from widget.popup import RecordingPopup


class AutoSlasher(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AS()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.showFullScreen()

        # self.ui.combo_field.addItem("Option 1")
        # self.ui.combo_field.addItem("Option 2")
        # self.ui.combo_field.addItem("Option 3")
        # self.ui.displayWidget = DisplayBoard()
        self.ui.combo_field.currentIndexChanged.connect(self.handle_activated)

        self.loadingDlg = LoadingDlg(self)
        self.loadingDlg.hide()
        # RecordingPopup(self).show()

        # self.ui.centralwidget.setStyleSheet("background-image: url(path_to_your_image.jpg);")

        self.ui.startBtn.clicked.connect(self.to_open_field_page)

        self.ui.startBoun.clicked.connect(self.start_recording_boundary)
        self.ui.stopBoun.clicked.connect(self.stop_recording)
        self.ui.startObs.clicked.connect(self.start_recording_obstacle)
        self.ui.stopObs.clicked.connect(self.stop_recording)
        self.ui.generateF.clicked.connect(self.save_file)

        self.gps = GPS(port=serial_port, baud_rate=baud_rate)
        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self._gps_stop = threading.Event()
        self.field_data: List[List[Tuple[int, int]]] = [[]]

        self.path_thread = threading.Thread(target=self.set_generated_path)

        self.ui.settingPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.hide()

    def to_record_field_page(self):
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.show()
        self.ui.movingPage.hide()

        self.ui.naviWidget.hide()
        self.ui.sureWidget.hide()

        self.gps = GPS(port=serial_port, baud_rate=baud_rate)
        self.gps.sig_msg.connect(self.show_gps_status)
        self.gps.start()
        self._gps_stop.clear()

    def to_open_field_page(self):
        self.ui.startPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.settingPage.hide()
        self.ui.movingPage.hide()
        self.ui.fieldPage.show()

        self.ui.fieldWidget.hide()
        self.ui.positionWidget.hide()
        self.ui.recordWidget.hide()
        self.ui.displayWidget.show()

        self.load_file('test.as')

    def handle_activated(self, index):
        self.ui.combo_field.blockSignals(True)
        self.ui.combo_field.setCurrentText(f"Selected Field: {self.ui.combo_field.itemText(index)}")
        self.ui.combo_field.blockSignals(False)

    def start_scheduler(self, index):
        schedule.clear()
        schedule.every(1).seconds.do(lambda: self.save_gps_data(index))
        while not self._gps_stop.is_set():
            schedule.run_pending()
            time.sleep(0.1)

    def start_recording_boundary(self):
        logger.info('Starting recording boundary...')
        self.field_data[0].clear()
        self.ui.displayWidget.clear_bnd_point()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(0,))
        self.scheduler_thread.start()

    def start_recording_obstacle(self):
        logger.info('Starting recording obstacle...')
        self.field_data.append([])
        self.ui.displayWidget.add_new_obs()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(len(self.field_data) - 1,))
        self.scheduler_thread.start()

    def stop_recording(self):
        if not self._gps_stop.is_set():
            logger.info('Stopping recording...')
            self._gps_stop.set()
            self.scheduler_thread.join()
            logger.info('Schedule stopped')
            if self.gps.isRunning():
                self.gps.stop()

    def save_gps_data(self, index):
        gps_data = self.gps.get_data()
        x, y = extract_from_gps(gps_data)
        if x is not None and y is not None:
            logger.info(f"Extracted coordinates: X = {x}, Y = {y}")
            self.field_data[index].append((int(x), int(y)))
            if index == 0:
                self.ui.displayWidget.add_bnd_point(int(x), int(y))
            else:
                self.ui.displayWidget.add_obs_point(int(x), int(y))
        else:
            logger.error("Conversion failed.")

    def load_file(self, filename):
        self.field_data.clear()
        logger.info(f'Loading {filename}...')
        with open(filename, 'r') as file:
            current_list: List[Tuple[int, int]] = []
            for line in file:
                line = line.strip()
                if line == '###':
                    if current_list:
                        self.field_data.append(current_list)
                    current_list = []
                else:
                    line = line.strip('()')
                    parts = line.split(',')
                    if len(parts) == 2:
                        a, b = int(parts[0]), int(parts[1])
                        tuple_data: Tuple[int, int] = (a, b)
                        current_list.append(tuple_data)
            if current_list:
                self.field_data.append(current_list)
        self.path_thread = threading.Thread(target=self.set_generated_path, daemon=True)
        self.path_thread.start()
        self.ui.guidWidget.setDisabled(True)
        self.loadingDlg.setModal(True)
        self.loadingDlg.exec()

    def set_generated_path(self):
        path = generate_path(self.field_data)
        self.ui.displayWidget.load_field_data(self.field_data, path)
        self.loadingDlg.close()
        self.ui.guidWidget.setEnabled(True)

    def save_file(self):
        name_dlg = NameDlg(self)
        name_dlg.exec()
        filename = name_dlg.get_name() + ".as"
        logger.debug(f"File name : {filename}")
        with open(filename, 'w') as file:
            for i in range(len(self.field_data)):
                file.write('###\n')
                for j in range(len(self.field_data[i])):
                    file.write(f"{self.field_data[i][j]}\n")

    def show_gps_status(self, status):
        self.ui.gps_sts.setText(status)

    def closeEvent(self, event):
        self.gps.stop()
        self._gps_stop.set()
        if self.scheduler_thread.is_alive():
            self.scheduler_thread.join(.1)
        schedule.clear()
        self.path_thread.join(.1)
        return super().closeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    screen_geometry = app.primaryScreen().geometry()
    screen_geometry.adjust(50, 50, -50, -50)
    window.setGeometry(screen_geometry)
    window.show()
    sys.exit(app.exec())
