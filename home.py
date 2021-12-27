from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5 import QtCore, QtGui, QtWidgets
from apparea import App, AppArea, Categories
import fdb

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
    if self.selector == 0:
      cur.execute("SELECT COUNT(*) FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=1")
    elif self.selector == 1:
      cur.execute("SELECT COUNT(*) FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=2")
    elif self.selector == 2:
      cur.execute("SELECT COUNT(*) FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=3")
    else:
      cur.execute("SELECT COUNT(*) FROM APP")
    return cur.fetchone()[0]

  def getApps(self, line):
    cur = self.con.cursor()
    if self.selector == 1:
      cur.execute("SELECT FIRST " + str(self.rowCount*self.columnCount) +
" SKIP " + str(line*self.columnCount) + " Title, Icon, ID FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=1 ORDER BY ID; "
)
    elif self.selector == 2:
      cur.execute("SELECT FIRST " + str(self.rowCount*self.columnCount) +
" SKIP " + str(line*self.columnCount) + " Title, Icon, ID FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=2 ORDER BY ID; "
)
    elif self.selector == 3:
      cur.execute("SELECT FIRST " + str(self.rowCount*self.columnCount) +
" SKIP " + str(line*self.columnCount) + " Title, Icon, ID FROM APP JOIN APP_CATEGORIES ON APP.ID=APP_CATEGORIES.ID_APP WHERE ID_CATEGORIES=3 ORDER BY ID; "
)
    else:
      cur.execute("SELECT FIRST " + str(self.rowCount*self.columnCount) +
" SKIP " + str(line*self.columnCount) + " Title, Icon, ID FROM APP ORDER BY ID; "
)
    appNames = []
    images = []
    indexes = []
    for row in cur.fetchall():
      appNames.append(row[0])
      images.append(row[1])
      indexes.append(int(row[2]))
    return (appNames, images, indexes)


  def getCategories(self, categoriesOne, categoriesTwo, categoriesThree):
    cur = self.con.cursor()
    cur.execute("SELECT ICON_CATEGORIES FROM CATEGORIES ORDER BY ID")
    images = []
    for row in cur.fetchall():
       images.append(row[0])
    for i in range(len(images)):
      if not isinstance(images[i],bytes):
        pixmap = QPixmap()
        images[i] = images[i].read()
        pixmap.loadFromData(images[i])
        pixmap = pixmap.scaled(377,217, QtCore.Qt.KeepAspectRatio)
        images[i] = pixmap
    categoriesOne = images[0] 
    categoriesTwo = images[1]
    categoriesThree = images[2]
    return categoriesOne, categoriesTwo, categoriesThree


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
    png = QFile(":/mainWindow/imageRedStore/search.png")
    if (png.open(QIODevice.ReadOnly)):
      data = png.readAll()
      png.close()

    self.imageSearchLabel = QLabel()
    self.imageSearchLabel.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
    pixmap = QPixmap()
    if isinstance(data,fdb.BlobReader):
      image = data.read()
    if not isinstance(data, QPixmap):
      self.imageSearchLabel.setPixmap(pixmap)
      pixmap.loadFromData(data)
      pixmap = pixmap.scaled(28,28, Qt.KeepAspectRatio)
      self.imageSearchLabel.setPixmap(pixmap)
    else:
      self.imageSearchLabel.setPixmap(data)
      
    categoriesOne = None
    categoriesTwo = None
    categoriesThree = None
    categoriesOne, categoriesTwo, categoriesThree = HomeArea.getCategories(self, categoriesOne, categoriesTwo, categoriesThree)
    self.selector1 = Categories(categoriesOne, 0)
    self.selector2 = Categories(categoriesTwo, 0)
    self.selector3 = Categories(categoriesThree, 0)
    self.searchBar = QLineEdit()
    self.searchBar.setGeometry(50,50,320,200)
    self.searchBar.resize(100,47)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.searchBar.setFont(font)
    self.searchBar.setStyleSheet("color:black; \n border-bottom:1px solid black;")
    self.searchBar.textChanged.connect(self.search)
    self.searchBar.setPlaceholderText("Поиск по приложениям")
    
    self.area = HomeArea(self.con)
    self.selector1.clicked.connect(lambda: self.setSelector(1))
    self.selector2.clicked.connect(lambda: self.setSelector(2))
    self.selector3.clicked.connect(lambda: self.setSelector(3))
    self.area.updated.connect(self.selector1.show)
    self.area.updated.connect(self.selector2.show)
    self.area.updated.connect(self.selector3.show)
    self.area.updated.connect(self.searchBar.show)
    self.area.updated.connect(self.imageSearchLabel.show)
    
    l1 = QVBoxLayout()
    l1.setContentsMargins(0,25,0,0)
    l2 = QHBoxLayout()
    l2.setContentsMargins(0,0,0,0)
    l2.addWidget(self.selector1)
    l2.addWidget(self.selector2)
    l2.addWidget(self.selector3)
    l3 = QHBoxLayout()
    l3.setContentsMargins(208,25,208,25)
    l3.addWidget(self.imageSearchLabel)
    l3.addWidget(self.searchBar)
    l1.addLayout(l2)
    l1.addLayout(l3)
    l1.addWidget(self.area)
    self.setLayout(l1)

  def setSelector(self, index):
    self.area.setSelector(index)
    self.selector1.hide()
    self.selector2.hide()
    self.selector3.hide()
    self.searchBar.hide()
    self.imageSearchLabel.hide()

  def search(self, text):
    self.searchRequested.emit(text)
