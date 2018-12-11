# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mygraph.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Graphs(object):
    def setupUi(self, Graphs):
        Graphs.setObjectName("Graphs")
        Graphs.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Graphs)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 581, 411))
        self.graphicsView.setObjectName("graphicsView")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 430, 420, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sin = QtWidgets.QPushButton(self.formLayoutWidget)
        self.sin.setObjectName("sin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sin)
        self.cos = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cos.setObjectName("cos")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cos)
        self.tg = QtWidgets.QPushButton(self.formLayoutWidget)
        self.tg.setObjectName("tg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tg)
        self.P = QtWidgets.QPushButton(self.formLayoutWidget)
        self.P.setObjectName("P")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.P)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(430, 460, 141, 51))
        self.clear.setObjectName("clear")
        self.goback = QtWidgets.QPushButton(self.centralwidget)
        self.goback.setGeometry(QtCore.QRect(710, 520, 75, 23))
        self.goback.setObjectName("goback")
        Graphs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Graphs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Graphs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Graphs)
        self.statusbar.setObjectName("statusbar")
        Graphs.setStatusBar(self.statusbar)

        self.retranslateUi(Graphs)
        QtCore.QMetaObject.connectSlotsByName(Graphs)

    def retranslateUi(self, Graphs):
        _translate = QtCore.QCoreApplication.translate
        Graphs.setWindowTitle(_translate("Graphs", "MainWindow"))
        self.sin.setText(_translate("Graphs", "a*sin(x)+b"))
        self.cos.setText(_translate("Graphs", "a*cos(x)+b"))
        self.tg.setText(_translate("Graphs", "a*tg(x)+b"))
        self.P.setText(_translate("Graphs", "многочлен"))
        self.label.setText(_translate("Graphs", "Задаваемые переменные: a,b"))
        self.label_2.setText(_translate("Graphs", "Задаваемые переменные: a,b"))
        self.label_3.setText(_translate("Graphs", "Задаваемые переменные: a,b"))
        self.label_4.setText(_translate("Graphs", "Задаваемые переменные: коэфициенты при степенях многочлена"))
        self.clear.setText(_translate("Graphs", "Очистить"))
        self.goback.setText(_translate("Graphs", "Назад"))

from pyqtgraph import PlotWidget
