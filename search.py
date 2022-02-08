from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5           import QtCore, QtGui, QtWidgets
import fdb


#дефолтные размеры виджета приложения
APP_WIDTH = 1070
APP_HEIGHT = 135

class App(QWidget):
  clicked = pyqtSignal()
  def __init__(self, text, image=None, miniDescr = "", index=0):
    super().__init__(None)
    self.index = index
    self.setFixedWidth(APP_WIDTH)
    self.setFixedHeight(APP_HEIGHT)
    w1 = QLabel()
    self.w2 = QLabel(text)
    self.w3 = QLabel(miniDescr)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(14)
    self.w2.setFont(font)
    self.w2.setContentsMargins(0,25,0,0)
    self.w3.setContentsMargins(0,0,115,0)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.w3.setFont(font)
    self.w2.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
    self.w3.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    #self.w2.setWordWrap(True)
    self.w3.setWordWrap(True)
    self.w3.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)

    pixmap = QtGui.QPixmap()
    if isinstance(image,fdb.BlobReader):
      image = image.read()
    if not isinstance(image, QPixmap):
      w1.setPixmap(pixmap)
      pixmap.loadFromData(image)
      pixmap = pixmap.scaled(100,100, Qt.KeepAspectRatio)
      w1.setPixmap(pixmap)
    else:
      w1.setPixmap(image)
    tempL = QVBoxLayout()
    tempL.addWidget(self.w2)
    tempL.addWidget(self.w3)
    tempL.setContentsMargins(2,0,0,0)
    l = QHBoxLayout()
    l.setContentsMargins(0,0,0,0)
    l.addWidget(w1)
    l.addLayout(tempL)
    self.setLayout(l)

  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.clicked.emit()
#==============================================================
class AppArea(QScrollArea):
  appClicked = pyqtSignal(int)
  def __init__(self, con):
    super().__init__(None)
    self.con = con
    w2 = QWidget()
    self.grid = QVBoxLayout()
    self.grid.setContentsMargins(0,0,0,0)
    w2.setLayout(self.grid)
    w1 = QWidget()
    l1 = QVBoxLayout()
    l1.setContentsMargins(0,0,0,0)
    l1.addWidget(w2)
    l1.addStretch()
    w1.setLayout(l1)
    self.setWidget(w1)
    self.setWidgetResizable(True)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

  def clearLayout(self):
    for i in range(self.grid.count()):
      self.grid.itemAt(i).widget().deleteLater()

  def updateApps(self, text):
    self.clearLayout()
    (names, images, miniDescr, indexes) = self.getApps(text)
    for i in range(len(names)):
      app = App(names[i], images[i], miniDescr[i], indexes[i])
      self.grid.addWidget(app)
      app.clicked.connect(lambda: self.appClicked.emit(QObject().sender().index))

  def getApps(self, name):
    cur = self.con.cursor()
    cur.execute("SELECT Title, Icon, MINI_DESCRIPTION, Id FROM App WHERE UPPER(Title) LIKE UPPER('" + name + "%');")
    appNames = []
    images = []
    miniDescr = []
    indexes = []
    for row in cur.fetchall():
      appNames.append(row[0])
      images.append(row[1])
      miniDescr.append(row[2])
      indexes.append(int(row[3]))
    return (appNames, images, miniDescr, indexes)

#==============================================================
class Search(QWidget):
  def __init__(self, con):
    super().__init__()
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

    self.searchBar = QLineEdit()
    self.searchBar.setGeometry(50,50,320,200)
    self.searchBar.resize(100,47)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.searchBar.setFont(font)
    self.searchBar.setStyleSheet("color:black; \n border-bottom:1px solid black;")
    self.searchBar.setPlaceholderText("Поиск по приложениям")


    self.area = AppArea(con)
    l1 = QHBoxLayout()
    l1.setContentsMargins(208,25,208,25)
    l1.addWidget(self.imageSearchLabel)
    l1.addWidget(self.searchBar)
    l2=QVBoxLayout()
    l2.setContentsMargins(154,0,154,0)
    l2.addWidget(self.area)
    l3 = QVBoxLayout()
    l3.addLayout(l1)
    l3.addLayout(l2)
    self.setLayout(l3)
    self.searchBar.textChanged.connect(self.area.updateApps)

  def startEdit(self, text):
    self.searchBar.setText(text)
    self.searchBar.setFocus()










