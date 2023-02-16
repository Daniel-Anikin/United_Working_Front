# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DebuggingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Debugging_menu_screen(object):
    def setupUi(self, Debugging_menu_screen):
        Debugging_menu_screen.setObjectName("Debugging_menu_screen")
        Debugging_menu_screen.resize(1080, 720)
        self.Rotate_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Rotate_Btn.setGeometry(QtCore.QRect(455, 230, 150, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Rotate_Btn.setFont(font)
        self.Rotate_Btn.setObjectName("Rotate_Btn")
        self.CSV_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.CSV_Btn.setGeometry(QtCore.QRect(645, 340, 150, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CSV_Btn.setFont(font)
        self.CSV_Btn.setObjectName("CSV_Btn")
        self.Lift_Up_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Lift_Up_Btn.setGeometry(QtCore.QRect(540, 490, 155, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lift_Up_Btn.setFont(font)
        self.Lift_Up_Btn.setObjectName("Lift_Up_Btn")
        self.Load_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Load_Btn.setGeometry(QtCore.QRect(354, 490, 155, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Load_Btn.setFont(font)
        self.Load_Btn.setObjectName("Load_Btn")
        self.Lift_Down_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Lift_Down_Btn.setGeometry(QtCore.QRect(265, 340, 150, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lift_Down_Btn.setFont(font)
        self.Lift_Down_Btn.setObjectName("Lift_Down_Btn")
        self.Debugging_screen = QtWidgets.QLabel(Debugging_menu_screen)
        self.Debugging_screen.setGeometry(QtCore.QRect(430, 40, 211, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Debugging_screen.setFont(font)
        self.Debugging_screen.setObjectName("Debugging_screen")
        self.Stop_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Stop_Btn.setGeometry(QtCore.QRect(455, 360, 150, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Stop_Btn.setFont(font)
        self.Stop_Btn.setObjectName("Stop_Btn")
        self.Undo_Btn = QtWidgets.QPushButton(Debugging_menu_screen)
        self.Undo_Btn.setGeometry(QtCore.QRect(20, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Undo_Btn.setFont(font)
        self.Undo_Btn.setObjectName("Undo_Btn")

        self.retranslateUi(Debugging_menu_screen)
        QtCore.QMetaObject.connectSlotsByName(Debugging_menu_screen)

    def retranslateUi(self, Debugging_menu_screen):
        _translate = QtCore.QCoreApplication.translate
        Debugging_menu_screen.setWindowTitle(_translate("Debugging_menu_screen", "Form"))
        self.Rotate_Btn.setText(_translate("Debugging_menu_screen", "Start drum rotation"))
        self.CSV_Btn.setText(_translate("Debugging_menu_screen", "Start CSV process"))
        self.Lift_Up_Btn.setText(_translate("Debugging_menu_screen", "Start lifting system"))
        self.Load_Btn.setText(_translate("Debugging_menu_screen", "Set drum in load mode"))
        self.Lift_Down_Btn.setText(_translate("Debugging_menu_screen", "Descent of the system"))
        self.Debugging_screen.setText(_translate("Debugging_menu_screen", "Debugging menu"))
        self.Stop_Btn.setText(_translate("Debugging_menu_screen", "Stop process"))
        self.Undo_Btn.setText(_translate("Debugging_menu_screen", "Back"))
