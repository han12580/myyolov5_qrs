from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from test import Ui_Dialog
import sys
import os


class MainForm(QMainWindow, Ui_Dialog):
    window = []

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

    def new_window(self):
        a = MainForm()
        self.window.append(a)
        a.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())