#-*- coding: utf-8 -*-

#import PyQt5 
#import os
import sys
import asyncio
###import fdb
#import pyautogui
#from time import sleep
#import sqlite3

#from pathlib import Path
#from PySide2.QtGui import QGuiApplication
#from PySide2.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
###from fdb.fbcore import Error

from ui_mainwindow import Ui_MainWindow
#from installApp import Install


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       # self.ui.installationFooter.hide()
       
            




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

