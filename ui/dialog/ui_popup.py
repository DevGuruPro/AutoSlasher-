# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import ui.res_rc

class Ui_PopUpDialog(object):
    def setupUi(self, PopUpDialog):
        if not PopUpDialog.objectName():
            PopUpDialog.setObjectName(u"PopUpDialog")
        PopUpDialog.resize(250, 88)
        self.verticalLayout = QVBoxLayout(PopUpDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(PopUpDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bnd_label = QLabel(self.widget)
        self.bnd_label.setObjectName(u"bnd_label")
        self.bnd_label.setPixmap(QPixmap(u":/img/popup_boundary.png"))

        self.verticalLayout_2.addWidget(self.bnd_label)

        self.obs_label = QLabel(self.widget)
        self.obs_label.setObjectName(u"obs_label")
        self.obs_label.setPixmap(QPixmap(u":/img/popup_obstale.png"))

        self.verticalLayout_2.addWidget(self.obs_label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(PopUpDialog)

        QMetaObject.connectSlotsByName(PopUpDialog)
    # setupUi

    def retranslateUi(self, PopUpDialog):
        PopUpDialog.setWindowTitle(QCoreApplication.translate("PopUpDialog", u"Popup", None))
        self.bnd_label.setText("")
        self.obs_label.setText("")
    # retranslateUi

