import sys
import threading

import schedule
import time
from typing import List, Tuple

from PySide6.QtWidgets import QApplication, QMainWindow

from settings import SERIAL_PORT, BAUD_RATE, POSITION_TOLERANCE
from ui.ui_as import Ui_AS

from utils.commons import (extract_from_gps, generate_path, calculate_heading_to_waypoint,
                           distance_to_waypoint, clip_speed)
# from utils.magnetometer import Magnetometer
# from utils.robot import Robot
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

        self.ui.settingPage.hide()
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.hide()

        self.field_data: List[List[Tuple[float, float]]] = [[]]
        self.waypoint = []
        self._moving_stop = False
        # self.focal = None

        self.gps = GPS()
        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self._gps_stop = threading.Event()
        self.path_thread = threading.Thread(target=self.set_generated_path)

        # self.compass = Magnetometer()
        # self.robot = Robot()

    def to_record_field_page(self):
        self.ui.fmanagerPage.hide()
        self.ui.fieldPage.show()
        self.ui.movingPage.hide()

        self.ui.naviWidget.hide()
        self.ui.sureWidget.hide()

        self.gps = GPS(port=SERIAL_PORT, baud_rate=BAUD_RATE)
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

    def get_position(self):
        gps_data = self.gps.get_data()
        return extract_from_gps(gps_data)

    # def follow_path(self):
    #     for i in range(1, len(self.waypoint)):
    #         self.navigate_to_waypoint(self.waypoint[i])
    #
    # def navigate_to_waypoint(self, waypoint):
    #     while True:
    #         current_position = self.get_position()
    #         distance = distance_to_waypoint(current_position, waypoint)
    #         if distance < POSITION_TOLERANCE:
    #             logger.debug(f'Reached waypoint : {waypoint}')
    #             return
    #         target_heading = calculate_heading_to_waypoint(current_position, waypoint)
    #         heading_error = (target_heading - self.compass.read_heading() + 360) % 360
    #         if heading_error > 180:
    #             heading_error -= 360
    #
    #         k_p_heading = 0.1  # Proportional gain for heading
    #         k_p_position = 0.01
    #
    #         heading_correction = k_p_heading * heading_error
    #         speed_correction = k_p_position * distance
    #         base_speed = 0.5
    #
    #         left_speed = base_speed - heading_correction + speed_correction
    #         right_speed = base_speed + heading_correction + speed_correction
    #
    #         # Adjust motor speed based on the position and heading corrections
    #         self.robot.set_motors(left_speed=clip_speed(left_speed),
    #                               right_speed=clip_speed(right_speed))
    #
    #         time.sleep(0.1)

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
        x, y = self.get_position()
        if x is not None and y is not None:
            logger.info(f"Extracted coordinates: X = {x}, Y = {y}")
            self.field_data[index].append((x, y))
            if index == 0:
                self.ui.displayWidget.add_bnd_point(int(x), int(y))
            else:
                self.ui.displayWidget.add_obs_point(int(x), int(y))
        else:
            logger.error("Conversion failed.")

    def load_file(self, filename):
        self.field_data.clear()
        self.waypoint.clear()
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
        if self.path_thread.is_alive():
            self.path_thread.join(.1)
        # if self.compass:
        #     del self.compass
        return super().closeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    screen_geometry = app.primaryScreen().geometry()
    screen_geometry.adjust(50, 50, -50, -50)
    window.setGeometry(screen_geometry)
    window.show()
    sys.exit(app.exec())
