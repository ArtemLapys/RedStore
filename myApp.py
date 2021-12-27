import sys
import os
#тут потом вместо * указать, какие классы точно нужны, плохо импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from apparea import App, AppArea

COLUMN_COUNT = 10
ROW_COUNT = 5

class myAppTab(AppArea):
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.columnCount = COLUMN_COUNT
    self.rowCount = ROW_COUNT
    self.updateScrollBar()
    self.setFirstLine(0)
    self.grid.setRowStretch(self.rowCount, 1)
    self.grid.setColumnStretch(self.columnCount, 1)
  def baseLocal():
    result = []
    with open("baseApp.dat", 'r') as file:
        lines = file.readlines()
        for line in lines:
            result += line.split("\n")
    result = list(filter(None, result))
    return result

  def getMaxCount(self):
    result = sum(1 for line in open("baseApp.dat", 'r'))
    return result

  def getApps(self, line):
    myApp = myAppTab.baseLocal()
    appNames = []
    images = []
    indexes = []
    for row in myApp:
        row = row.split(" ")
        temp1 = str(row[0])
        temp2 = str(row[1])
        cur = self.con.cursor()
        cur.execute("SELECT TITLE, ICON, ID FROM APP WHERE ID = " +str(temp1)+" AND LOWER(INSTALL_PACK)= LOWER('"+str(temp2)+"');")

        for row in cur.fetchall():
            appNames.append(row[0])
            images.append(row[1])
            indexes.append(int(row[2]))
    return (appNames, images, indexes)