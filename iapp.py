# import sys
# import os
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore    import *
#from PyQt5.QtGui     import *
import fdb
from apparea import App, AppArea

hostDB = 'localhost'
DB = '/var/REDStore/RedStore.fdb'
userLogin = 'SYSDBA'
userPassword ='000000'

MAX_COUNT = 100 #это чисто для создания таблицы

class IappTab(AppArea):
  def activated(self):
    self.con = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')
    self.maxCount = self.getMaxCount()
    if (self.maxCount%self.columnCount == 0):
      self.scrollBar.setMaximum(self.maxCount//self.columnCount - 1)
    else:
      self.scrollBar.setMaximum(self.maxCount//self.columnCount)
    self.setActivePage(0)
    self.grid.setRowStretch(self.rowCount, 1)
    self.grid.setColumnStretch(self.columnCount, 1)

  def deactivated(self):
    self.con.close()

  def getMaxCount(self):
    cur = self.con.cursor()
    cur.execute("SELECT COUNT(*) FROM App")
    return cur.fetchone()[0]

  def getApps(self, line):
    cur = self.con.cursor()
    cur.execute("SELECT FIRST " + str(self.rowCount*self.columnCount) +
" SKIP " + str(line*self.columnCount) + " Title, Icon, Id FROM App ORDER BY Id;")
    appNames = []
    images = []
    indexes = []
    for row in cur.fetchall():
      appNames.append(row[0])
      images.append(row[1])
      indexes.append(int(row[2]))
    return (appNames, images, indexes)