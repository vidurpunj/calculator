# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 150, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 150, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 190, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 190, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 190, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 230, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 230, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 230, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 230, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(130, 270, 93, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(220, 270, 93, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 270, 93, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(400, 270, 93, 28))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(130, 300, 93, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(220, 300, 93, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(400, 300, 93, 28))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(130, 330, 93, 28))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(400, 330, 93, 28))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(310, 330, 93, 28))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(220, 330, 93, 28))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 100, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(partial(self.update_data, self.pushButton))
        self.pushButton_2.clicked.connect(partial(self.update_data, self.pushButton_2))
        self.pushButton_3.clicked.connect(partial(self.update_data, self.pushButton_3))
        self.pushButton_4.clicked.connect(partial(self.update_data, self.pushButton_4))
        self.pushButton_5.clicked.connect(partial(self.update_data, self.pushButton_5))
        self.pushButton_6.clicked.connect(partial(self.update_data, self.pushButton_6))
        self.pushButton_7.clicked.connect(partial(self.update_data, self.pushButton_7))
        self.pushButton_8.clicked.connect(partial(self.update_data, self.pushButton_8))
        self.pushButton_9.clicked.connect(partial(self.update_data, self.pushButton_9))
        self.pushButton_10.clicked.connect(partial(self.update_data, self.pushButton_10))
        self.pushButton_11.clicked.connect(partial(self.update_data, self.pushButton_11))
        self.pushButton_12.clicked.connect(partial(self.update_data, self.pushButton_12))
        self.pushButton_13.clicked.connect(partial(self.update_data, self.pushButton_13))
        self.pushButton_14.clicked.connect(partial(self.update_data, self.pushButton_14))
        self.pushButton_15.clicked.connect(partial(self.update_data, self.pushButton_15))
        self.pushButton_16.clicked.connect(partial(self.update_data, self.pushButton_16))
        self.pushButton_17.clicked.connect(partial(self.update_data, self.pushButton_17))
        self.pushButton_18.clicked.connect(partial(self.update_data, self.pushButton_18))
        self.pushButton_19.clicked.connect(partial(self.update_data, self.pushButton_19))
        self.pushButton_20.clicked.connect(partial(self.update_data, self.pushButton_20))
        self.pushButton_21.clicked.connect(partial(self.update_data, self.pushButton_21))
        self.pushButton_22.clicked.connect(partial(self.update_data, self.pushButton_22))
        self.pushButton_23.clicked.connect(partial(self.update_data, self.pushButton_23))
        self.pushButton_25.clicked.connect(partial(self.update_data, self.pushButton_25))

    def update_data(self, button):
        print("Update label")
        text = button.text()
        print(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "%"))
        self.pushButton_2.setText(_translate("MainWindow", "CE"))
        self.pushButton_3.setText(_translate("MainWindow", "C"))
        self.pushButton_4.setText(_translate("MainWindow", "x"))
        self.pushButton_5.setText(_translate("MainWindow", "1/x"))
        self.pushButton_6.setText(_translate("MainWindow", "x2"))
        self.pushButton_7.setText(_translate("MainWindow", "2/x"))
        self.pushButton_8.setText(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_11.setText(_translate("MainWindow", "9"))
        self.pushButton_12.setText(_translate("MainWindow", "x"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_15.setText(_translate("MainWindow", "6"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "1"))
        self.pushButton_18.setText(_translate("MainWindow", "2"))
        self.pushButton_19.setText(_translate("MainWindow", "3"))
        self.pushButton_20.setText(_translate("MainWindow", "+"))
        self.pushButton_21.setText(_translate("MainWindow", "+/-"))
        self.pushButton_22.setText(_translate("MainWindow", "="))
        self.pushButton_23.setText(_translate("MainWindow", "."))
        self.pushButton_25.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
