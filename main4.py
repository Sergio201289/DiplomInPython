# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StationButton = QtWidgets.QPushButton(self.centralwidget)
        self.StationButton.setGeometry(QtCore.QRect(60, 200, 111, 41))
        self.StationButton.setObjectName("StationButton")
        self.EmpoyeesButton = QtWidgets.QPushButton(self.centralwidget)
        self.EmpoyeesButton.setGeometry(QtCore.QRect(250, 200, 111, 41))
        self.EmpoyeesButton.setObjectName("EmpoyeesButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/i (2).jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.StationButton.raise_()
        self.EmpoyeesButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StationButton.setText(_translate("MainWindow", "Станции"))
        self.EmpoyeesButton.setText(_translate("MainWindow", "Работники"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Start()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
