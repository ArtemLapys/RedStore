#-*- coding: utf-8 -*-

import PyQt5 
import os
import sys
import fdb
import pyautogui
from time import sleep
#import sqlite3

#from pathlib import Path
#from PySide2.QtGui import QGuiApplication
#from PySide2.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from fdb.fbcore import Error

from ui_mainwindow import Ui_MainWindow
from installApp import Install

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #tablet
        self.ui.tableWidget.setColumnWidth(0,280)
        self.ui.tableWidget.setColumnWidth(1,300)
        self.ui.tableWidget.setColumnWidth(2,350)
        self.ui.tableWidget.setColumnWidth(3,250)       
        layout = Qt.QHBoxLayout(self)
        table = self.ui.tableWidget
        self.pushButtons = QtWidgets.QPushButton(table)        
        self.pushButtons.setObjectName("Установить")
        table.setCellWidget(0,0,self.pushButtons)
        layout.addWidget(table)

        #tabl



        self.loadTableApp()


    
    
    def loadTableApp(self):
            hostDB = 'localhost'
            DB = '/var/REDStore/RedStore.fdb'
            userLogin = 'SYSDBA'
            userPassword ='000000'
            try:
                connection = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')
                cur = connection.cursor()
                print("Connected to database.")
                
                cur.execute('select TITLE, AUTHOR, INSTALL_PACK from APP')
                resultApp = cur.fetchall()
                
                tableRow = 0
                for row in resultApp:
                    rowPosition = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(rowPosition)

                    print(tableRow)
                    self.ui.tableWidget.setRowCount(tableRow+1)
                    self.ui.tableWidget.setItem(tableRow,0, QtWidgets.QTableWidgetItem(row[0]))
                    self.ui.tableWidget.setItem(tableRow,2, QtWidgets.QTableWidgetItem(row[2]))
                    button = QtWidgets.QPushButton(str("Установить"))
                    button.clicked.connect(lambda ch, btn=button:self.insta())
                    self.ui.tableWidget.setCellWidget(rowPosition,3,button)
                    for r in cur.execute('select FIRST_NAME,LAST_NAME from AUTHORS where ID='+str(row[1])):
                        self.ui.tableWidget.setItem(tableRow,1, QtWidgets.QTableWidgetItem(r[0]+" "+r[1]))
                    tableRow +=1
                cur.close()

          
            except fdb.Error as error:
                print("[Error-#101] - Module \"fdb\" operation error.") 
            finally:
                if connection:
                    connection.close()
            print("Connection with database is closed.")
    
    def insta(self):
        self.ui.textInstallorDeleteLabel.setText("")
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.pos()).row()
            col = self.ui.tableWidget.indexAt(button.pos()).column()-1
            informationDnfApp = self.ui.tableWidget.model().index(row,col).data()
            #print(row,col)
            #info = str(self.ui.tableWidget.model().index(row,self.ui.tableWidget.indexAt(button.pos()).column()-3).data())
            print(informationDnfApp)
            Install(informationDnfApp, self, row, col, button)
            




def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    #engine = QQmlApplicationEngine()
    #engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    #if not engine.rootObjects():
    #    sys.exit(-1)
    #sys.exit(app.exec_())

