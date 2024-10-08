import math
import sys

from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QVBoxLayout, QApplication, QToolButton
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QPolygon, QIcon, QCursor, QPixmap
from PySide6.QtCore import QPoint, QSize, Qt
from typing import List

from utils.logger import logger

import ui.res_rc

class DisplayBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.up_btn = QToolButton(self)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.up_btn.setAutoRaise(True)
        self.up_btn.setStyleSheet("""  
                   QToolButton {  
                       background-color: transparent;  
                       border: none;  
                   }  
                   QToolButton:hover {  
                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                   }  
               """)
        icon = QIcon()
        icon.addFile(u":/img/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up_btn.setIcon(icon)
        self.up_btn.setIconSize(QSize(20, 60))

        self.left_btn = QToolButton(self)
        self.left_btn.setObjectName(u"left_btn")
        self.left_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.left_btn.setAutoRaise(True)
        self.left_btn.setStyleSheet("""  
                                   QToolButton {  
                                       background-color: transparent;  
                                       border: none;  
                                   }  
                                   QToolButton:hover {  
                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                   }  
                               """)
        icon = QIcon()
        icon.addFile(u":/img/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.left_btn.setIcon(icon)
        self.left_btn.setIconSize(QSize(60, 20))

        self.down_btn = QToolButton(self)
        self.down_btn.setObjectName(u"down_btn")
        self.down_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.down_btn.setAutoRaise(True)
        self.down_btn.setStyleSheet("""  
                                   QToolButton {  
                                       background-color: transparent;  
                                       border: none;  
                                   }  
                                   QToolButton:hover {  
                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                   }  
                               """)
        icon = QIcon()
        icon.addFile(u":/img/down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.down_btn.setIcon(icon)
        self.down_btn.setIconSize(QSize(20, 60))

        self.right_btn = QToolButton(self)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.right_btn.setAutoRaise(True)
        self.right_btn.setStyleSheet("""  
                                           QToolButton {  
                                               background-color: transparent;  
                                               border: none;  
                                           }  
                                           QToolButton:hover {  
                                               background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                           }  
                                       """)
        icon = QIcon()
        icon.addFile(u":/img/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.right_btn.setIcon(icon)
        self.right_btn.setIconSize(QSize(60, 20))

        self.fit_btn = QToolButton(self)
        self.fit_btn.setObjectName(u"fit_btn")
        self.fit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fit_btn.setAutoRaise(True)
        self.fit_btn.setStyleSheet("""  
                                                   QToolButton {  
                                                       background-color: transparent;  
                                                       border: none;  
                                                   }  
                                                   QToolButton:hover {  
                                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                                   }  
                                               """)
        icon = QIcon()
        icon.addFile(u":/img/fit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fit_btn.setIcon(icon)
        self.fit_btn.setIconSize(QSize(40, 40))

        self.zoom_in = QToolButton(self)
        self.zoom_in.setObjectName(u"zoom_in")
        self.zoom_in.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.zoom_in.setAutoRaise(True)
        self.zoom_in.setStyleSheet("""  
                                                   QToolButton {  
                                                       background-color: transparent;  
                                                       border: none;  
                                                   }  
                                                   QToolButton:hover {  
                                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                                   }  
                                               """)
        icon = QIcon()
        icon.addFile(u":/img/zin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoom_in.setIcon(icon)
        self.zoom_in.setIconSize(QSize(30, 30))

        self.zoom_out = QToolButton(self)
        self.zoom_out.setObjectName(u"right_btn")
        self.zoom_out.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.zoom_out.setAutoRaise(True)
        self.zoom_out.setStyleSheet("""  
                                                   QToolButton {  
                                                       background-color: transparent;  
                                                       border: none;  
                                                   }  
                                                   QToolButton:hover {  
                                                       background-color: rgba(255, 255, 255, 50);  // Example of a slight hover effect  
                                                   }  
                                               """)
        icon = QIcon()
        icon.addFile(u":/img/zout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoom_out.setIcon(icon)
        self.zoom_out.setIconSize(QSize(30, 30))

        self.up_btn.clicked.connect(self.on_up)
        self.down_btn.clicked.connect(self.on_down)
        self.left_btn.clicked.connect(self.on_left)
        self.right_btn.clicked.connect(self.on_right)
        self.fit_btn.clicked.connect(self.on_fit)
        self.zoom_in.clicked.connect(self.on_zoom_in)
        self.zoom_out.clicked.connect(self.on_zoom_out)

        self.bnd_points = []
        self.obs_points: List[List[QPoint]] = []
        self.path_points = []
        self.scale = 1  # Initial scale factor
        # self.setFixedSize(400, 300)
        self.margin = 50
        self.outline_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.bounding_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.grid_size = 20
        self.bnd_drawing = False
        self.obs_drawing = False
        self.transform_x = 0
        self.transform_y = 0
        self.transform_scale = 1
        self.moving_unit = 10
        self.converted_x = 0
        self.converted_y = 0
        self.heading = None
        self.current = None
        self.update()

    def on_up(self):
        self.transform_y = self.transform_y - self.moving_unit
        self.update()

    def on_down(self):
        self.transform_y = self.transform_y + self.moving_unit
        self.update()

    def on_left(self):
        self.transform_x = self.transform_x - self.moving_unit
        self.update()

    def on_right(self):
        self.transform_x = self.transform_x + self.moving_unit
        self.update()

    def on_fit(self):
        self.transform_x = self.transform_y = 0
        self.transform_scale = 1
        self.update()

    def on_zoom_in(self):
        self.transform_scale = self.transform_scale + 0.2
        self.update()

    def on_zoom_out(self):
        self.transform_scale = self.transform_scale - 0.2
        self.update()

    def resizeEvent(self, event):
        self.up_btn.setGeometry(int(event.size().width() / 2), 10, 20, 60)
        self.left_btn.setGeometry(10, int(event.size().height() / 2), 60, 20)
        self.down_btn.setGeometry(int(event.size().width() / 2), event.size().height()-70, 20, 60)
        self.right_btn.setGeometry(event.size().width()-70, int(event.size().height() / 2), 60, 20)
        self.fit_btn.setGeometry(70, event.size().height()-100, 40, 40)
        self.zoom_in.setGeometry(20, event.size().height()-135, 30, 30)
        self.zoom_out.setGeometry(20, event.size().height()-95, 30, 30)

    def clear(self):
        self.bnd_points.clear()
        self.obs_points.clear()
        self.path_points.clear()
        self.scale = 1
        self.outline_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.bounding_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.grid_size = 20
        self.bnd_drawing = False
        self.obs_drawing = False
        self.transform_x = 0
        self.transform_y = 0
        self.transform_scale = 1
        self.moving_unit = 10
        self.converted_x = 0
        self.converted_y = 0
        self.heading = None
        self.current = None
        self.update()

    def init_current(self):
        self.heading = None
        self.current = None

    def set_location(self, point, angle):
        self.current = (point[0]+self.converted_x, point[1]+self.converted_y)
        self.heading = angle
        self.update()

    def load_field_data(self, field_data, path):
        self.clear()
        QApplication.processEvents()
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

        self.bounding_rect.setRect(self.rect().center().x()+min_x-center_x, self.rect().center().y()+min_y-center_y,
                                   max_x-min_x, max_y-min_y)
        self.outline_rect = self.rect().adjusted(self.margin, self.margin, -self.margin, -self.margin)
        self.converted_x = self.outline_rect.center().x() - center_x
        self.converted_y = self.outline_rect.center().y() - center_y
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
                QPoint(self.outline_rect.center().x() + x - center_x,
                       self.outline_rect.center().y() + y - center_y))

        self.adjust_scale_to_fit()
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

        if self.current is not None and self.heading is not None:
            painter.translate(self.current[0], self.current[1])
            painter.save()
            painter.rotate(self.heading)
            arrow_image = QPixmap(u":/img/current.png")
            painter.drawPixmap(-arrow_image.width() // 2, -arrow_image.height() // 2, arrow_image)
            painter.restore()

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
        painter.scale(self.scale*self.transform_scale, self.scale*self.transform_scale)
        painter.translate(-self.rect().center())
        painter.translate(self.transform_x,self.transform_y)

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
