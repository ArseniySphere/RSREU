import math

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def __init__(self):
        self.do = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 100000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.spinBox_m = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_m.setObjectName("spinBox_m")
        self.horizontalLayout_2.addWidget(self.spinBox_m)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.spinBox_k = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_k.setObjectName("spinBox_k")
        self.horizontalLayout.addWidget(self.spinBox_k)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Code


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Решение уравнения методом"))
        self.label_2.setText(_translate("MainWindow", "Дихотомии:"))
        self.label_5.setText(_translate("MainWindow", "м. касательных:"))
        self.label_3.setText(_translate("MainWindow", " хорд:"))
        self.label_6.setText(_translate("MainWindow", "комбинированным:"))
        self.label_4.setText(_translate("MainWindow", "касательных:"))
        self.label_7.setText(_translate("MainWindow", "итерационным:"))
        self.label_8.setText(_translate("MainWindow", "Уравнение: k * e ** x = m * x ** 2"))
        self.label_10.setText(_translate("MainWindow", "Коэффициент m"))
        self.label_9.setText(_translate("MainWindow", "Коэффициент k"))
        self.pushButton.setText(_translate("MainWindow", "Найти решения"))

        # Code
        self.eps = 1e-4
        self.do = True
        self.pushButton.clicked.connect(self.display_gr)
        self.pushButton.clicked.connect(self.show_answers)

    def display_gr(self):
        self.do = True
        self.k = self.spinBox_k.value()
        self.m = self.spinBox_m.value()
        if self.m and self.k:
            x = np.linspace(-10, 10, 100)
            y = self.m * x ** 2 - self.k * 2.71828 ** x
            plt.plot(x, y)
            plt.title('График функции')
            plt.grid()
            plt.show()
        else:
            self.err()

    def err(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка")
        msg.setInformativeText('Неверно введенные данные')
        msg.setWindowTitle("Ошибка")
        msg.exec_()
        self.do = False

    def func(self, x):
        return self.m * x ** 2 - self.k * 2.71828 ** x

    def m_dih(self, a, b):
        while(abs(b - a) > self.eps):
            x = (a + b) / 2
            fx = self.func(x)
            fa = self.func(a)
            if fa * fx > 0:
                a = x
            else:
                b = x
        return x

    def m_hor(self):


    def show_answers(self):
        if self.do:
            _translate = QtCore.QCoreApplication.translate
            ans = self.m_dih(-3, 0)
            self.label_2.setText(_translate("MainWindow", f"Дихотомии: {ans}"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
