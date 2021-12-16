# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/A.Lapys/Документы/RedStore/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from headerClass import Header

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#F0F0F0;")
        self.centralwidget.setObjectName("centralwidget")

        #--------header--------#
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setEnabled(True)
        self.header.setGeometry(QtCore.QRect(0, 0, 1280, 44))
        self.header.setStyleSheet("background-color: #E4E4E4;")
        self.header.setObjectName("header")
        #self.homeButton = QtWidgets.QLabel(self.header)
        self.homeButton = Header(MainWindow, 0)
        self.homeButton.setGeometry(QtCore.QRect(29, 0, 146, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.homeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homeButton.setAutoFillBackground(False)
        self.homeButton.setStyleSheet("color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.homeButton.setAlignment(QtCore.Qt.AlignCenter)
        self.homeButton.setWordWrap(False)
        self.homeButton.setOpenExternalLinks(False)
        self.homeButton.setObjectName("homeButton")
        #self.cEditorialButton = QtWidgets.QLabel(self.header)
        self.cEditorialButton = Header(MainWindow, 1)
        self.cEditorialButton.setGeometry(QtCore.QRect(205, 0, 125, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.cEditorialButton.setFont(font)
        self.cEditorialButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cEditorialButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cEditorialButton.setAutoFillBackground(False)
        self.cEditorialButton.setStyleSheet("color: black;\n"
"border-bottom: 0px solid #E44641;\n"
"")
        self.cEditorialButton.setAlignment(QtCore.Qt.AlignCenter)
        self.cEditorialButton.setWordWrap(False)
        self.cEditorialButton.setOpenExternalLinks(False)
        self.cEditorialButton.setObjectName("cEditorialButton")
        #self.iApplicationButton = QtWidgets.QLabel(self.header)
        self.iApplicationButton = Header(MainWindow, 2)
        self.iApplicationButton.setGeometry(QtCore.QRect(360, 0, 205, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.iApplicationButton.setFont(font)
        self.iApplicationButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.iApplicationButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iApplicationButton.setAutoFillBackground(False)
        self.iApplicationButton.setStyleSheet("color: black;\n"
"border-bottom: 0px solid #E44641;\n"
"")
        self.iApplicationButton.setAlignment(QtCore.Qt.AlignCenter)
        self.iApplicationButton.setWordWrap(False)
        self.iApplicationButton.setOpenExternalLinks(False)
        self.iApplicationButton.setObjectName("iApplicationButton")
        
        self.searchButton = QtWidgets.QLabel(self.header)
        self.searchButton = Header(MainWindow, 3)
        self.searchButton.setGeometry(QtCore.QRect(1123, 0, 28, 44))
        self.searchButton.setText("")
        self.searchButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/search.png"))
        self.searchButton.setObjectName("searchButton")
        
        self.supportButton = QtWidgets.QLabel(self.header)
        self.supportButton = Header(MainWindow, 4)
        self.supportButton.setGeometry(QtCore.QRect(1171, 0, 28, 44))
        self.supportButton.setStyleSheet("")
        self.supportButton.setText("")
        self.supportButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/support.png"))
        self.supportButton.setObjectName("supportButton")
        
        
        self.settingsButton = QtWidgets.QLabel(self.header)
        self.settingsButton = Header(MainWindow, 5)
        self.settingsButton.setGeometry(QtCore.QRect(1214, 0, 36, 44))
        self.settingsButton.setText("")
        self.settingsButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/settings.png"))
        self.settingsButton.setObjectName("settingsButton")


        #--------footer--------#
        self.installationFooter = QtWidgets.QWidget(self.centralwidget)
        self.installationFooter.setEnabled(False)
        self.installationFooter.setGeometry(QtCore.QRect(0, 676, 1280, 44))
        self.installationFooter.setStyleSheet("background-color: #E4E4E4;")
        self.installationFooter.setObjectName("installationFooter")
        self.progressBar = QtWidgets.QProgressBar(self.installationFooter)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 1280, 2))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"border-radius:0;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color:#E44641;\n"
"}\n"
"")
        self.progressBar.setProperty("value", 10)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.textInstallorDeleteLabel = QtWidgets.QLabel(self.installationFooter)
        self.textInstallorDeleteLabel.setGeometry(QtCore.QRect(0, 6, 1280, 18))
        self.textInstallorDeleteLabel.setStyleSheet("color:black;\n"
"")
        self.textInstallorDeleteLabel.setScaledContents(False)
        self.textInstallorDeleteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textInstallorDeleteLabel.setText("mkjhgvbnhjkl")
        self.progressTextLabel = QtWidgets.QLabel(self.installationFooter)
        self.progressTextLabel.setGeometry(QtCore.QRect(0, 21, 1280, 18))
        self.progressTextLabel.setStyleSheet("color:black;\n"
"background-color:transparent;\n"
"")
        self.progressTextLabel.setScaledContents(False)
        self.progressTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressTextLabel.setObjectName("progressTextLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1281, 671))
        #self.tabWidget.setMinimumSize(QtCore.QSize(1281, 0))
        self.tabWidget.setStyleSheet("border:transparent; \n"
"background-color:#F0F0F0;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)



        #main
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "home")

        self.iapp = QtWidgets.QWidget()
        self.iapp.setObjectName("iapp")
        self.tabWidget.addTab(self.iapp, "iapp")

        self.installapp = QtWidgets.QWidget()
        self.installapp.setObjectName("installapp")
        self.tabWidget.addTab(self.installapp, "installapp")

        self.searchapp = QtWidgets.QWidget()
        self.searchapp.setObjectName("searchapp")
        self.tabWidget.addTab(self.searchapp, "searchapp")

        self.support = QtWidgets.QWidget()
        self.support.setObjectName("support")
        self.tabWidget.addTab(self.support, "support")

        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.tabWidget.addTab(self.settings, "settings")
    


        #таблица
        self.tableWidget = QtWidgets.QTableWidget(self.iapp)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 1231, 601))
        self.tableWidget.setStyleSheet("border:2px solid black;\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Название","Автор","Установочный пакет", "Установить"])
        #self.tableWidget.setRowCount(0)


        self.tabWidget.tabBar().hide()
        #qttablet переходит на задний план:
        self.tabWidget.raise_()
        self.header.raise_()
        self.installationFooter.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #------Внесенные изменения------#
        #self.homeButton.clicked = clickTabOne()
        self.homeButton.clicked.connect(self.tabWidget.setCurrentIndex)
        self.cEditorialButton.clicked.connect(self.tabWidget.setCurrentIndex)
        self.iApplicationButton.clicked.connect(self.tabWidget.setCurrentIndex)
        self.searchButton.clicked.connect(self.tabWidget.setCurrentIndex)
        self.supportButton.clicked.connect(self.tabWidget.setCurrentIndex)
        self.settingsButton.clicked.connect(self.tabWidget.setCurrentIndex)
     

        self.pushButton = QtWidgets.QPushButton(self.header)
        self.pushButton.setGeometry(QtCore.QRect(700, 10, 80, 26))
        self.pushButton.setObjectName("pushButton")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "Домашняя страница"))
        self.cEditorialButton.setText(_translate("MainWindow", "Выбор редакции"))
        self.iApplicationButton.setText(_translate("MainWindow", "Установленные приложения"))
        #self.searchButton.setText(_translate("MainWindow", "Поиск приложения"))
        #self.supportButton.setText(_translate("MainWindow", "Поддержка REDStore"))
        #self.settingsButton.setText(_translate("MainWindow", "Настройки REDStore"))
        self.textInstallorDeleteLabel.setText(_translate("MainWindow", "textInstallorDeleteLabel"))
        self.progressTextLabel.setText(_translate("MainWindow", "progressTextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("MainWindow", "home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.iapp), _translate("MainWindow", "iapp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.installapp), _translate("MainWindow", "installapp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchapp), _translate("MainWindow", "searchapp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.support), _translate("MainWindow", "support"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "settings"))

import resources_rc
