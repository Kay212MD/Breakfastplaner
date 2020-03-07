# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frühstücksplaner.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.personlist = QtWidgets.QPushButton(self.centralwidget)
        self.personlist.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.personlist.setObjectName("personlist")
        self.foodlist = QtWidgets.QPushButton(self.centralwidget)
        self.foodlist.setGeometry(QtCore.QRect(170, 10, 151, 23))
        self.foodlist.setObjectName("foodlist")
        self.manage_personlist = QtWidgets.QPushButton(self.centralwidget)
        self.manage_personlist.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.manage_personlist.setObjectName("manage_personlist")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(510, 10, 248, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(620, 600, 156, 23))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.personavailable = QtWidgets.QPushButton(self.centralwidget)
        self.personavailable.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.personavailable.setObjectName("personavailable")
        self.theplan = QtWidgets.QPushButton(self.centralwidget)
        self.theplan.setGeometry(QtCore.QRect(330, 10, 151, 23))
        self.theplan.setObjectName("theplan")
        self.manage_foodlist = QtWidgets.QPushButton(self.centralwidget)
        self.manage_foodlist.setGeometry(QtCore.QRect(170, 40, 151, 23))
        self.manage_foodlist.setObjectName("manage_foodlist")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 741, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.actionNeu = QtWidgets.QAction(MainWindow)
        self.actionNeu.setObjectName("actionNeu")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.menuDatei.addAction(self.actionNeu)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frühstücksplaner"))
        self.personlist.setText(_translate("MainWindow", "Person anlegen"))
        self.foodlist.setText(_translate("MainWindow", "Lebensmittelliste anlegen"))
        self.manage_personlist.setText(_translate("MainWindow", "Personen verwalten"))
        self.personavailable.setText(_translate("MainWindow", "Person anwesend"))
        self.theplan.setText(_translate("MainWindow", "Plan anlegen"))
        self.manage_foodlist.setText(_translate("MainWindow", "Lebensmittelliste verwalten"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionNeu.setText(_translate("MainWindow", "Neu"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
