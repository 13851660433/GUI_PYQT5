# coding:utf-8
# author = cong

from PyQt5 import QtCore, QtWidgets, QtGui
from Math_game import Ui_MainWindow
import sys


class MainTool(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainTool, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui =MainTool()
    ui.show()
    sys.exit(app.exec_())
