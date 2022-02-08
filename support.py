from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5           import QtCore, QtGui
import fdb

class ClickableLabel(QLabel):
  clicked = pyqtSignal()
  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.clicked.emit()
#========================================================
class Item(QWidget):
  def __init__(self, qu, an):
    super().__init__()
    self.qu = ClickableLabel(qu)
    self.an = ClickableLabel(an)
    self.an.setWordWrap(True)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(14)
    self.qu.setFont(font)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(12)
    self.an.setFont(font)
    self.qu.setStyleSheet("background-color:#E4E4E4; border-radius: 20px;")
    self.an.setStyleSheet("background-color:rgba(67%, 67%, 67%, 0.5);")
    self.an.setContentsMargins(5, 0, 5, 0)
    self.qu.setContentsMargins(5, 0, 5, 0)
    l = QVBoxLayout()
    l.setContentsMargins(54,0,54,0)
    l.addWidget(self.qu)
    l.addWidget(self.an)
    self.setLayout(l)
    self.an.hide()
    self.qu.clicked.connect(lambda: self.an.setVisible(not self.an.isVisible()))
    self.an.clicked.connect(self.an.hide)

#========================================================
class ItemList(QWidget):
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.grid = QVBoxLayout()
    self.grid.setContentsMargins(0,0,0,0)
    self.grid.setSpacing(50)
    self.updateList("")
    self.setLayout(self.grid)

  def clearLayout(self):
    for i in range(self.grid.count()):
      self.grid.itemAt(i).widget().deleteLater()

  def updateList(self, text):
    self.clearLayout()
    cur = self.con.cursor()
    cur.execute("SELECT QUSTION, ANSWER FROM QA WHERE UPPER(QUSTION) LIKE UPPER('%" + text + "%');")
    for row in cur.fetchall():
      self.grid.addWidget(Item(row[0], row[1]))
#========================================================
class Support(QScrollArea):
  def __init__(self, con):
    super().__init__()
    w = QWidget()
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

  
   



    searchBar = QLineEdit()
    searchBar.setGeometry(0,0,0,0)
    searchBar.resize(100,47)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    searchBar.setFont(font)
    searchBar.setStyleSheet("color:black; \n border-bottom:1px solid black;")
    searchBar.setPlaceholderText("Поиск по вопросам")
    #searchBar = QLineEdit()
    itemList = ItemList(con)
    ltemp = QHBoxLayout()
    ltemp.setContentsMargins(208,25,208,25)
    ltemp.addWidget(self.imageSearchLabel)
    ltemp.addWidget(searchBar)
    l = QVBoxLayout()
    l.setSpacing(50)
    w.setLayout(l)
    l.addLayout(ltemp)
    l.addWidget(itemList)
    l.addStretch()
    self.setWidget(w)
    self.setWidgetResizable(True)
    searchBar.textChanged.connect(itemList.updateList)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)






