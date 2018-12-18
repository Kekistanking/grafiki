# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buildgraph = QtWidgets.QPushButton(self.centralwidget)
        self.buildgraph.setGeometry(QtCore.QRect(340, 190, 261, 101))
        self.buildgraph.setObjectName("buildgraph")
        self.bexit = QtWidgets.QPushButton(self.centralwidget)
        self.bexit.setGeometry(QtCore.QRect(340, 320, 261, 101))
        self.bexit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.buildgraph.setText(_translate("MainWindow", "Построить график на плоскости"))
        self.bexit.setText(_translate("MainWindow", "Выйти"))

