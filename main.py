import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.ui_as import Ui_AS


class AutoSlasher(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AS()
        self.ui.setupUi(self)

        self.ui.fieldWidget.hide()
        # self.ui.naviWidget.hide()
        self.ui.guidWidget.hide()
        self.ui.recordWidget.hide()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AutoSlasher()
    window.show()
    sys.exit(app.exec())
