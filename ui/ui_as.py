# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'as.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import ui.res_rc

class Ui_AS(object):
    def setupUi(self, AS):
        if not AS.objectName():
            AS.setObjectName(u"AS")
        AS.resize(800, 1399)
        self.centralwidget = QWidget(AS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.startPage = QWidget(self.centralwidget)
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_11 = QVBoxLayout(self.startPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.startPage)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)

        self.widget_13 = QWidget(self.startPage)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setStyleSheet(u"QPushButton {  \n"
"    background-color: #4CAF50; /* Green background */  \n"
"    color: white; /* Text color */  \n"
"    border: 2px solid #4CAF50; /* Border */  \n"
"    border-radius: 10px; /* Optional: rounded corners */  \n"
"    padding: 5px; /* Optional: padding for text */  \n"
"    /* Ensure the button responds to mouse events */  \n"
"    pointer-events: auto;   \n"
"}  ")
        self.verticalLayout_12 = QVBoxLayout(self.widget_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.m_settingBtn = QPushButton(self.widget_14)
        self.m_settingBtn.setObjectName(u"m_settingBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.m_settingBtn.sizePolicy().hasHeightForWidth())
        self.m_settingBtn.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.m_settingBtn.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.m_settingBtn.setFont(font)
        self.m_settingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.m_settingBtn.setStyleSheet(u"QPushButton {  \n"
"	color: rgb(85, 170, 255);\n"
"	color: rgb(50, 224, 227);\n"
"    background-color: #55aaff; /* Green background */  \n"
"	color: rgb(78, 202, 255);\n"
"    color: black; /* White text */  \n"
"    border: 2px solid #55aaff; /* Border */  \n"
"    border-radius: 10px; /* Rounded corners */  \n"
"    padding: 10px 20px; /* Padding for content */  \n"
"}  \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: #50a0f0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: #4090e0; /* Darker green when pressed */  \n"
"}  ")

        self.verticalLayout_12.addWidget(self.m_settingBtn)

        self.f_manaBtn = QPushButton(self.widget_14)
        self.f_manaBtn.setObjectName(u"f_manaBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.f_manaBtn.sizePolicy().hasHeightForWidth())
        self.f_manaBtn.setSizePolicy(sizePolicy2)
        self.f_manaBtn.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.f_manaBtn.setPalette(palette1)
        self.f_manaBtn.setFont(font)
        self.f_manaBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.f_manaBtn.setStyleSheet(u"QPushButton {  \n"
"	color: rgb(85, 170, 255);\n"
"	color: rgb(50, 224, 227);\n"
"    background-color: #55aaff; /* Green background */  \n"
"	color: rgb(78, 202, 255);\n"
"    color: black; /* White text */  \n"
"    border: 2px solid #55aaff; /* Border */  \n"
"    border-radius: 10px; /* Rounded corners */  \n"
"    padding: 10px 20px; /* Padding for content */  \n"
"}  \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: #50a0f0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: #4090e0; /* Darker green when pressed */  \n"
"}  ")

        self.verticalLayout_12.addWidget(self.f_manaBtn)

        self.widget = QWidget(self.widget_14)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_19 = QHBoxLayout(self.widget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_10)

        self.combo_field = QComboBox(self.widget)
        self.combo_field.addItem("")
        self.combo_field.addItem("")
        self.combo_field.setObjectName(u"combo_field")
        self.combo_field.setFont(font)
        self.combo_field.setStyleSheet(u"QComboBox {  \n"
"	color: rgb(85, 170, 255);\n"
"	color: rgb(50, 224, 227);\n"
"    background-color: #55aaff; /* Green background */  \n"
"	color: rgb(78, 202, 255);\n"
"    color: black; /* White text */  \n"
"    border: 2px solid #55aaff; /* Border */  \n"
"    border-radius: 10px; /* Rounded corners */  \n"
"    padding: 10px 20px; /* Padding for content */  \n"
"}  \n"
"\n"
"QComboBox:hover {  \n"
"    background-color: #50a0f0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QComboBox:pressed {  \n"
"    background-color: #4090e0; /* Darker green when pressed */  \n"
"}  ")

        self.horizontalLayout_19.addWidget(self.combo_field)


        self.verticalLayout_12.addWidget(self.widget)


        self.horizontalLayout_9.addWidget(self.widget_14)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.startPage)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.startBtn = QToolButton(self.widget_15)
        self.startBtn.setObjectName(u"startBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy4)
        self.startBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startBtn.setStyleSheet(u"QToolButton {\n"
"\n"
"    border: none; /* Remove the border */  \n"
"}")
        icon = QIcon()
        icon.addFile(u":/img/start_btn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startBtn.setIcon(icon)
        self.startBtn.setIconSize(QSize(300, 80))

        self.horizontalLayout_10.addWidget(self.startBtn)


        self.verticalLayout_11.addWidget(self.widget_15)


        self.verticalLayout.addWidget(self.startPage)

        self.settingPage = QWidget(self.centralwidget)
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_19 = QVBoxLayout(self.settingPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(30, -1, 30, -1)
        self.label_9 = QLabel(self.settingPage)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_19.addWidget(self.label_9)

        self.widget_25 = QWidget(self.settingPage)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_11 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)

        self.settingTable = QTableWidget(self.widget_25)
        if (self.settingTable.columnCount() < 3):
            self.settingTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.settingTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.settingTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.settingTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.settingTable.rowCount() < 6):
            self.settingTable.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.settingTable.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.settingTable.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.settingTable.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.settingTable.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.settingTable.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.settingTable.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.settingTable.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.settingTable.setItem(3, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.settingTable.setItem(3, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.settingTable.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.settingTable.setItem(4, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.settingTable.setItem(5, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.settingTable.setItem(5, 1, __qtablewidgetitem20)
        self.settingTable.setObjectName(u"settingTable")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.settingTable.sizePolicy().hasHeightForWidth())
        self.settingTable.setSizePolicy(sizePolicy5)
        self.settingTable.setAutoScrollMargin(16)
        self.settingTable.setSortingEnabled(False)
        self.settingTable.horizontalHeader().setVisible(True)
        self.settingTable.horizontalHeader().setCascadingSectionResizes(False)
        self.settingTable.horizontalHeader().setDefaultSectionSize(100)
        self.settingTable.horizontalHeader().setHighlightSections(False)
        self.settingTable.horizontalHeader().setStretchLastSection(True)
        self.settingTable.verticalHeader().setVisible(False)
        self.settingTable.verticalHeader().setCascadingSectionResizes(False)
        self.settingTable.verticalHeader().setMinimumSectionSize(23)
        self.settingTable.verticalHeader().setDefaultSectionSize(30)

        self.horizontalLayout_17.addWidget(self.settingTable)

        self.horizontalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)


        self.verticalLayout_19.addWidget(self.widget_25)


        self.verticalLayout.addWidget(self.settingPage)

        self.fmanagerPage = QWidget(self.centralwidget)
        self.fmanagerPage.setObjectName(u"fmanagerPage")
        self.verticalLayout_20 = QVBoxLayout(self.fmanagerPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(30, -1, 30, -1)
        self.label_11 = QLabel(self.fmanagerPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_20.addWidget(self.label_11)

        self.widget_26 = QWidget(self.fmanagerPage)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_13 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.settingTable_2 = QTableWidget(self.widget_26)
        if (self.settingTable_2.columnCount() < 2):
            self.settingTable_2.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.settingTable_2.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.settingTable_2.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        if (self.settingTable_2.rowCount() < 6):
            self.settingTable_2.setRowCount(6)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.settingTable_2.setVerticalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.settingTable_2.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.settingTable_2.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.settingTable_2.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.settingTable_2.setItem(1, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.settingTable_2.setItem(2, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.settingTable_2.setItem(2, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.settingTable_2.setItem(3, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.settingTable_2.setItem(3, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.settingTable_2.setItem(4, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.settingTable_2.setItem(4, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.settingTable_2.setItem(5, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.settingTable_2.setItem(5, 1, __qtablewidgetitem40)
        self.settingTable_2.setObjectName(u"settingTable_2")
        sizePolicy5.setHeightForWidth(self.settingTable_2.sizePolicy().hasHeightForWidth())
        self.settingTable_2.setSizePolicy(sizePolicy5)
        self.settingTable_2.setAutoScrollMargin(16)
        self.settingTable_2.setSortingEnabled(False)
        self.settingTable_2.horizontalHeader().setVisible(True)
        self.settingTable_2.horizontalHeader().setCascadingSectionResizes(False)
        self.settingTable_2.horizontalHeader().setMinimumSectionSize(20)
        self.settingTable_2.horizontalHeader().setDefaultSectionSize(100)
        self.settingTable_2.horizontalHeader().setHighlightSections(False)
        self.settingTable_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.settingTable_2.horizontalHeader().setStretchLastSection(False)
        self.settingTable_2.verticalHeader().setVisible(False)
        self.settingTable_2.verticalHeader().setCascadingSectionResizes(False)
        self.settingTable_2.verticalHeader().setMinimumSectionSize(23)
        self.settingTable_2.verticalHeader().setDefaultSectionSize(30)
        self.settingTable_2.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_18.addWidget(self.settingTable_2)

        self.horizontalSpacer_14 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)


        self.verticalLayout_20.addWidget(self.widget_26)


        self.verticalLayout.addWidget(self.fmanagerPage)

        self.fieldPage = QWidget(self.centralwidget)
        self.fieldPage.setObjectName(u"fieldPage")
        self.fieldPage.setMaximumSize(QSize(16777215, 16777215))
        self.fieldPage.setStyleSheet(u"background-color: rgb(147, 147, 147);")
        self.verticalLayout_2 = QVBoxLayout(self.fieldPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fieldWidget = QWidget(self.fieldPage)
        self.fieldWidget.setObjectName(u"fieldWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.fieldWidget.sizePolicy().hasHeightForWidth())
        self.fieldWidget.setSizePolicy(sizePolicy6)
        palette2 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(147, 147, 147, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.fieldWidget.setPalette(palette2)
        font2 = QFont()
        font2.setPointSize(12)
        self.fieldWidget.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.fieldWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.fieldWidget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_5 = QWidget(self.fieldWidget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.deleteF = QPushButton(self.widget_5)
        self.deleteF.setObjectName(u"deleteF")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.deleteF.sizePolicy().hasHeightForWidth())
        self.deleteF.setSizePolicy(sizePolicy7)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(255, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.deleteF.setPalette(palette3)
        self.deleteF.setFont(font3)
        self.deleteF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteF.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.verticalLayout_10.addWidget(self.deleteF)

        self.generateF = QPushButton(self.widget_5)
        self.generateF.setObjectName(u"generateF")
        sizePolicy7.setHeightForWidth(self.generateF.sizePolicy().hasHeightForWidth())
        self.generateF.setSizePolicy(sizePolicy7)
        self.generateF.setMinimumSize(QSize(0, 20))
        self.generateF.setMaximumSize(QSize(16777215, 16777215))
        self.generateF.setSizeIncrement(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(147, 220, 139, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.generateF.setPalette(palette4)
        self.generateF.setFont(font3)
        self.generateF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.generateF.setFocusPolicy(Qt.NoFocus)
        self.generateF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.generateF.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 139);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.generateF.setIconSize(QSize(16, 16))

        self.verticalLayout_10.addWidget(self.generateF)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.fieldWidget)

        self.naviWidget = QWidget(self.fieldPage)
        self.naviWidget.setObjectName(u"naviWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.naviWidget.sizePolicy().hasHeightForWidth())
        self.naviWidget.setSizePolicy(sizePolicy8)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.naviWidget.setPalette(palette5)
        self.naviWidget.setFont(font2)
        self.horizontalLayout_6 = QHBoxLayout(self.naviWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.naviWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.guidWidget = QWidget(self.naviWidget)
        self.guidWidget.setObjectName(u"guidWidget")
        self.verticalLayout_8 = QVBoxLayout(self.guidWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.guidWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.startGuid = QPushButton(self.widget_3)
        self.startGuid.setObjectName(u"startGuid")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.startGuid.sizePolicy().hasHeightForWidth())
        self.startGuid.setSizePolicy(sizePolicy9)
        self.startGuid.setMinimumSize(QSize(0, 30))
        self.startGuid.setSizeIncrement(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.startGuid.setPalette(palette6)
        self.startGuid.setFont(font3)
        self.startGuid.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startGuid.setFocusPolicy(Qt.NoFocus)
        self.startGuid.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.startGuid.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 139);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.startGuid.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.startGuid)

        self.stopGuid = QPushButton(self.widget_3)
        self.stopGuid.setObjectName(u"stopGuid")
        sizePolicy7.setHeightForWidth(self.stopGuid.sizePolicy().hasHeightForWidth())
        self.stopGuid.setSizePolicy(sizePolicy7)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopGuid.setPalette(palette7)
        self.stopGuid.setFont(font3)
        self.stopGuid.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stopGuid.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.stopGuid)


        self.verticalLayout_8.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.guidWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.addObst = QPushButton(self.widget_4)
        self.addObst.setObjectName(u"addObst")
        sizePolicy7.setHeightForWidth(self.addObst.sizePolicy().hasHeightForWidth())
        self.addObst.setSizePolicy(sizePolicy7)
        self.addObst.setMinimumSize(QSize(0, 30))
        self.addObst.setSizeIncrement(QSize(0, 0))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(147, 220, 218, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.addObst.setPalette(palette8)
        self.addObst.setFont(font3)
        self.addObst.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addObst.setFocusPolicy(Qt.NoFocus)
        self.addObst.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.addObst.setAutoFillBackground(False)
        self.addObst.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 218);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.addObst.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.addObst)


        self.verticalLayout_8.addWidget(self.widget_4)


        self.horizontalLayout_6.addWidget(self.guidWidget)

        self.positionWidget = QWidget(self.naviWidget)
        self.positionWidget.setObjectName(u"positionWidget")
        self.verticalLayout_9 = QVBoxLayout(self.positionWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.travelToStart = QPushButton(self.positionWidget)
        self.travelToStart.setObjectName(u"travelToStart")
        sizePolicy7.setHeightForWidth(self.travelToStart.sizePolicy().hasHeightForWidth())
        self.travelToStart.setSizePolicy(sizePolicy7)
        self.travelToStart.setMinimumSize(QSize(0, 0))
        self.travelToStart.setSizeIncrement(QSize(0, 0))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.travelToStart.setPalette(palette9)
        self.travelToStart.setFont(font3)
        self.travelToStart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.travelToStart.setFocusPolicy(Qt.NoFocus)
        self.travelToStart.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.travelToStart.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 139);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.travelToStart.setIconSize(QSize(16, 16))

        self.verticalLayout_9.addWidget(self.travelToStart)

        self.startCurrent = QPushButton(self.positionWidget)
        self.startCurrent.setObjectName(u"startCurrent")
        sizePolicy7.setHeightForWidth(self.startCurrent.sizePolicy().hasHeightForWidth())
        self.startCurrent.setSizePolicy(sizePolicy7)
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush7 = QBrush(QColor(0, 163, 245, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.startCurrent.setPalette(palette10)
        self.startCurrent.setFont(font3)
        self.startCurrent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startCurrent.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(0,163, 245);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.startCurrent)


        self.horizontalLayout_6.addWidget(self.positionWidget)


        self.verticalLayout_2.addWidget(self.naviWidget)

        self.displayWidget = QWidget(self.fieldPage)
        self.displayWidget.setObjectName(u"displayWidget")
        self.displayWidget.setStyleSheet(u"QWidget{\n"
"	border: 2px solid #000000;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.displayWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_2.addWidget(self.displayWidget)

        self.recordWidget = QWidget(self.fieldPage)
        self.recordWidget.setObjectName(u"recordWidget")
        sizePolicy4.setHeightForWidth(self.recordWidget.sizePolicy().hasHeightForWidth())
        self.recordWidget.setSizePolicy(sizePolicy4)
        self.recordWidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.recordWidget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widget_6 = QWidget(self.recordWidget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy10)
        self.widget_6.setStyleSheet(u"#widget_6{\n"
"	border: 2px solid #000000;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 2, 2)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy10.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy10)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startBoun = QPushButton(self.widget_7)
        self.startBoun.setObjectName(u"startBoun")
        sizePolicy4.setHeightForWidth(self.startBoun.sizePolicy().hasHeightForWidth())
        self.startBoun.setSizePolicy(sizePolicy4)
        self.startBoun.setMinimumSize(QSize(0, 30))
        self.startBoun.setSizeIncrement(QSize(0, 0))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.startBoun.setPalette(palette11)
        self.startBoun.setFont(font3)
        self.startBoun.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startBoun.setFocusPolicy(Qt.NoFocus)
        self.startBoun.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.startBoun.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 139);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.startBoun.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.startBoun)

        self.stopBoun = QPushButton(self.widget_7)
        self.stopBoun.setObjectName(u"stopBoun")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.stopBoun.sizePolicy().hasHeightForWidth())
        self.stopBoun.setSizePolicy(sizePolicy11)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopBoun.setPalette(palette12)
        self.stopBoun.setFont(font3)
        self.stopBoun.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stopBoun.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.stopBoun)


        self.verticalLayout_3.addWidget(self.widget_7)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_10 = QWidget(self.recordWidget)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy10.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy10)
        self.widget_10.setStyleSheet(u"#widget_10{\n"
"	border: 2px solid #000000;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 2)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy10.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy10)
        self.verticalLayout_6 = QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")
        sizePolicy10.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy10)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy10.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy10)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.startExzn = QPushButton(self.widget_12)
        self.startExzn.setObjectName(u"startExzn")
        sizePolicy9.setHeightForWidth(self.startExzn.sizePolicy().hasHeightForWidth())
        self.startExzn.setSizePolicy(sizePolicy9)
        self.startExzn.setMinimumSize(QSize(0, 30))
        self.startExzn.setSizeIncrement(QSize(0, 0))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.startExzn.setPalette(palette13)
        self.startExzn.setFont(font3)
        self.startExzn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startExzn.setFocusPolicy(Qt.NoFocus)
        self.startExzn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.startExzn.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(147, 220, 139);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")
        self.startExzn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.startExzn)

        self.stopExzn = QPushButton(self.widget_12)
        self.stopExzn.setObjectName(u"stopExzn")
        sizePolicy9.setHeightForWidth(self.stopExzn.sizePolicy().hasHeightForWidth())
        self.stopExzn.setSizePolicy(sizePolicy9)
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopExzn.setPalette(palette14)
        self.stopExzn.setFont(font3)
        self.stopExzn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stopExzn.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.stopExzn)


        self.verticalLayout_5.addWidget(self.widget_12)


        self.horizontalLayout_3.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.recordWidget)


        self.verticalLayout.addWidget(self.fieldPage)

        self.movingWidget = QWidget(self.centralwidget)
        self.movingWidget.setObjectName(u"movingWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.movingWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout.addWidget(self.movingWidget)

        AS.setCentralWidget(self.centralwidget)

        self.retranslateUi(AS)

        QMetaObject.connectSlotsByName(AS)
    # setupUi

    def retranslateUi(self, AS):
        AS.setWindowTitle(QCoreApplication.translate("AS", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("AS", u"TextLabel", None))
        self.m_settingBtn.setText(QCoreApplication.translate("AS", u"Machine Settings", None))
        self.f_manaBtn.setText(QCoreApplication.translate("AS", u"Field Manager", None))
        self.label_10.setText(QCoreApplication.translate("AS", u"Selected Field :", None))
        self.combo_field.setItemText(0, QCoreApplication.translate("AS", u"Field 1", None))
        self.combo_field.setItemText(1, QCoreApplication.translate("AS", u"Field 2", None))

        self.combo_field.setCurrentText(QCoreApplication.translate("AS", u"Field 1", None))
        self.startBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("AS", u"Settings", None))
        ___qtablewidgetitem = self.settingTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AS", u"PARAMETER", None));
        ___qtablewidgetitem1 = self.settingTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AS", u"UNIT", None));
        ___qtablewidgetitem2 = self.settingTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AS", u"VALUE", None));
        ___qtablewidgetitem3 = self.settingTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AS", u"1", None));
        ___qtablewidgetitem4 = self.settingTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AS", u"2", None));
        ___qtablewidgetitem5 = self.settingTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AS", u"3", None));
        ___qtablewidgetitem6 = self.settingTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AS", u"4", None));
        ___qtablewidgetitem7 = self.settingTable.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AS", u"5", None));
        ___qtablewidgetitem8 = self.settingTable.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AS", u"6", None));

        __sortingEnabled = self.settingTable.isSortingEnabled()
        self.settingTable.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.settingTable.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AS", u"SPEED", None));
        ___qtablewidgetitem10 = self.settingTable.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AS", u"%", None));
        ___qtablewidgetitem11 = self.settingTable.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AS", u"OVERLAP", None));
        ___qtablewidgetitem12 = self.settingTable.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AS", u"%", None));
        ___qtablewidgetitem13 = self.settingTable.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AS", u"BOUNDARY AVOIDANCE", None));
        ___qtablewidgetitem14 = self.settingTable.item(2, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("AS", u"MM", None));
        ___qtablewidgetitem15 = self.settingTable.item(3, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("AS", u"OBSTACLE AVOIDANCE", None));
        ___qtablewidgetitem16 = self.settingTable.item(3, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("AS", u"MM", None));
        ___qtablewidgetitem17 = self.settingTable.item(4, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("AS", u"FIELD AUTO CORRECT", None));
        ___qtablewidgetitem18 = self.settingTable.item(4, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("AS", u"MM", None));
        ___qtablewidgetitem19 = self.settingTable.item(5, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("AS", u"OUT OF BOUNDS TOLERANCE", None));
        ___qtablewidgetitem20 = self.settingTable.item(5, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("AS", u"MM", None));
        self.settingTable.setSortingEnabled(__sortingEnabled)

        self.label_11.setText(QCoreApplication.translate("AS", u"Field Manager", None))
        ___qtablewidgetitem21 = self.settingTable_2.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("AS", u"Field Name", None));
        ___qtablewidgetitem22 = self.settingTable_2.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("AS", u"Delete", None));
        ___qtablewidgetitem23 = self.settingTable_2.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("AS", u"1", None));
        ___qtablewidgetitem24 = self.settingTable_2.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("AS", u"2", None));
        ___qtablewidgetitem25 = self.settingTable_2.verticalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("AS", u"3", None));
        ___qtablewidgetitem26 = self.settingTable_2.verticalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("AS", u"4", None));
        ___qtablewidgetitem27 = self.settingTable_2.verticalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("AS", u"5", None));
        ___qtablewidgetitem28 = self.settingTable_2.verticalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("AS", u"6", None));

        __sortingEnabled1 = self.settingTable_2.isSortingEnabled()
        self.settingTable_2.setSortingEnabled(False)
        self.settingTable_2.setSortingEnabled(__sortingEnabled1)

        self.label_4.setText(QCoreApplication.translate("AS", u"Create New Field", None))
        self.deleteF.setText(QCoreApplication.translate("AS", u"Discard", None))
        self.generateF.setText(QCoreApplication.translate("AS", u" Generate Field", None))
        self.label_3.setText(QCoreApplication.translate("AS", u"Auto Mode - RTK GPS Guidance\n"
"Field : Front Yard1", None))
        self.startGuid.setText(QCoreApplication.translate("AS", u"Start", None))
        self.stopGuid.setText(QCoreApplication.translate("AS", u"Stop", None))
        self.addObst.setText(QCoreApplication.translate("AS", u"Add Obstacle", None))
        self.travelToStart.setText(QCoreApplication.translate("AS", u"Travel to Start Point", None))
        self.startCurrent.setText(QCoreApplication.translate("AS", u"Start Current Position", None))
        self.label.setText(QCoreApplication.translate("AS", u"Record Boundary", None))
        self.startBoun.setText(QCoreApplication.translate("AS", u"Start", None))
        self.stopBoun.setText(QCoreApplication.translate("AS", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("AS", u"Record Exclusion Zone", None))
        self.startExzn.setText(QCoreApplication.translate("AS", u"Start", None))
        self.stopExzn.setText(QCoreApplication.translate("AS", u"Stop", None))
    # retranslateUi

