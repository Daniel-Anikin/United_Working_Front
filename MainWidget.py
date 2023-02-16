# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Screen(object):
    def setupUi(self, Main_Screen):
        Main_Screen.setObjectName("Main_Screen")
        Main_Screen.resize(1080, 720)
        Main_Screen.setStyleSheet("")
        self.Start_Btn = QtWidgets.QPushButton(Main_Screen)
        self.Start_Btn.setGeometry(QtCore.QRect(465, 320, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Start_Btn.setFont(font)
        self.Start_Btn.setObjectName("Start_Btn")
        self.Debug_Btn = QtWidgets.QPushButton(Main_Screen)
        self.Debug_Btn.setGeometry(QtCore.QRect(465, 520, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Debug_Btn.setFont(font)
        self.Debug_Btn.setObjectName("Debug_Btn")
        self.Infinity_Btn = QtWidgets.QPushButton(Main_Screen)
        self.Infinity_Btn.setGeometry(QtCore.QRect(720, 420, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Infinity_Btn.setFont(font)
        self.Infinity_Btn.setObjectName("Infinity_Btn")
        self.Stop_Btn = QtWidgets.QPushButton(Main_Screen)
        self.Stop_Btn.setGeometry(QtCore.QRect(210, 420, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Stop_Btn.setFont(font)
        self.Stop_Btn.setObjectName("Stop_Btn")
        self.Time_of_drum_rotation = QtWidgets.QLabel(Main_Screen)
        self.Time_of_drum_rotation.setGeometry(QtCore.QRect(170, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_of_drum_rotation.setFont(font)
        self.Time_of_drum_rotation.setObjectName("Time_of_drum_rotation")
        self.Number_of_iterations = QtWidgets.QLabel(Main_Screen)
        self.Number_of_iterations.setGeometry(QtCore.QRect(760, 120, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Number_of_iterations.setFont(font)
        self.Number_of_iterations.setObjectName("Number_of_iterations")
        self.Machine_control_main_screen = QtWidgets.QLabel(Main_Screen)
        self.Machine_control_main_screen.setGeometry(QtCore.QRect(370, 20, 350, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Machine_control_main_screen.setFont(font)
        self.Machine_control_main_screen.setObjectName("Machine_control_main_screen")
        self.Time_of_rotation = QtWidgets.QSlider(Main_Screen)
        self.Time_of_rotation.setGeometry(QtCore.QRect(100, 230, 320, 25))
        self.Time_of_rotation.setMinimum(10)
        self.Time_of_rotation.setMaximum(30)
        self.Time_of_rotation.setOrientation(QtCore.Qt.Horizontal)
        self.Time_of_rotation.setObjectName("Time_of_rotation")
        self.Num_of_iterations = QtWidgets.QSlider(Main_Screen)
        self.Num_of_iterations.setGeometry(QtCore.QRect(660, 230, 320, 25))
        self.Num_of_iterations.setMinimum(1)
        self.Num_of_iterations.setMaximum(10)
        self.Num_of_iterations.setOrientation(QtCore.Qt.Horizontal)
        self.Num_of_iterations.setObjectName("Num_of_iterations")
        self.time_num = QtWidgets.QLCDNumber(Main_Screen)
        self.time_num.setGeometry(QtCore.QRect(220, 170, 101, 51))
        self.time_num.setProperty("intValue", 10)
        self.time_num.setObjectName("time_num")
        self.iter_num = QtWidgets.QLCDNumber(Main_Screen)
        self.iter_num.setGeometry(QtCore.QRect(790, 170, 101, 51))
        self.iter_num.setProperty("intValue", 1)
        self.iter_num.setObjectName("iter_num")

        self.retranslateUi(Main_Screen)
        QtCore.QMetaObject.connectSlotsByName(Main_Screen)

    def retranslateUi(self, Main_Screen):
        _translate = QtCore.QCoreApplication.translate
        Main_Screen.setWindowTitle(_translate("Main_Screen", "Form"))
        self.Start_Btn.setText(_translate("Main_Screen", "Start simple launch"))
        self.Debug_Btn.setText(_translate("Main_Screen", "System debug menu"))
        self.Infinity_Btn.setText(_translate("Main_Screen", "Start infinity launch"))
        self.Stop_Btn.setText(_translate("Main_Screen", "Stop process"))
        self.Time_of_drum_rotation.setText(_translate("Main_Screen", "Time of drum rotation, s"))
        self.Number_of_iterations.setText(_translate("Main_Screen", "Number of iterations"))
        self.Machine_control_main_screen.setText(_translate("Main_Screen", "Machine control main screen"))
