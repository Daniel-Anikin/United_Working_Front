import sys
import serial

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QInputDialog, QSlider
from MainWidget import Ui_Main_Screen
from DebuggingWidget import Ui_Debugging_menu_screen


class MainScreen(QWidget, Ui_Main_Screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Main screen')
        self.connecting_btns()
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.ser.flush()

    def connecting_btns(self):
        self.Debug_Btn.clicked.connect(self.debugging_menu)
        self.Start_Btn.clicked.connect(self.start)
        self.Infinity_Btn.clicked.connect(self.infinity)
        self.Stop_Btn.clicked.connect(self.stop)

    def start(self):
        self.ser.write(b"0x00\n")

    def infinity(self):
        self.ser.write(b"0x01\n")

    def stop(self):
        self.ser.write(b"0x02\n")

    def debugging_menu(self):
        self.debug_widget = DebuggingMenu()
        self.close()
        self.debug_widget.show()


class DebuggingMenu(QWidget, Ui_Debugging_menu_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connecting_btns()

    def connecting_btns(self):
        self.Stop_Btn.clicked.connect(self.stop)
        self.Rotate_Btn.clicked.connect(self.rotate)
        self.CSV_Btn.clicked.connect(self.CSV)
        self.Lift_Up_Btn.clicked.connect(self.lift_up)
        self.Lift_Down_Btn.clicked.connect(self.lift_down)
        self.Load_Btn.clicked.connect(self.load)
        self.Undo_Btn.clicked.connect(self.undo)

    def stop(self):
        self.ser.write(b"0x02\n")

    def rotate(self):
        self.ser.write(b"0x10\n")

    def CSV(self):
        self.ser.write(b"0x11\n")

    def lift_up(self):
        self.ser.write(b"0x12\n")

    def lift_down(self):
        self.ser.write(b"0x13\n")

    def load(self):
        self.ser.write(b"0x14\n")

    def undo(self):
        self.main_widget = MainScreen()
        self.close()
        self.main_widget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreen()
    ex.show()
    sys.exit(app.exec_())
