# compass.py

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtCore import Qt, QTimer
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

# Import necessary classes
from imu.magnetometer import MagnetometerSensor
from calibration import CalibrationManager, CalibrationData
from sensor_processing import HeadingCalculator

class CompassWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.heading = 0
        self.target_heading = None

        # Adjust the image path as needed
        self.arrow_image = QPixmap('ui/img/arrow.png')
        if self.arrow_image.isNull():
            print("Error: Could not load 'ui/img/arrow.png'. Please ensure the file exists.")
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Compass')
        self.setGeometry(2500, 100, 400, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.angle_label = QLabel("Heading: 0°", self)
        self.angle_label.setAlignment(Qt.AlignCenter)
        self.layout.addStretch()
        self.layout.addWidget(self.angle_label)

    def update_heading_display(self, heading):
        self.heading = heading % 360  # Ensure the heading stays within 0-359 degrees
        self.angle_label.setText(f"Heading: {self.heading:.2f}°")
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        center = self.rect().center()
        painter.translate(center)
        painter.save()
        painter.rotate(self.heading)
        if not self.arrow_image.isNull():
            painter.drawPixmap(-self.arrow_image.width() // 2, -self.arrow_image.height() // 2, self.arrow_image)
        else:
            # Draw a placeholder if the image is not available
            painter.setPen(QPen(Qt.black, 2))
            painter.drawLine(0, -50, 0, 50)
            painter.drawLine(-50, 0, 50, 0)
        painter.restore()
        if self.target_heading is not None:
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.save()
            painter.rotate(self.target_heading)
            painter.drawLine(0, 0, 0, 100)
            painter.restore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    compass_widget = CompassWidget()
    compass_widget.show()

    # Initialize the MagnetometerSensor
    sensor = MagnetometerSensor(address=0x0C, bus_num=1)  # Use the appropriate address and bus number

    # Initialize CalibrationManager and load calibration data
    calibration_manager = CalibrationManager()
    # For now, we'll set calibration data manually
    calibration_manager.calibration_data = CalibrationData(
        min_x=-2048, max_x=2047,
        min_y=-2048, max_y=2047
    )

    # Initialize HeadingCalculator
    heading_calculator = HeadingCalculator()

    # Define the function to update the heading
    def update_heading():
        try:
            # Read raw data from the sensor
            raw_x, raw_y, raw_z = sensor.read_raw_data()

            # Apply calibration
            x_calibrated, y_calibrated, z_calibrated = calibration_manager.apply_calibration(raw_x, raw_y, raw_z)

            # Calculate heading
            heading = heading_calculator.calculate_heading(x_calibrated, y_calibrated)

            # Update the compass widget
            compass_widget.update_heading_display(heading)
        except Exception as e:
            print(f"Error updating heading: {e}")

    # Set up a timer to update the heading periodically
    timer = QTimer()
    timer.timeout.connect(update_heading)
    timer.start(100)  # Update every 100 milliseconds

    sys.exit(app.exec())
