import math
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import QPoint


class DisplayBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.points = []
        self.scale = 1.0  # Initial scale factor
        self.setFixedSize(400, 300)
        margin = 50
        self.outline_rect = self.geometry().adjusted(margin, margin, -margin, -margin)
        self.bounding_rect = self.geometry().adjusted(margin, margin, -margin, -margin)

    def add_point(self, x, y):
        new_point = QPoint(self.outline_rect.center().x()+x, self.outline_rect.center().y()+y)
        self.points.append(new_point)

        if not self.bounding_rect.contains(new_point):

            if new_point.x() < self.bounding_rect.topLeft().x():
                self.bounding_rect.setLeft(new_point.x())
            elif new_point.x() > self.bounding_rect.bottomRight().x():
                self.bounding_rect.setRight(new_point.x())
            if new_point.y() < self.bounding_rect.topLeft().y():
                self.bounding_rect.setTop(new_point.x())
            elif new_point.y() > self.bounding_rect.bottomRight().y():
                self.bounding_rect.setBottom(new_point.x())

            self.adjust_scale_to_fit()

        self.update()

    def adjust_scale_to_fit(self):
        scale_x = self.outline_rect.width() / self.bounding_rect.width()
        scale_y = self.outline_rect.height() / self.bounding_rect.height()
        self.scale = min(scale_x, scale_y)

    def paintEvent(self, event):
        if not self.points:
            return

        painter = QPainter(self)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(self.outline_rect)

        painter.scale(self.scale, self.scale)

        for i in range(1, len(self.points)-1):
            painter.drawLine(self.points[i-1], self.points[i])


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main Window")
#         self.setGeometry(50, 50, 400, 300)
#
#         self.init_ui()
#         self.line_widget = DisplayBoard()
#         self.index = 0
#
#     def init_ui(self):
#         button = QPushButton("Open LineWidget", self)
#         button.clicked.connect(self.show_board)
#
#         button1 = QPushButton("Add", self)
#         button1.clicked.connect(self.add_point)
#
#         central_widget = QWidget()
#         layout = QVBoxLayout(central_widget)
#         layout.addWidget(button)
#         layout.addWidget(button1)
#         self.setCentralWidget(central_widget)
#
#     def add_point(self):
#         self.line_widget.add_point(self.index*10, int(math.sin(self.index)*50))
#         self.index = self.index+1
#
#     def show_board(self):
#         self.line_widget.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())
