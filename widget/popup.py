from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog

from ui.dialog.ui_popup import Ui_PopUpDialog


class RecordingPopup(QDialog):

    def __init__(self, app):
        super().__init__(parent=app)
        self.ui = Ui_PopUpDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.obs_label.hide()

    def set_type(self, m_type):
        if m_type == "boundary":
            self.ui.bnd_label.show()
            self.ui.obs_label.hide()
        elif m_type == "obstacle":
            self.ui.bnd_label.hide()
            self.ui.obs_label.show()
