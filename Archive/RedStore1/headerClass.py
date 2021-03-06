#-*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Header(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(int)
    
    def __init__(self, parent, index) :
        super().__init__(parent.ui.header)
        self.index = index
        self.ui = parent.ui


    def clickTabOne(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")

    def clickTabTwo(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")

    def clickTabThree(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")

    def clickTabFour(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")

       # self.ui.searchButton.setText("??????????")
    
    def clickTabFive(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")

    def clickTabSix(self, event):
        self.ui.homeButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.cEditorialButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.iApplicationButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.searchButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.supportButton.setStyleSheet("color:black; border-bottom:0px solid #E44641")
        self.ui.settingsButton.setStyleSheet("color:black; border-bottom:2px solid #E44641")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self.index)

            if self.index == 0:
                self.clickTabOne(event)
            elif self.index == 1:
                self.clickTabTwo(event)
            elif self.index == 2:
                self.clickTabThree(event)
            elif self.index == 3:
                self.clickTabFour(event)
            elif self.index == 4:
                self.clickTabFive(event)
            elif self.index == 5:
                self.clickTabSix(event)
        
            #self.setStyleSheet("color:black; border-bottom:2px solid #E44641")


            