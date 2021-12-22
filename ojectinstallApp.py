# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setFocusPolicy(Qt.WheelFocus)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#F0F0F0;")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setEnabled(True)
        self.header.setGeometry(QRect(0, 0, 1280, 44))
        self.header.setStyleSheet(u"background-color: #E4E4E4;")
        self.homeButton = QLabel(self.header)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(29, 0, 146, 44))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(10)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QCursor(Qt.ArrowCursor))
        self.homeButton.setLayoutDirection(Qt.LeftToRight)
        self.homeButton.setAutoFillBackground(False)
        self.homeButton.setStyleSheet(u"color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.homeButton.setAlignment(Qt.AlignCenter)
        self.homeButton.setWordWrap(True)
        self.homeButton.setOpenExternalLinks(False)
        self.cEditorialButton = QLabel(self.header)
        self.cEditorialButton.setObjectName(u"cEditorialButton")
        self.cEditorialButton.setGeometry(QRect(205, 0, 125, 44))
        self.cEditorialButton.setFont(font)
        self.cEditorialButton.setCursor(QCursor(Qt.ArrowCursor))
        self.cEditorialButton.setLayoutDirection(Qt.LeftToRight)
        self.cEditorialButton.setAutoFillBackground(False)
        self.cEditorialButton.setStyleSheet(u"color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.cEditorialButton.setAlignment(Qt.AlignCenter)
        self.cEditorialButton.setWordWrap(False)
        self.cEditorialButton.setOpenExternalLinks(False)
        self.iApplicationButton = QLabel(self.header)
        self.iApplicationButton.setObjectName(u"iApplicationButton")
        self.iApplicationButton.setGeometry(QRect(360, 0, 205, 44))
        self.iApplicationButton.setFont(font)
        self.iApplicationButton.setCursor(QCursor(Qt.ArrowCursor))
        self.iApplicationButton.setLayoutDirection(Qt.LeftToRight)
        self.iApplicationButton.setAutoFillBackground(False)
        self.iApplicationButton.setStyleSheet(u"color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.iApplicationButton.setAlignment(Qt.AlignCenter)
        self.iApplicationButton.setWordWrap(False)
        self.iApplicationButton.setOpenExternalLinks(False)
        self.searchButton = QLabel(self.header)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1070, 0, 28, 44))
        self.searchButton.setStyleSheet(u"color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.searchButton.setPixmap(QPixmap(u":/mainWindow/imageRedStore/search.png"))
        self.settingsButton = QLabel(self.header)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(1214, 0, 36, 44))
        self.settingsButton.setPixmap(QPixmap(u":/mainWindow/imageRedStore/settings.png"))
        self.supportButton = QLabel(self.header)
        self.supportButton.setObjectName(u"supportButton")
        self.supportButton.setGeometry(QRect(1171, 0, 28, 44))
        self.supportButton.setStyleSheet(u"")
        self.supportButton.setPixmap(QPixmap(u":/mainWindow/imageRedStore/support.png"))
        self.searchTextLabel = QLabel(self.header)
        self.searchTextLabel.setObjectName(u"searchTextLabel")
        self.searchTextLabel.setGeometry(QRect(1090, 0, 61, 44))
        self.searchTextLabel.setFont(font)
        self.searchTextLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.searchTextLabel.setLayoutDirection(Qt.LeftToRight)
        self.searchTextLabel.setAutoFillBackground(False)
        self.searchTextLabel.setStyleSheet(u"color: black;\n"
"border-bottom: 2px solid #E44641;\n"
"")
        self.searchTextLabel.setAlignment(Qt.AlignCenter)
        self.searchTextLabel.setWordWrap(False)
        self.searchTextLabel.setOpenExternalLinks(False)
        self.searchTextLabel.raise_()
        self.homeButton.raise_()
        self.cEditorialButton.raise_()
        self.iApplicationButton.raise_()
        self.searchButton.raise_()
        self.settingsButton.raise_()
        self.supportButton.raise_()
        self.installationFooter = QWidget(self.centralwidget)
        self.installationFooter.setObjectName(u"installationFooter")
        self.installationFooter.setEnabled(False)
        self.installationFooter.setGeometry(QRect(0, 676, 1280, 44))
        self.installationFooter.setStyleSheet(u"background-color: #E4E4E4;")
        self.progressBar = QProgressBar(self.installationFooter)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 0, 1280, 2))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"border-radius:0;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color:#E44641;\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.textInstallorDeleteLabel = QLabel(self.installationFooter)
        self.textInstallorDeleteLabel.setObjectName(u"textInstallorDeleteLabel")
        self.textInstallorDeleteLabel.setGeometry(QRect(0, 6, 1280, 18))
        self.textInstallorDeleteLabel.setStyleSheet(u"color:black;\n"
"")
        self.textInstallorDeleteLabel.setScaledContents(False)
        self.textInstallorDeleteLabel.setAlignment(Qt.AlignCenter)
        self.progressTextLabel = QLabel(self.installationFooter)
        self.progressTextLabel.setObjectName(u"progressTextLabel")
        self.progressTextLabel.setGeometry(QRect(0, 21, 1280, 18))
        self.progressTextLabel.setStyleSheet(u"color:black;\n"
"background-color:transparent;\n"
"")
        self.progressTextLabel.setScaledContents(False)
        self.progressTextLabel.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 40, 1281, 631))
        self.tabWidget.setMinimumSize(QSize(1281, 0))
        self.tabWidget.setStyleSheet(u"border:transparent; \n"
"background-color:#F0F0F0;")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.tabWidget.addTab(self.home, "")
        self.installApp = QWidget()
        self.installApp.setObjectName(u"installApp")
        self.iconInstallApp_Label = QLabel(self.installApp)
        self.iconInstallApp_Label.setObjectName(u"iconInstallApp_Label")
        self.iconInstallApp_Label.setGeometry(QRect(60, 20, 125, 125))
        self.iconInstallApp_Label.setPixmap(QPixmap(u":/mainWindow/imageRedStore/obs.png"))
        self.installButtonInstallApp_Label = QLabel(self.installApp)
        self.installButtonInstallApp_Label.setObjectName(u"installButtonInstallApp_Label")
        self.installButtonInstallApp_Label.setGeometry(QRect(1003, 30, 219, 40))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.installButtonInstallApp_Label.setFont(font1)
        self.installButtonInstallApp_Label.setAutoFillBackground(False)
        self.installButtonInstallApp_Label.setStyleSheet(u"color: white;\n"
"border-radius:20px;\n"
"background-color:#E44641;\n"
"\n"
"")
        self.installButtonInstallApp_Label.setAlignment(Qt.AlignCenter)
        self.nameAppInstallApp_Label = QLabel(self.installApp)
        self.nameAppInstallApp_Label.setObjectName(u"nameAppInstallApp_Label")
        self.nameAppInstallApp_Label.setGeometry(QRect(196, 30, 793, 27))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.nameAppInstallApp_Label.setFont(font2)
        self.nameAppInstallApp_Label.setStyleSheet(u"color: black;\n"
"background:transparent;\n"
"")
        self.nameOrgApp_Label = QLabel(self.installApp)
        self.nameOrgApp_Label.setObjectName(u"nameOrgApp_Label")
        self.nameOrgApp_Label.setGeometry(QRect(200, 60, 781, 25))
        font3 = QFont()
        font3.setPointSize(12)
        self.nameOrgApp_Label.setFont(font3)
        self.nameOrgApp_Label.setStyleSheet(u"color: black;\n"
"background:transparent;\n"
"")
        self.miniDiscrAppInstallApp_Lapes = QLabel(self.installApp)
        self.miniDiscrAppInstallApp_Lapes.setObjectName(u"miniDiscrAppInstallApp_Lapes")
        self.miniDiscrAppInstallApp_Lapes.setGeometry(QRect(200, 80, 1011, 51))
        self.miniDiscrAppInstallApp_Lapes.setStyleSheet(u"color: black;\n"
"background:transparent;\n"
"")
        self.descriptionAppInstallApp_Lapes = QLabel(self.installApp)
        self.descriptionAppInstallApp_Lapes.setObjectName(u"descriptionAppInstallApp_Lapes")
        self.descriptionAppInstallApp_Lapes.setGeometry(QRect(60, 160, 1161, 481))
        self.descriptionAppInstallApp_Lapes.setStyleSheet(u"color: black;\n"
"background:transparent;\n"
"")
        self.descriptionAppInstallApp_Lapes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptionAppInstallApp_Lapes.setWordWrap(True)
        self.tabWidget.addTab(self.installApp, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.header.raise_()
        self.installationFooter.raise_()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0441\u0442\u0430\u0440\u043d\u0438\u0446\u0430", None))
        self.cEditorialButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0434\u0430\u043a\u0446\u0438\u0438", None))
        self.iApplicationButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.searchButton.setText("")
        self.settingsButton.setText("")
        self.supportButton.setText("")
        self.searchTextLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.textInstallorDeleteLabel.setText(QCoreApplication.translate("MainWindow", u"textInstallorDeleteLabel", None))
        self.progressTextLabel.setText(QCoreApplication.translate("MainWindow", u"progressTextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), QCoreApplication.translate("MainWindow", u"home", None))
        self.iconInstallApp_Label.setText("")
        self.installButtonInstallApp_Label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.nameAppInstallApp_Label.setText(QCoreApplication.translate("MainWindow", u"nameAppInstallApp_Label", None))
        self.nameOrgApp_Label.setText(QCoreApplication.translate("MainWindow", u"nameOrgApp_Label", None))
        self.miniDiscrAppInstallApp_Lapes.setText(QCoreApplication.translate("MainWindow", u"miniDiscrAppInstallApp_Lapes", None))
        self.descriptionAppInstallApp_Lapes.setText(QCoreApplication.translate("MainWindow", u"descriptionAppInstallApp_Lapes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.installApp), QCoreApplication.translate("MainWindow", u"iapp", None))
    # retranslateUi

