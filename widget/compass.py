import sys
import time
import os

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPixmap, QPen, QColor

from utils.magnetometer import MagnetometerSensor


class CompassWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compass")
        self.setGeometry(100, 100, 400, 400)
        self.layout = QVBoxLayout(self)
        self.angle_label = QLabel("Heading: 0°", self)
        self.angle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.angle_label.setStyleSheet("font-size: 20px;")
        self.layout.addStretch()
        self.layout.addWidget(self.angle_label)
        
        self.heading = 0
        self.target_heading = None
        
        # Load the arrow image
        arrow_image_path = os.path.join(os.path.dirname(__file__), '../ui/img/arrow.png')
        if os.path.exists(arrow_image_path):
            self.arrow_image = QPixmap(arrow_image_path)
        else:
            print(f"Error: Arrow image not found at {arrow_image_path}")
            self.arrow_image = QPixmap(100, 100)  # Create a placeholder pixmap
            self.arrow_image.fill(QColor(0, 0, 0, 0))  # Fill it with transparency

        self.sensor = MagnetometerSensor()  # Initialize the MagnetometerSensor

    def update_heading_display(self):
        heading = self.sensor.read_heading()
        self.heading = heading
        self.angle_label.setText(f"Heading: {self.heading:.2f}°")
        self.angle_label.font().setPointSize(20)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center = self.rect().center()
        painter.translate(center)
        painter.save()
        painter.rotate(self.heading)
        painter.drawPixmap(-self.arrow_image.width() // 2, -self.arrow_image.height() // 2, self.arrow_image)
        painter.restore()
        if self.target_heading is not None:
            painter.setPen(QPen(QColor('red'), 2, Qt.PenStyle.SolidLine))
            painter.save()
            painter.rotate(self.target_heading)
            painter.drawLine(0, 0, 0, 100)
            painter.restore()

    def closeEvent(self, event):
        if self.sensor:
            del self.sensor
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    compass_widget = CompassWidget()
    compass_widget.show()

    timer = QTimer()
    timer.timeout.connect(compass_widget.update_heading_display)
    timer.start(100)

    sys.exit(app.exec())
