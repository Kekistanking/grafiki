import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from MyWindow import Ui_MainWindow
from PyQt5 import QtGui, QtCore
from MyGraph import Ui_Graphs


class SecondWindow(QMainWindow, Ui_Graphs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.build()
        self.window = None

    def build(self):
        self.goback.clicked.connect(self.back)
        self.sin.clicked.connect(self.run_sin)
        self.cos.clicked.connect(self.run_cos)
        self.tg.clicked.connect(self.run_tg)
        self.P.clicked.connect(self.run_p)
        self.clear.clicked.connect(self.clear_graph)

    def back(self):
        self.window = MyWidget()
        self.window.show()
        self.close()

    def run_sin(self):
        pass

    def run_tg(self):
        pass

    def run_cos(self):
        pass

    def run_p(self):
        pass

    def clear_graph(self):
        pass


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        self.setupUi(self)
        self.buildgraph.clicked.connect(self.run)

    def run(self):
        self.secondWin = SecondWindow()
        self.secondWin.show()
        self.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
