import sys
#тут потом вместо * запиши, какие классы точно нужны, нет смысла импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtSql     import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

MAX_COUNT = 100
WIDTH = 10
HEIGHT = 5
PAGE_SIZE = WIDTH*HEIGHT

def initDb():
  db = QSqlDatabase.addDatabase("QSQLITE");
  db.setDatabaseName(":memory:");
  db.open()
  query = QSqlQuery(db)
  query.exec_("CREATE TABLE Apps ("
              "  Id      INTEGER PRIMARY KEY,"
              "  AppName INTEGER"
              ");")
  for i in range(MAX_COUNT):
    query.exec_("INSERT INTO Apps (id, AppName) VALUES"
                "(" +str(i)+ ", 'App" +str(i)+ "');")

def getApps(page):
  db = QSqlDatabase.database()
  query = QSqlQuery(db)
  query.exec_("SELECT AppName FROM Apps WHERE id BETWEEN " +
              str(page*PAGE_SIZE)+ " AND " +str((page+1)*PAGE_SIZE-1)+ ";")
  result = []
  while query.next():
    result.append(query.record().value(0))
  return result

#это наш кастомный виджет тоже заглушка
class Widget(QLabel):
  def __init__(self, text, image=None):
    super().__init__(None)
    self.setText(text)
    self.setFixedWidth(100)
    self.setFixedHeight(100)

class AppTab(QWidget):
  def __init__(self):
    super().__init__(None)
    self.grid = QGridLayout()
    self.scrollBar = QScrollBar()
    self.scrollBar.setMaximum(MAX_COUNT//PAGE_SIZE)#это надо переделать
    self.scrollBar.valueChanged.connect(self.setActivePage)
    l = QHBoxLayout()
    l.addLayout(self.grid)
    l.addWidget(self.scrollBar)
    self.setActivePage(0)
    self.setLayout(l)
  
  
  def setActivePage(self, page):
    for i in range(self.grid.count()):
      self.grid.itemAt(i).widget().deleteLater()
    apps = getApps(page)
    row = 0
    column = 0
    for i in range(len(apps)):
      self.grid.addWidget(Widget(apps[i]), row, column)
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
###      print(y)