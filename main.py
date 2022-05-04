import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class umpalumpa():
    o = "O"
    x = "X"
    w = [["O", "O", ""], ["O", "", "O"], ["", "O", "O"]]
    l = [["X","X",""],["X","","X"],["","X","X"]]

class Ui_MainWindow(object):
    def xod(self):
        pr = [[lambda: self.pushButton.setText("O"), lambda: self.pushButton_2.setText("O"),
               lambda: self.pushButton_3.setText("O")],
              [lambda: self.pushButton_4.setText("O"), lambda: self.pushButton_5.setText("O"),
               lambda: self.pushButton_6.setText("O")],
              [lambda: self.pushButton_7.setText("O"), lambda: self.pushButton_8.setText("O"),
               lambda: self.pushButton_9.setText("O")],
              [lambda: self.pushButton.setText("O"), lambda: self.pushButton_4.setText("O"),
               lambda: self.pushButton_7.setText("O")],
              [lambda: self.pushButton_2.setText("O"), lambda: self.pushButton_5.setText("O"),
               lambda: self.pushButton_8.setText("O")],
              [lambda: self.pushButton_3.setText("O"), lambda: self.pushButton_6.setText("O"),
               lambda: self.pushButton_9.setText("O")],
              [lambda: self.pushButton.setText("O"), lambda: self.pushButton_5.setText("O"),
               lambda: self.pushButton_9.setText("O")],
              [lambda: self.pushButton_3.setText("O"), lambda: self.pushButton_5.setText("O"),
               lambda: self.pushButton_7.setText("O")]]
        pp = [[self.pushButton.text(), self.pushButton_2.text(), self.pushButton_3.text()],
              [self.pushButton_4.text(), self.pushButton_5.text(), self.pushButton_6.text()],
              [self.pushButton_7.text(), self.pushButton_8.text(), self.pushButton_9.text()],
              [self.pushButton.text(), self.pushButton_4.text(), self.pushButton_7.text()],
              [self.pushButton_2.text(), self.pushButton_5.text(), self.pushButton_8.text()],
              [self.pushButton_3.text(), self.pushButton_6.text(), self.pushButton_9.text()],
              [self.pushButton.text(), self.pushButton_5.text(), self.pushButton_9.text()],
              [self.pushButton_3.text(), self.pushButton_5.text(), self.pushButton_7.text()]]
        r=False
        for i in pp:
            if i in umpalumpa.w:
                pr[pp.index(i)][pp[pp.index(i)].index("")]()
                r = True
                break
        if not r:
            for i in pp:
                if i in umpalumpa.l:
                    pr[pp.index(i)][pp[pp.index(i)].index("")]()
                    r = True
                    break

        if not r:
            def rek():
                z = random.randint(0, 7)
                zz = random.randint(0, 2)
                if pp[z][zz] == "":
                    pr[z][zz]()
                else:
                    rek()
            rek()
    def qqq(self):
        a = [[self.pushButton.text(), self.pushButton_2.text(), self.pushButton_3.text()],
             [self.pushButton_4.text(), self.pushButton_5.text(), self.pushButton_6.text()],
             [self.pushButton_7.text(), self.pushButton_8.text(), self.pushButton_9.text()],
             [self.pushButton.text(), self.pushButton_4.text(), self.pushButton_7.text()],
             [self.pushButton_2.text(), self.pushButton_5.text(), self.pushButton_8.text()],
             [self.pushButton_3.text(), self.pushButton_6.text(), self.pushButton_9.text()],
             [self.pushButton.text(), self.pushButton_5.text(), self.pushButton_9.text()],
             [self.pushButton_3.text(), self.pushButton_5.text(), self.pushButton_7.text()]]
        if ["X", "X", "X"] in a:
            self.label.setText("Выйграл Крестик")
        elif ["O", "O", "O"] in a:
            self.label.setText("Выйграл Нолик")
        else:
            qeqe=0
            for jojo in a:
                if not "" in jojo:
                    qeqe+=1
            if qeqe == 8:
                self.label.setText("Ничья")
    def p(self):
        if self.pushButton.text() == "":
            self.pushButton.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p2(self):
        if self.pushButton_2.text() == "":
            self.pushButton_2.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p3(self):
        if self.pushButton_3.text() == "":
            self.pushButton_3.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p4(self):
        if self.pushButton_4.text() == "":
            self.pushButton_4.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p5(self):
        if self.pushButton_5.text() == "":
            self.pushButton_5.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p6(self):
        if self.pushButton_6.text() == "":
            self.pushButton_6.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p7(self):
        if self.pushButton_7.text() == "":
            self.pushButton_7.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p8(self):
        if self.pushButton_8.text() == "":
            self.pushButton_8.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def p9(self):
        if self.pushButton_9.text() == "":
            self.pushButton_9.setText(umpalumpa.x)
            self.qqq()
            self.xod()
            self.qqq()

    def reranb(self):
        self.xod()
        umpalumpa.x = "X"
        umpalumpa.o = "O"
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.label.setText("Крестики-нолики")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(236, 345)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "color: rgb(85, 170, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 75, 75))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 60, 75, 75))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 196, 75, 75))
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 60, 75, 75))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 75, 75))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 130, 75, 75))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 130, 75, 75))
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 200, 75, 71))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 200, 75, 71))
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.reran = QtWidgets.QPushButton(self.centralwidget)
        self.reran.setGeometry(QtCore.QRect(34, 310, 171, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reran.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        self.pushButton_8.setFont(font)
        self.pushButton_9.setFont(font)
        self.reran.setStyleSheet("color: rgb(170, 85, 0);\n"
                                 "background-color: rgb(100, 25, 15);")
        self.reran.setObjectName("reran")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 2, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.reran.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.pushButton_7.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.p)
        self.pushButton_2.clicked.connect(self.p2)
        self.pushButton_3.clicked.connect(self.p3)
        self.pushButton_4.clicked.connect(self.p4)
        self.pushButton_5.clicked.connect(self.p5)
        self.pushButton_6.clicked.connect(self.p6)
        self.pushButton_7.clicked.connect(self.p7)
        self.pushButton_8.clicked.connect(self.p8)
        self.pushButton_9.clicked.connect(self.p9)
        self.reran.clicked.connect(self.reranb)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reran.setText(_translate("MainWindow", "Играть снова!"))
        self.label.setText(_translate("MainWindow", "Крестики-нолики"))


class Okoshko(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okoshko()
    okno.show()
    sys.exit(app.exec())
