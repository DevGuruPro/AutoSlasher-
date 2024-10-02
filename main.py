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

from utils.commons import extract_from_gps
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
        self.ui.displayWidget = DisplayBoard()
        self.ui.combo_field.currentIndexChanged.connect(self.handle_activated)

        # LoadingDlg(self).show()
        # RecordingPopup(self).show()

        self.ui.startPage.hide()
        self.ui.settingPage.hide()
        self.ui.fmanagerPage.hide()
        # self.ui.fieldPage.hide()
        self.ui.movingPage.hide()
        # self.ui.centralwidget.setStyleSheet("background-image: url(path_to_your_image.jpg);")

        self.ui.startBoun.clicked.connect(self.start_recording_boundary)
        self.ui.stopBoun.clicked.connect(self.stop_recording)
        self.ui.startObs.clicked.connect(self.start_recording_obstacle)
        self.ui.stopObs.clicked.connect(self.stop_recording)
        self.ui.generateF.clicked.connect(self.save_file)

        self.gps = GPS(port=serial_port, baud_rate=baud_rate)
        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self._gps_stop = threading.Event()
        self.obs_index = 1
        self.field_data: List[List[Tuple[int, int]]] = [[]]

    def handle_activated(self, index):
        print(index)
        self.ui.combo_field.blockSignals(True)
        self.ui.combo_field.setCurrentText(f"Selected Field: {self.ui.combo_field.itemText(index)}")
        self.ui.combo_field.blockSignals(False)

    def start_scheduler(self, index):
        schedule.clear()
        schedule.every(3).seconds.do(lambda: self.save_gps_data(index))
        while not self._gps_stop.is_set():
            schedule.run_pending()
            time.sleep(1)

    def start_recording_boundary(self):
        logger.info('Starting recording boundary...')
        self.field_data[0].clear()
        self.gps.start()
        self._gps_stop.clear()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(0,))
        self.scheduler_thread.start()

    def start_recording_obstacle(self):
        logger.info('Starting recording obstacle...')
        self.field_data.append([])
        self.gps.start()
        self._gps_stop.clear()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler, args=(self.obs_index,))
        self.scheduler_thread.start()
        self.obs_index = self.obs_index+1

    def stop_recording(self):
        if not self._gps_stop.is_set():
            logger.info('Stopping recording...')
            self._gps_stop.set()
            self.scheduler_thread.join()
            logger.info('Schedule stopped')
            if self.gps.is_alive():
                self.gps.stop()

    def save_gps_data(self, index):
        gps_data = self.gps.get_data()
        x, y = extract_from_gps(gps_data)
        logger.info(f"Location : {x},{y}")
        self.field_data[index].append((int(x), int(y)))

    def save_file(self):
        name_dlg = NameDlg(self)
        name_dlg.exec()
        filename = name_dlg.get_name() + ".as"
        logger.debug(f"File name : {filename}")
        with open(filename, 'w') as file:
            for i in range(len(self.field_data)):
                file.write('###')
                for j in range(len(self.field_data[i])):
                    file.write(f"{self.field_data[i][j]}\n")

    def closeEvent(self, event):
        self.gps.stop()
        return super().closeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    screen_geometry = app.primaryScreen().geometry()
    screen_geometry.adjust(50, 50, -50, -50)
    window.setGeometry(screen_geometry)
    window.show()
    sys.exit(app.exec())
