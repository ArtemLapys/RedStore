# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setEnabled(True)
        self.header.setGeometry(QtCore.QRect(0, 0, 1280, 44))
        self.header.setStyleSheet("background-color: #E4E4E4;")
        self.header.setObjectName("header")
        self.homeButton = QtWidgets.QLabel(self.header)
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
        self.homeButton.setWordWrap(True)
        self.homeButton.setOpenExternalLinks(False)
        self.homeButton.setObjectName("homeButton")
        self.cEditorialButton = QtWidgets.QLabel(self.header)
        self.cEditorialButton.setGeometry(QtCore.QRect(205, 0, 125, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.cEditorialButton.setFont(font)
        self.cEditorialButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cEditorialButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cEditorialButton.setAutoFillBackground(False)
        self.cEditorialButton.setStyleSheet("color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.cEditorialButton.setAlignment(QtCore.Qt.AlignCenter)
        self.cEditorialButton.setWordWrap(False)
        self.cEditorialButton.setOpenExternalLinks(False)
        self.cEditorialButton.setObjectName("cEditorialButton")
        self.iApplicationButton = QtWidgets.QLabel(self.header)
        self.iApplicationButton.setGeometry(QtCore.QRect(360, 0, 205, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.iApplicationButton.setFont(font)
        self.iApplicationButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.iApplicationButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iApplicationButton.setAutoFillBackground(False)
        self.iApplicationButton.setStyleSheet("color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.iApplicationButton.setAlignment(QtCore.Qt.AlignCenter)
        self.iApplicationButton.setWordWrap(False)
        self.iApplicationButton.setOpenExternalLinks(False)
        self.iApplicationButton.setObjectName("iApplicationButton")
        self.searchButton = QtWidgets.QLabel(self.header)
        self.searchButton.setGeometry(QtCore.QRect(1070, 0, 28, 44))
        self.searchButton.setStyleSheet("color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.searchButton.setText("")
        self.searchButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/search.png"))
        self.searchButton.setObjectName("searchButton")
        self.settingsButton = QtWidgets.QLabel(self.header)
        self.settingsButton.setGeometry(QtCore.QRect(1214, 0, 36, 44))
        self.settingsButton.setText("")
        self.settingsButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/settings.png"))
        self.settingsButton.setObjectName("settingsButton")
        self.supportButton = QtWidgets.QLabel(self.header)
        self.supportButton.setGeometry(QtCore.QRect(1171, 0, 28, 44))
        self.supportButton.setStyleSheet("")
        self.supportButton.setText("")
        self.supportButton.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/support.png"))
        self.supportButton.setObjectName("supportButton")
        self.searchTextLabel = QtWidgets.QLabel(self.header)
        self.searchTextLabel.setGeometry(QtCore.QRect(1090, 0, 61, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.searchTextLabel.setFont(font)
        self.searchTextLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.searchTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchTextLabel.setAutoFillBackground(False)
        self.searchTextLabel.setStyleSheet("color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.searchTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchTextLabel.setWordWrap(False)
        self.searchTextLabel.setOpenExternalLinks(False)
        self.searchTextLabel.setObjectName("searchTextLabel")
        self.searchTextLabel.raise_()
        self.homeButton.raise_()
        self.cEditorialButton.raise_()
        self.iApplicationButton.raise_()
        self.searchButton.raise_()
        self.settingsButton.raise_()
        self.supportButton.raise_()
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
        self.progressBar.setProperty("value", 0)
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
        self.textInstallorDeleteLabel.setObjectName("textInstallorDeleteLabel")
        self.progressTextLabel = QtWidgets.QLabel(self.installationFooter)
        self.progressTextLabel.setGeometry(QtCore.QRect(0, 21, 1280, 18))
        self.progressTextLabel.setStyleSheet("color:black;\n"
"background-color:transparent;\n"
"")
        self.progressTextLabel.setScaledContents(False)
        self.progressTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressTextLabel.setObjectName("progressTextLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 1281, 631))
        self.tabWidget.setMinimumSize(QtCore.QSize(1281, 0))
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
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "")
        self.PageIApp = QtWidgets.QWidget()
        self.PageIApp.setObjectName("PageIApp")
        self.iconPageIApp_Label = QtWidgets.QLabel(self.PageIApp)
        self.iconPageIApp_Label.setGeometry(QtCore.QRect(60, 20, 125, 125))
        self.iconPageIApp_Label.setText("")
        self.iconPageIApp_Label.setPixmap(QtGui.QPixmap(":/mainWindow/imageRedStore/obs.png"))
        self.iconPageIApp_Label.setObjectName("iconPageIApp_Label")
        self.installButtonPageIApp_Label = QtWidgets.QLabel(self.PageIApp)
        self.installButtonPageIApp_Label.setGeometry(QtCore.QRect(1003, 30, 219, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.installButtonPageIApp_Label.setFont(font)
        self.installButtonPageIApp_Label.setAutoFillBackground(False)
        self.installButtonPageIApp_Label.setStyleSheet("color: white;\n"
"border-radius:20px;\n"
"background-color:#E44641;\n"
"\n"
"")
        self.installButtonPageIApp_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.installButtonPageIApp_Label.setObjectName("installButtonPageIApp_Label")
        self.nameAppPageIApp_Label = QtWidgets.QLabel(self.PageIApp)
        self.nameAppPageIApp_Label.setGeometry(QtCore.QRect(196, 30, 793, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nameAppPageIApp_Label.setFont(font)
        self.nameAppPageIApp_Label.setStyleSheet("color: black;\n"
"background:transparent;\n"
"")
        self.nameAppPageIApp_Label.setObjectName("nameAppPageIApp_Label")
        self.nameOrgAppPageIApp_Label = QtWidgets.QLabel(self.PageIApp)
        self.nameOrgAppPageIApp_Label.setGeometry(QtCore.QRect(200, 60, 781, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameOrgAppPageIApp_Label.setFont(font)
        self.nameOrgAppPageIApp_Label.setStyleSheet("color: black;\n"
"background:transparent;\n"
"")
        self.nameOrgAppPageIApp_Label.setObjectName("nameOrgAppPageIApp_Label")
        self.miniDiscrAppPageIApp_Lapes = QtWidgets.QLabel(self.PageIApp)
        self.miniDiscrAppPageIApp_Lapes.setGeometry(QtCore.QRect(200, 80, 1011, 51))
        self.miniDiscrAppPageIApp_Lapes.setStyleSheet("color: black;\n"
"background:transparent;\n"
"")
        self.miniDiscrAppPageIApp_Lapes.setObjectName("miniDiscrAppPageIApp_Lapes")
        self.descriptionAppPageIApp_Lapes = QtWidgets.QLabel(self.PageIApp)
        self.descriptionAppPageIApp_Lapes.setGeometry(QtCore.QRect(60, 160, 1161, 481))
        self.descriptionAppPageIApp_Lapes.setStyleSheet("color: black;\n"
"background:transparent;\n"
"")
        self.descriptionAppPageIApp_Lapes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionAppPageIApp_Lapes.setWordWrap(True)
        self.descriptionAppPageIApp_Lapes.setObjectName("descriptionAppPageIApp_Lapes")
        self.tabWidget.addTab(self.PageIApp, "")
        self.tabWidget.raise_()
        self.header.raise_()
        self.installationFooter.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "Домашняя старница"))
        self.cEditorialButton.setText(_translate("MainWindow", "Выбор редакции"))
        self.iApplicationButton.setText(_translate("MainWindow", "Установленные приложения"))
        self.searchTextLabel.setText(_translate("MainWindow", "Поиск"))
        self.textInstallorDeleteLabel.setText(_translate("MainWindow", "textInstallorDeleteLabel"))
        self.progressTextLabel.setText(_translate("MainWindow", "progressTextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("MainWindow", "home"))
        self.installButtonPageIApp_Label.setText(_translate("MainWindow", "Установить"))
        self.nameAppPageIApp_Label.setText(_translate("MainWindow", "nameAppInstallApp_Label"))
        self.nameOrgAppPageIApp_Label.setText(_translate("MainWindow", "nameOrgApp_Label"))
        self.miniDiscrAppPageIApp_Lapes.setText(_translate("MainWindow", "miniDiscrAppInstallApp_Lapes"))
        self.descriptionAppPageIApp_Lapes.setText(_translate("MainWindow", "descriptionAppInstallApp_Lapes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PageIApp), _translate("MainWindow", "iapp"))
import resources_rc