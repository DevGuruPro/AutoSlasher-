import os

from PySide6 import QtCore
from PySide6.QtGui import Qt, QMovie
from PySide6.QtWidgets import QDialog

from ui.dialog.ui_nameDlg import Ui_NameDialog

import ui.res_rc


class NameDlg(QDialog):

    def __init__(self, app):
        super().__init__(parent=app)
        self.ui = Ui_NameDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.setBtn.released.connect(self.close)

    def get_name(self):
        return self.ui.lineEdit.text()
