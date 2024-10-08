import math
import sys

from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QVBoxLayout, QApplication
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QPolygon
from PySide6.QtCore import QPoint
from typing import List

from utils.logger import logger


class DisplayBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bnd_points = []
        self.obs_points: List[List[QPoint]] = []
        self.path_points = []
        self.scale = 1  # Initial scale factor
        # self.setFixedSize(400, 300)
        self.margin = 50
        self.outline_rect = self.geometry().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.bounding_rect = self.geometry().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.grid_size = 20
        self.bnd_drawing = False
        self.obs_drawing = False
        self.update()

    def load_field_data(self, field_data, path):
        self.bnd_drawing = False
        self.obs_drawing = False
        self.bnd_points.clear()
        self.obs_points.clear()
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        for sublist in field_data:
            for (x, y) in sublist:
                # Update the min/max values
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        logger.info(f"{min_x}, {min_y}, {max_x}, {max_y}")
        self.bounding_rect.setRect(self.rect().center().x()+min_x-center_x, self.rect().center().y()+min_y-center_y,
                                   max_x-min_x, max_y-min_y)
        logger.info(self.bounding_rect)
        self.outline_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        for (x, y) in field_data[0]:
            new_point = QPoint(self.outline_rect.center().x() + x - center_x,
                               self.outline_rect.center().y() + y - center_y)
            self.bnd_points.append(new_point)
        for sublist in field_data[1:]:
            self.obs_points.append([])
            for (x, y) in sublist:
                new_point = QPoint(self.outline_rect.center().x() + x - center_x,
                                   self.outline_rect.center().y() + y - center_y)
                self.obs_points[len(self.obs_points) - 1].append(new_point)

        self.path_points.clear()
        for (x, y) in path:
            self.path_points.append(
                QPoint(self.outline_rect.center().x() + int(x) - center_x,
                       self.outline_rect.center().y() + int(y) - center_y))

        self.adjust_scale_to_fit()
        print(self.scale)
        self.update()

    def clear_bnd_point(self):
        self.bnd_points.clear()

    def add_bnd_point(self, x, y):
        new_point = QPoint(self.outline_rect.center().x() + x, self.outline_rect.center().y() + y)
        self.bnd_points.append(new_point)
        self.adjust_board(new_point)

    def add_new_obs(self):
        self.obs_points.append([])

    def add_obs_point(self, x, y):
        new_point = QPoint(self.outline_rect.center().x() + x, self.outline_rect.center().y() + y)
        self.obs_points[len(self.obs_points) - 1].append(new_point)
        self.adjust_board(new_point)

    def adjust_board(self, new_point):
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
        painter = QPainter(self)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))

        pen.setWidth(1)
        painter.setPen(pen)
        # rect = self.rect()
        # x = rect.left()
        # while x <= rect.right():
        #     painter.drawLine(x, rect.top(), x, rect.bottom())
        #     x += self.grid_size
        #
        # y = rect.top()
        # while y <= rect.bottom():
        #     painter.drawLine(rect.left(), y, rect.right(), y)
        #     y += self.grid_size

        painter.translate(self.rect().center())
        painter.scale(self.scale, self.scale)
        painter.translate(-self.rect().center())

        if self.bnd_points:
            pen = QPen(QColor(255, 0, 0))
            pen.setWidth(4)
            painter.setPen(pen)
            for i in range(1, len(self.bnd_points)):
                painter.drawLine(self.bnd_points[i - 1], self.bnd_points[i])

            if not self.bnd_drawing:
                painter.drawLine(self.bnd_points[0], self.bnd_points[len(self.bnd_points) - 1])

        if self.obs_points:
            pen = QPen(QColor(0, 0, 0))
            pen.setWidth(1)
            painter.setPen(pen)
            brush = QBrush(QColor(255, 0, 0))  # Red color
            painter.setBrush(brush)

            for i in range(len(self.obs_points) - 1):
                painter.drawPolygon(QPolygon(self.obs_points[i]))

            if self.bnd_drawing:
                for i in range(1, len(self.obs_points[len(self.obs_points) - 1])):
                    painter.drawLine(self.obs_points[len(self.obs_points) - 1][i - 1],
                                     self.obs_points[len(self.obs_points) - 1][i])
            else:
                painter.drawPolygon(QPolygon(self.obs_points[len(self.obs_points) - 1]))

        if self.path_points:
            pen = QPen(QColor(0, 128, 192))
            pen.setWidth(2)
            painter.setPen(pen)
            for i in range(1, len(self.path_points)):
                painter.drawLine(self.path_points[i - 1], self.path_points[i])


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
#         button5 = QPushButton("Clear boundary point", self)
#         button5.clicked.connect(self.clr_bnd_point)
#
#         button1 = QPushButton("Add boundary point", self)
#         button1.clicked.connect(self.add_bnd_point)
#
#         button2 = QPushButton("Add new obstacle", self)
#         button2.clicked.connect(self.add_new_obs)
#
#         button3 = QPushButton("Add obstacle point", self)
#         button3.clicked.connect(self.add_obs_point)
#
#         central_widget = QWidget()
#         layout = QVBoxLayout(central_widget)
#         layout.addWidget(button)
#         layout.addWidget(button5)
#         layout.addWidget(button1)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         self.setCentralWidget(central_widget)
#
#     def clr_bnd_point(self):
#         self.line_widget.clear_bnd_point()
#
#     def add_bnd_point(self):
#         self.line_widget.add_bnd_point(self.index*10, int(math.sin(self.index)*50))
#         self.index = self.index + 1
#
#     def add_new_obs(self):
#         self.line_widget.add_new_obs()
#
#     def add_obs_point(self):
#         self.line_widget.add_obs_point(self.index * 10, int(math.sin(self.index) * 50))
#         self.index = self.index + 1
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
