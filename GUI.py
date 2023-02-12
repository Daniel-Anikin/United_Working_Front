import sys
import sqlite3
import serial

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QInputDialog, QSlider
from PyQt5.QtGui import QImage, QPalette, QBrush
from MainWidget import Ui_Main_Screen


class MainScreen(QWidget, Ui_Main_Screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Main screen')
        self.Debug_Btn.clicked.connect(self.debugging_menu)
        self.Start_Btn.clicked.connect(self.start)
        self.Infinity_Btn.clicked.connect(self.infinity)
        self.Stop_Btn.clicked.connect(self.stop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreen()
    ex.show()
    sys.exit(app.exec_())
