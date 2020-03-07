import Breakfastplaner as b
from personlistwindow import Ui_Dialog
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor

conn = sqlite3.connect('Breakfastplan.db')
cur = conn.cursor()

# specify dirver QSQLITE	SQLite version 3 or above
#db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
# set connection Paramters
#db.setDatabaseName('Breakfastplan.db')




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.personlist = QtWidgets.QPushButton(self.centralwidget)
        self.personlist.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.personlist.setObjectName("personlist")
        #self.personlist.clicked.connect(self.show_sql_table)
        self.personlist.clicked.connect(self.openWindow)

        self.foodlist = QtWidgets.QPushButton(self.centralwidget)
        self.foodlist.setGeometry(QtCore.QRect(170, 10, 151, 23))
        self.foodlist.setObjectName("foodlist")
        self.foodlist.clicked.connect(lambda: b.foodlist())

        self.manage_personlist = QtWidgets.QPushButton(self.centralwidget)
        self.manage_personlist.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.manage_personlist.setObjectName("manage_personlist")
        self.manage_personlist.clicked.connect(lambda: b.manage_personlist())

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(510, 10, 248, 183))
        self.calendarWidget.setObjectName("calendarWidget")

        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(600, 230, 156, 23))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.personavailable = QtWidgets.QPushButton(self.centralwidget)
        self.personavailable.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.personavailable.setObjectName("personavailable")
        self.personavailable.clicked.connect(lambda: b.personavailable())

        self.theplan = QtWidgets.QPushButton(self.centralwidget)
        self.theplan.setGeometry(QtCore.QRect(330, 10, 151, 23))
        self.theplan.setObjectName("theplan")
        self.theplan.clicked.connect(lambda: b.theplan())

        self.manage_foodlist = QtWidgets.QPushButton(self.centralwidget)
        self.manage_foodlist.setGeometry(QtCore.QRect(170, 40, 151, 23))
        self.manage_foodlist.setObjectName("manage_foodlist")
        self.manage_foodlist.clicked.connect(lambda: b.manage_foodlist())

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 741, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)

        # self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(20, 210, 741, 351))
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
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

    def show_sql_table(self):
        # conn = sqlite3.connect('Breakfastplan.db')
        query = "SELECT * FROM People"
        result = conn.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()
    # open the Window, important is it is a window or a dialog
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
