# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Math_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 90, 1001, 551))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(70, 60, 104, 71))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 60, 104, 71))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 60, 104, 71))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(480, 60, 104, 71))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(790, 60, 181, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 180, 101, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 180, 101, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 180, 101, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 280, 101, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 280, 101, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 280, 101, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 380, 101, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 380, 101, 61))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 380, 101, 61))
        self.pushButton_10.setToolTipDuration(0)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 470, 101, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(670, 250, 191, 111))
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(620, 60, 101, 71))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数学游戏"))
        MainWindow.setToolTip(_translate("MainWindow", "确认"))
        self.groupBox.setTitle(_translate("MainWindow", "游戏题目"))
        self.pushButton.setToolTip(_translate("MainWindow", "确认"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "出题"))
        self.pushButton_12.setText(_translate("MainWindow", "出题"))

        self.pushButton_12.clicked.connect(self.math_text)
        self.pushButton_2.clicked.connect(self.one)
        self.pushButton_3.clicked.connect(self.two)
        self.pushButton_4.clicked.connect(self.three)
        self.pushButton_5.clicked.connect(self.four)
        self.pushButton_6.clicked.connect(self.five)
        self.pushButton_7.clicked.connect(self.six)
        self.pushButton_8.clicked.connect(self.seven)
        self.pushButton_9.clicked.connect(self.eight)
        self.pushButton_10.clicked.connect(self.nine)
        self.pushButton_11.clicked.connect(self.zero)
        self.pushButton.clicked.connect(self.passtest)
        self.Qright = QtWidgets.QMessageBox(self)
        self.count = 0
        self.count1 = 0
        self.right_text = 0
        self.wrong_text = 0

    # 出题
    def math_text(self):
        # 出题数超过固定值时，结束游戏
        if self.count > 3:
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_9.setEnabled(False)
            self.pushButton_10.setEnabled(False)
            self.pushButton_11.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.Qright.information(self, '结束', '恭喜，你已完成本次游戏\n答对---{0}\n答错---{1}'.format(self.right_text, self.wrong_text), QtWidgets.QMessageBox.Yes)
        # 开始出题
        elif self.count == 0:
            self.p1 = random.randint(0, 9)
            self.p2 = random.randint(0, 9)
            self.textEdit.setText(str(self.p1))
            if self.p1 >= self.p2:
                self.Add = random.choice(['+', '-'])
                self.textEdit_2.setText(self.Add)
            else:
                self.textEdit_2.setText('+')
            self.textEdit_3.setText(str(self.p2))
            self.textEdit_4.setText('=')
            self.lineEdit.clear()
            self.count += 1
        elif self.count > 0 and self.lineEdit.text() == '':
            if self.textEdit_2.toPlainText() == '+':
                result = self.p1 + self.p2
                self.wrong_text += 1
                self.Qright.information(self, '空题', '你空题了\n本题结果为{0}'.format(result), QtWidgets.QMessageBox.Yes)
            elif self.textEdit_2.toPlainText() == '-':
                result = self.p1 - self.p2
                self.wrong_text += 1
                self.Qright.information(self, '空题', '你空题了\n本题结果为{0}'.format(result), QtWidgets.QMessageBox.Yes)
            self.Qright.close()
            self.p1 = random.randint(0, 9)
            self.p2 = random.randint(0, 9)
            self.textEdit.setText(str(self.p1))
            if self.p1 >= self.p2:
                self.Add = random.choice(['+', '-'])
                self.textEdit_2.setText(self.Add)
            else:
                self.textEdit_2.setText('+')
            self.textEdit_3.setText(str(self.p2))
            self.textEdit_4.setText('=')
            self.lineEdit.clear()
            self.count += 1
            self.count1 = 0
        elif self.count > 0 and self.lineEdit.text() != '':
            self.p1 = random.randint(0, 9)
            self.p2 = random.randint(0, 9)
            self.textEdit.setText(str(self.p1))
            if self.p1 >= self.p2:
                self.Add = random.choice(['+', '-'])
                self.textEdit_2.setText(self.Add)
            else:
                self.textEdit_2.setText('+')
            self.textEdit_3.setText(str(self.p2))
            self.textEdit_4.setText('=')
            self.lineEdit.clear()
            self.count += 1
            self.count1 = 0
        elif self.count > 3:
            pass

    def one(self):
        self.lineEdit.insert('1')

    def two(self):
        self.lineEdit.insert('2')

    def three(self):
        self.lineEdit.insert('3')

    def four(self):
        self.lineEdit.insert('4')

    def five(self):
        self.lineEdit.insert('5')

    def six(self):
        self.lineEdit.insert('6')

    def seven(self):
        self.lineEdit.insert('7')

    def eight(self):
        self.lineEdit.insert('8')

    def nine(self):
        self.lineEdit.insert('9')

    def zero(self):
        self.lineEdit.insert('0')

    # 运行结果
    def passtest(self):
        if self.count1 == 0:
            if self.lineEdit.text() != '' and self.lineEdit.text().isdigit():
                if self.textEdit_2.toPlainText() == '+':
                    result = self.p1 + self.p2
                    if result == int(self.lineEdit.text()):
                        self.right_text += 1
                        self.count1 += 1
                        self.Qright.information(self, 'win', 'GOOD', QtWidgets.QMessageBox.Yes)
                    else:
                        self.wrong_text += 1
                        self.count1 += 1
                        self.Qright.information(self, 'wrong', '正确答案是---{0}'.format(result), QtWidgets.QMessageBox.Yes)
                elif self.textEdit_2.toPlainText() == '-':
                    result = self.p1 - self.p2
                    if result == int(self.lineEdit.text()):
                        self.right_text += 1
                        self.count1 += 1
                        self.Qright.information(self, 'win', 'GOOD', QtWidgets.QMessageBox.Yes)
                    else:
                        self.Qright.information(self, 'wrong', '正确答案是---{0}'.format(result), QtWidgets.QMessageBox.Yes)
                        self.wrong_text += 1
                        self.count1 += 1
                self.Qright.close()
            else:
                self.Qright.information(self, 'wrong', '请输入一个数字结果', QtWidgets.QMessageBox.Yes)
                self.Qright.close()
        else:
            self.Qright.information(self, 'wrong', '请选择出题', QtWidgets.QMessageBox.Yes)
            self.Qright.close()


