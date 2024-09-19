import sys

from PySide6 import QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_as import Ui_AS
from widget.popup import RecordingPopup


class AutoSlasher(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AS()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.combo_field.addItem("Option 1")
        self.ui.combo_field.addItem("Option 2")
        self.ui.combo_field.addItem("Option 3")
        self.ui.combo_field.currentIndexChanged.connect(self.handle_activated)

        RecordingPopup(self).show()

    def handle_activated(self, index):
        print(index)
        self.ui.combo_field.blockSignals(True)
        self.ui.combo_field.setCurrentText(f"Selected Field: {self.ui.combo_field.itemText(index)}")
        self.ui.combo_field.blockSignals(False)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    window.show()
    sys.exit(app.exec())
