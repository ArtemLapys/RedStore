#тут потом вместо * указать, какие классы точно нужны, нет смысла импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5           import QtCore, QtGui, QtWidgets
from apparea import App, AppArea

COLUMN_COUNT = 10
ROW_COUNT_1 = 2
ROW_COUNT_2 = 5

class HomeArea(AppArea):
  updated = pyqtSignal()
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.updateWidgets()

  def updateWidgets(self):
    self.selector = 0
    self.setSelector(0)
    self.grid.setRowStretch(self.rowCount, 1)
    self.grid.setColumnStretch(self.columnCount, 1)
    self.updated.emit()

  def getMaxCount(self):
    cur = self.con.cursor()
    if self.selector   == 1:
      cur.execute("SELECT COUNT(*) FROM Apps WHERE id between 0 and 20;")
    elif self.selector == 2:
      cur.execute("SELECT COUNT(*) FROM Apps WHERE id between 21 and 50;")
    elif self.selector == 3:
      cur.execute("SELECT COUNT(*) FROM Apps WHERE id between 0 and 50;")
    else:
      cur.execute("SELECT COUNT(*) FROM Apps;")
    return cur.fetchone()[0]

  def getApps(self, line):
    cur = self.con.cursor()
    if self.selector == 1:
      cur.execute("SELECT AppName, Image, Id FROM Apps WHERE id between 0 and 20 ORDER BY Id "
                  "LIMIT " + str(self.rowCount*self.columnCount) + " " +
                  "OFFSET " + str(line*self.columnCount) + ";")
    elif self.selector == 2:
      cur.execute("SELECT AppName, Image, Id FROM Apps WHERE id between 21 and 50 ORDER BY Id "
                  "LIMIT " + str(self.rowCount*self.columnCount) + " " +
                  "OFFSET " + str(line*self.columnCount) + ";")
    elif self.selector == 3:
      cur.execute("SELECT AppName, Image, Id FROM Apps WHERE id between 0 and 50 ORDER BY Id "
                  "LIMIT " + str(self.rowCount*self.columnCount) + " " +
                  "OFFSET " + str(line*self.columnCount) + ";")
    else:
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

  def setSelector(self, selector):
    self.columnCount = COLUMN_COUNT
    if selector == 0:
      self.rowCount = ROW_COUNT_1
    else:
      self.rowCount = ROW_COUNT_2
    self.selector = selector
    self.updateScrollBar()
    self.setFirstLine(0)
#========================================================================
class Home(QWidget):
  searchRequested = pyqtSignal(str)
  def __init__(self, con):
    super().__init__()
    self.con = con
    data = None
    png = QFile(":/mainWindow/imageRedStore/support.png")
    if (png.open(QIODevice.ReadOnly)):
      data = png.readAll()
      png.close()
    self.selector1 = App("выбор 0-20", data, 0)
    self.selector2 = App("выбор 21-50", data, 0)
    self.selector3 = App("выбор 0-50", data, 0)
    self.searchBar = QLineEdit()
    self.searchBar.setGeometry(QtCore.QRect(1008, 270, 867, 47))
    self.searchBar.setText("Поиск по приложениям")
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.searchBar.setFont(font)
    self.searchBar.setStyleSheet("color: rgba(0, 0, 0, 0.8); border-bottom:1px solid black;")
   # self.searchBar.clicked(self.searchBar.setText(""))
    self.searchBar.textChanged.connect(self.search)
    self.area = HomeArea(self.con)
    self.selector1.clicked.connect(lambda: self.setSelector(1))
    self.selector2.clicked.connect(lambda: self.setSelector(2))
    self.selector3.clicked.connect(lambda: self.setSelector(3))
    self.area.updated.connect(self.selector1.show)
    self.area.updated.connect(self.selector2.show)
    self.area.updated.connect(self.selector3.show)
    self.area.updated.connect(self.searchBar.show)
    l1 = QVBoxLayout()
    l1.setContentsMargins(0,0,0,0)
    l2 = QHBoxLayout()
    l2.setContentsMargins(0,0,0,0)
    l2.addWidget(self.selector1)
    l2.addWidget(self.selector2)
    l2.addWidget(self.selector3)
    l1.addLayout(l2)
    l1.addWidget(self.searchBar)
    l1.addWidget(self.area)
    self.setLayout(l1)

  def setSelector(self, index):
    self.area.setSelector(index)
    self.selector1.hide()
    self.selector2.hide()
    self.selector3.hide()
    self.searchBar.hide()


  def search(self, text):
    self.searchRequested.emit(text)
