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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AS(object):
    def setupUi(self, AS):
        if not AS.objectName():
            AS.setObjectName(u"AS")
        AS.setEnabled(True)
        AS.resize(638, 441)
        font = QFont()
        font.setPointSize(12)
        AS.setFont(font)
        self.centralwidget = QWidget(AS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	"
                        "border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb("
                        "255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
""
                        "/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52)"
                        ";\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; "
                        "}\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
""
                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	paddi"
                        "ng: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
""
                        "QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
""
                        "    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" Q"
                        "ScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons"
                        "/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width:"
                        " 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
""
                        "    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, "
                        "198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"background-color: rgb(147, 147, 147);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fieldWidget = QWidget(self.widget)
        self.fieldWidget.setObjectName(u"fieldWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldWidget.sizePolicy().hasHeightForWidth())
        self.fieldWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(147, 147, 147, 255))
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
        self.fieldWidget.setPalette(palette)
        self.fieldWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.fieldWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.createF = QPushButton(self.fieldWidget)
        self.createF.setObjectName(u"createF")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(True)
        self.createF.setFont(font1)
        self.createF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createF.setStyleSheet(u"QPushButton { \n"
"	color: black; \n"
"    border: none;  \n"
"    background: none;  \n"
"    padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}  \n"
"QPushButton:hover {  \n"
"    color: #444444;  /* Optional visual feedback */  \n"
"} \n"
"QPushButton:pressed {  \n"
"    color: #888888;  /* Optional visual feedback */  \n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.createF)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_5 = QWidget(self.fieldWidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.generateF = QPushButton(self.widget_5)
        self.generateF.setObjectName(u"generateF")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generateF.sizePolicy().hasHeightForWidth())
        self.generateF.setSizePolicy(sizePolicy1)
        self.generateF.setMinimumSize(QSize(0, 30))
        self.generateF.setSizeIncrement(QSize(0, 0))
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(147, 220, 139, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.generateF.setPalette(palette1)
        self.generateF.setFont(font1)
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

        self.horizontalLayout_4.addWidget(self.generateF)

        self.deleteF = QPushButton(self.widget_5)
        self.deleteF.setObjectName(u"deleteF")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush4 = QBrush(QColor(255, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.deleteF.setPalette(palette2)
        self.deleteF.setFont(font1)
        self.deleteF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteF.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.deleteF)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.fieldWidget)

        self.naviWidget = QWidget(self.widget)
        self.naviWidget.setObjectName(u"naviWidget")
        sizePolicy.setHeightForWidth(self.naviWidget.sizePolicy().hasHeightForWidth())
        self.naviWidget.setSizePolicy(sizePolicy)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.naviWidget.setPalette(palette3)
        self.naviWidget.setFont(font)
        self.horizontalLayout_6 = QHBoxLayout(self.naviWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.naviWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
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
        self.widget_2 = QWidget(self.guidWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.startGuid = QPushButton(self.widget_2)
        self.startGuid.setObjectName(u"startGuid")
        sizePolicy1.setHeightForWidth(self.startGuid.sizePolicy().hasHeightForWidth())
        self.startGuid.setSizePolicy(sizePolicy1)
        self.startGuid.setMinimumSize(QSize(0, 30))
        self.startGuid.setSizeIncrement(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.startGuid.setPalette(palette4)
        self.startGuid.setFont(font1)
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

        self.stopGuid = QPushButton(self.widget_2)
        self.stopGuid.setObjectName(u"stopGuid")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopGuid.setPalette(palette5)
        self.stopGuid.setFont(font1)
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


        self.verticalLayout_8.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.guidWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.addObst = QPushButton(self.widget_3)
        self.addObst.setObjectName(u"addObst")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addObst.sizePolicy().hasHeightForWidth())
        self.addObst.setSizePolicy(sizePolicy2)
        self.addObst.setMinimumSize(QSize(0, 30))
        self.addObst.setSizeIncrement(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush5 = QBrush(QColor(147, 220, 218, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.addObst.setPalette(palette6)
        self.addObst.setFont(font1)
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


        self.verticalLayout_8.addWidget(self.widget_3)


        self.horizontalLayout_6.addWidget(self.guidWidget)

        self.positionWidget = QWidget(self.naviWidget)
        self.positionWidget.setObjectName(u"positionWidget")
        self.verticalLayout_9 = QVBoxLayout(self.positionWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.travelToStart = QPushButton(self.positionWidget)
        self.travelToStart.setObjectName(u"travelToStart")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.travelToStart.sizePolicy().hasHeightForWidth())
        self.travelToStart.setSizePolicy(sizePolicy3)
        self.travelToStart.setMinimumSize(QSize(0, 0))
        self.travelToStart.setSizeIncrement(QSize(0, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.travelToStart.setPalette(palette7)
        self.travelToStart.setFont(font1)
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
        sizePolicy3.setHeightForWidth(self.startCurrent.sizePolicy().hasHeightForWidth())
        self.startCurrent.setSizePolicy(sizePolicy3)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.startCurrent.setPalette(palette8)
        self.startCurrent.setFont(font1)
        self.startCurrent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startCurrent.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: rgb(255, 0, 0);\n"
"	padding-top: 10px;\n"
"    padding-right: 15px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.startCurrent)


        self.horizontalLayout_6.addWidget(self.positionWidget)


        self.verticalLayout_2.addWidget(self.naviWidget)

        self.displayWidget = QWidget(self.widget)
        self.displayWidget.setObjectName(u"displayWidget")
        self.displayWidget.setStyleSheet(u"QWidget{\n"
"	border: 2px solid #000000;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.displayWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_2.addWidget(self.displayWidget)

        self.recordWidget = QWidget(self.widget)
        self.recordWidget.setObjectName(u"recordWidget")
        sizePolicy1.setHeightForWidth(self.recordWidget.sizePolicy().hasHeightForWidth())
        self.recordWidget.setSizePolicy(sizePolicy1)
        self.recordWidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.recordWidget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widget_6 = QWidget(self.recordWidget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy4.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy4)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startBoun = QPushButton(self.widget_7)
        self.startBoun.setObjectName(u"startBoun")
        sizePolicy1.setHeightForWidth(self.startBoun.sizePolicy().hasHeightForWidth())
        self.startBoun.setSizePolicy(sizePolicy1)
        self.startBoun.setMinimumSize(QSize(0, 30))
        self.startBoun.setSizeIncrement(QSize(0, 0))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.startBoun.setPalette(palette9)
        self.startBoun.setFont(font1)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stopBoun.sizePolicy().hasHeightForWidth())
        self.stopBoun.setSizePolicy(sizePolicy5)
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopBoun.setPalette(palette10)
        self.stopBoun.setFont(font1)
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
        sizePolicy4.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy4)
        self.widget_10.setStyleSheet(u"#widget_10{\n"
"	border: 2px solid #000000;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 2)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy4.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy4)
        self.verticalLayout_6 = QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy4.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.startExzn = QPushButton(self.widget_12)
        self.startExzn.setObjectName(u"startExzn")
        sizePolicy1.setHeightForWidth(self.startExzn.sizePolicy().hasHeightForWidth())
        self.startExzn.setSizePolicy(sizePolicy1)
        self.startExzn.setMinimumSize(QSize(0, 30))
        self.startExzn.setSizeIncrement(QSize(0, 0))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.startExzn.setPalette(palette11)
        self.startExzn.setFont(font1)
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
        sizePolicy5.setHeightForWidth(self.stopExzn.sizePolicy().hasHeightForWidth())
        self.stopExzn.setSizePolicy(sizePolicy5)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.stopExzn.setPalette(palette12)
        self.stopExzn.setFont(font1)
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


        self.verticalLayout.addWidget(self.widget)

        AS.setCentralWidget(self.centralwidget)

        self.retranslateUi(AS)

        QMetaObject.connectSlotsByName(AS)
    # setupUi

    def retranslateUi(self, AS):
        AS.setWindowTitle(QCoreApplication.translate("AS", u"AutoSlasher", None))
        self.createF.setText(QCoreApplication.translate("AS", u"Create New Field", None))
        self.generateF.setText(QCoreApplication.translate("AS", u" Generate Field", None))
        self.deleteF.setText(QCoreApplication.translate("AS", u" Delete Field", None))
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

