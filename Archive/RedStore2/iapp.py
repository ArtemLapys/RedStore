import sys
import os
#тут потом вместо * указать, какие классы точно нужны, плохо импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from apparea import App, AppArea

COLUMN_COUNT = 10
ROW_COUNT = 5

class IappTab(AppArea):
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.columnCount = COLUMN_COUNT
    self.rowCount = ROW_COUNT
    self.updateScrollBar()
    self.setFirstLine(0)
    self.grid.setRowStretch(self.rowCount, 1)
    self.grid.setColumnStretch(self.columnCount, 1)

  def getMaxCount(self):
    cur = self.con.cursor()
    cur.execute("SELECT COUNT(*) FROM Apps")
    return cur.fetchone()[0]

  def getApps(self, line):
    cur = self.con.cursor()
    cur.execute("SELECT AppName, Image, Id FROM Apps ORDER BY Id "
                "LIMIT " + str(self.rowCount*self.columnCount) + " " +
                "OFFSET " + str(line*self.columnCount) + ";")
    appNames = []
    images = []
    indexes = []
    for row in cur.fetchall():
      appNames.append(row[0])
      images.append(row[1])
      indexes.append(int(row[2]))
    return (appNames, images, indexes)