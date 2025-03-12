
from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import decimal


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
        self.max_iter = 100
        self.pushButton.clicked.connect(self.display_gr)
        self.pushButton.clicked.connect(self.show_answers)

    def display_gr(self):
        self.do = True
        self.k = self.spinBox_k.value()
        self.m = self.spinBox_m.value()
        if 0 < self.m < 4 and 0 < self.k < 4:
            x = np.linspace(-5, 5, 1000)
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

    def der1_func(self, x):
        return self.m * 2 * x - self.k * 2.71828 ** x

    def der2_func(self, x):
        return self.m * 2 - self.k * 2.71828 ** x

    def f_iter(self, x):
        return self.k * 2.71828 ** x - self.m * x ** 2 - 3 * x


    def find_interval(self):
        a = -10
        right = 10
        b = -9
        while b != right:
            if self.func(a) * self.func(b) < 0:
                return [a, b]
            a += 0.1
            b += 0.1


    def m_dih(self, a, b):
        while(abs(b - a) > self.eps):
            x = (a + b) / 2
            fx = self.func(x)
            fa = self.func(a)
            if fa * fx > 0:
                a = x
            else:
                b = x
        accur = round(abs(b-a), 6)
        return x, accur

    def m_hor(self, a, b):
        left = a
        right = b
        z = self.func(a)
        t = self.func(b)
        x = left
        while True:
            last = x
            x = left - ((right - left) / (t - z)) * z
            y = self.func(x)
            if y * z < 0:
                right = x
                t = y
            else:
                left = x
                z = y
            if abs(last - x) < self.eps:
                accur = round(abs(last - x), 6)
                return x, accur

    def m_kas(self,a , b):
        left = a
        right = b
        if self.func(left) * self.der2_func(left) > 0:
            x = left
        elif self.func(right) * self.der2_func(right):
            x = right
        else:
            self.err()
            exit(1)
        while True:
            h = self.func(x) / self.der1_func(x)
            x = x - h
            if abs(h) < self.eps:
                accur = round(abs(h), 6)
                return x, accur

    def m_m_kas(self, a, b):
        left = a
        right = b
        previous = float('inf')

        if self.func(left) * self.der2_func(left) > 0:
            x = left
        else:
            x = right

        d = self.der1_func(x)

        while abs(x - previous) > self.eps:
            previous = x
            x -= self.func(x) / d
        accur = round(abs(x - previous), 6)
        return x, accur

    def m_comb(self, a, b):
        left = a
        right = b
        prev = 0

        if self.func(left) * self.der2_func(left) > 0:
            x = left
            y = right
        else:
            x = right
            y = left

        while abs(x - y) > self.eps:
            mx = x - self.func(x) / self.der1_func(x)
            my = y - self.func(y) * (x - y) / (self.func(x) - self.func(y))

            prev = x
            x = mx
            y = my
        ans = float((x + y) / 2)
        accur = round(abs(x - prev), 6)
        return ans, accur

    def m_iter(self, a, b):
        left = a
        right = b
        prev = 0
        x = (left + right) / 2
        m = max([self.func(left), self.func(right), self.func(x)])
        for _ in range(self.max_iter):
            if abs(x - prev) < self.eps:
                accur = round(abs(x - prev), 6)
                return x, accur

            mx = x + self.func(x) / m
            m = max(m, self.func(mx))

            prev = x
            x = mx

    def show_answers(self):
        if self.do:
            _translate = QtCore.QCoreApplication.translate
            left, right = self.find_interval()
            ans, accur = self.m_dih(left, right)
            self.label_2.setText(_translate("MainWindow", f"Дихотомии: {ans}, погр. {accur}"))

            ans, accur = self.m_hor(left, right)
            self.label_3.setText(_translate("MainWindow", f" хорд: {ans}, погр. {accur}"))

            ans, accur = self.m_kas(left, right)
            self.label_4.setText(_translate("MainWindow", f"касательных: {ans}, погр. {accur}"))

            ans, accur = self.m_m_kas(left, right)
            self.label_5.setText(_translate("MainWindow", f"м. касательных: {ans}, погр. {accur}"))

            ans, accur = self.m_comb(left, right)
            self.label_6.setText(_translate("MainWindow", f"комбинированным: {ans}, погр. {accur}"))

            ans, accur = self.m_iter(left, right)
            self.label_7.setText(_translate("MainWindow", f"итерационным: {ans}, погр. {accur}"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
