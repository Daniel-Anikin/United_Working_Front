import sys
import serial

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from MainWidget import Ui_Main_Screen
from DebuggingWidget import Ui_Debugging_menu_screen

flag = 0


class MainScreen(QWidget, Ui_Main_Screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connecting_btns()
        self.Time_of_rotation.valueChanged.connect(self.time_num.display)  # подключаем ползунки
        self.Num_of_iterations.valueChanged.connect(self.iter_num.display)
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # теперь мы можем отправлять сигналы на serial-порт
        self.ser.flush()

    def connecting_btns(self):  # подключаем все кнопки основного экрана
        self.Debug_Btn.clicked.connect(self.debugging_menu)
        self.Start_Btn.clicked.connect(self.start)
        self.Infinity_Btn.clicked.connect(self.infinity)
        self.Stop_Btn.clicked.connect(self.stop)

    def start(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для запуска программы в'
                                                                 ' обычном режиме.\n'
                                                                 'Время вращения барабана'
                                                                 f' - {self.time_num.intValue()}с,\n'
                                                                 f'Количество итераций - {self.iter_num.intValue()}.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x01\n")  # отсылаем сигнал о запуске программы в конечном режиме

    def infinity(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для запуска программы в'
                                                                 ' бесконечном режиме.', ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x02\n")

    def stop(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для остановки программы.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да':
            self.ser.write(b"0x00\n")

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
        self.Rotate_Btn.clicked.connect(self.rotate)
        self.CSV_Btn.clicked.connect(self.CSV)
        self.Lift_Up_Btn.clicked.connect(self.lift_up)
        self.Lift_Down_Btn.clicked.connect(self.lift_down)
        self.Load_Btn.clicked.connect(self.load)
        self.Undo_Btn.clicked.connect(self.undo)

    def rotate(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для запуска вращения барабана.'
                                                                 'Время вращения барабана указано в изначальном виде.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x10\n")

    def CSV(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите Да для запуска СТЗ.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x11\n")

    def lift_up(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для запуска системы подъёма.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x12\n")

    def lift_down(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для спуска системы подъёма.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x13\n")

    def load(self):
        name, choice = QInputDialog.getItem(self, 'Вы уверены?', 'Выберите "Да" для установки барабана '
                                                                 'в режим загрузки.',
                                            ('Да', 'Нет'), 1, False)
        if choice and name == 'Да' and flag == 0:
            self.ser.write(b"0x14\n")

    def undo(self):
        self.main_widget = MainScreen()
        self.close()
        self.main_widget.show()


if __name__ == '__main__':  # запуск дисплея
    app = QApplication(sys.argv)
    ex = MainScreen()
    ex.show()
    sys.exit(app.exec_())
