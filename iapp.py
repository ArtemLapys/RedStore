import sys
import os
#тут потом вместо * указать, какие классы точно нужны, нет смысла импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

import fdb
#import sqlite3

MAX_COUNT = 100 #используется только для создания таблицы
WIDTH = 10
HEIGHT = 5
#PAGE_SIZE = WIDTH*HEIGHT

APP_WIDTH = 135
APP_HEIGHT = 135

hostDB = 'localhost'
DB = '/var/REDStore/RedStore.fdb'
userLogin = 'SYSDBA'
userPassword ='000000'



class App(QWidget):
  def __init__(self, text, image=None):   
    super().__init__(None)
    self.setFixedWidth(APP_WIDTH)
    self.setFixedHeight(APP_HEIGHT)
    w1 = QLabel()
    w1.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
    w2 = QLabel(text)
    w2.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    #тут картинку бери на основе image=None
    w2.setWordWrap(True)
    w1.setPixmap(QPixmap(":/mainWindow/imageRedStore/search.png"))
    l = QVBoxLayout()
    l.setContentsMargins(0,0,0,0)
    l.addWidget(w1)
    l.addWidget(w2)
    self.setLayout(l)

class AppTab(QWidget):
  def __init__(self):
    super().__init__(None)
    self.grid = QGridLayout()
    self.scrollBar = QScrollBar()
    self.scrollBar.hide()  
    self.scrollBar.valueChanged.connect(self.setActivePage)
    l = QHBoxLayout()
    l.addLayout(self.grid)
    l.addWidget(self.scrollBar)
    self.setLayout(l)

  def setActivePage(self, line):
    for i in range(self.grid.count()):
      self.grid.itemAt(i).widget().deleteLater()
    apps = self.getApps(line)
    row = 0
    column = 0
    for i in range(len(apps)):
      self.grid.addWidget(App(apps[i]), row, column)
      if column<WIDTH-1:
        column = column + 1
      else:
        column = 0
        row = row + 1

  def wheelEvent(self, event):
      y = event.angleDelta().y()
      value = self.scrollBar.value()
      if y>0:
        self.scrollBar.setValue(value-1)
      if y<0:
        self.scrollBar.setValue(value+1)

  def activated(self):
    self.con = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')
    #self.createTable()
    self.maxCount = self.getMaxCount()
    if (self.maxCount%WIDTH == 0):
      self.scrollBar.setMaximum(self.maxCount//WIDTH - 1)
    else:
      self.scrollBar.setMaximum(self.maxCount//WIDTH-3)
    self.setActivePage(0)
    self.grid.setRowStretch(HEIGHT, 1)
    self.grid.setColumnStretch(WIDTH, 1)

  def deactivated(self):
    self.con.close()

  def getMaxCount(self):
    cur = self.con.cursor()
    cur.execute("SELECT COUNT(*) FROM App")
    return cur.fetchone()[0]

  def getApps(self, line):
    cur = self.con.cursor()
    cur.execute("SELECT Title FROM App WHERE id BETWEEN " +
                str(line*WIDTH)+ " AND " +str(line*WIDTH+HEIGHT*WIDTH-1)+ ";")
    result = []
    for row in cur.fetchall():
      for column in row:
        result.append(column)
    return result


