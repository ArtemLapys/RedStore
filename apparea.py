import fdb

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QScrollBar, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore    import Qt, pyqtSignal, QObject
from PyQt5.QtGui     import QPixmap


#дефолтные размеры иконки
APP_WIDTH = 120
APP_HEIGHT = 130

class App(QWidget):
  clicked = pyqtSignal()

  def __init__(self, text, image, index):
    super().__init__(None)
    self.index = index
    self.setFixedWidth(APP_WIDTH)
    self.setFixedHeight(APP_HEIGHT)
    w1 = QLabel()
    w1.setStyleSheet("border-radius: 20px;\n")
    w1.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
    self.w2 = QLabel(text)
    self.w2.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    self.w2.setWordWrap(True)
    pixmap = QPixmap()
    if isinstance(image,fdb.BlobReader):
      image = image.read()
    if not isinstance(image, QPixmap):
      w1.setPixmap(pixmap)
      pixmap.loadFromData(image)
      pixmap = pixmap.scaled(85,85, Qt.KeepAspectRatio)
      w1.setPixmap(pixmap)
    else:
      w1.setPixmap(image)
    # if isinstance(image,fdb.BlobReader):
    #   image = image.read()
    # w1.setPixmap(pixmap)
    # pixmap.loadFromData(image)
    # pixmap = pixmap.scaled(85,85, Qt.KeepAspectRatio)
    # w1.setPixmap(pixmap)
    l = QVBoxLayout()
    l.setContentsMargins(0,0,0,0)
    l.addWidget(w1)
    l.addWidget(self.w2)
    self.setLayout(l)

  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.clicked.emit()

class Categories(QWidget):
  clicked = pyqtSignal()
  def __init__(self, image, index):
    super().__init__(None)
    self.index = index
    self.setFixedWidth(377)
    self.setFixedHeight(217)
    w1 = QLabel()
    w1.setStyleSheet("border: 1px solid #000000;\nborder-radius: 20px;\n")
    w1.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
    #w1.setPixmap(QPixmap(":/mainWindow/imageRedStore/search.png"))
    pixmap = QPixmap()
    if isinstance(image,fdb.BlobReader):
      image = image.read()
    if not isinstance(image, QPixmap):
      w1.setPixmap(pixmap)
      pixmap.loadFromData(image)
      pixmap = pixmap.scaled(377,217, Qt.KeepAspectRatio)
      w1.setPixmap(pixmap)
    else:
      w1.setPixmap(image)
    l = QVBoxLayout()
    l.setContentsMargins(0,0,0,0)
    l.addWidget(w1)
    self.setLayout(l)
  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.clicked.emit()
#==============================================================
class AppArea(QWidget):
  appClicked = pyqtSignal(int)
  def __init__(self):
    super().__init__(None)
    self.grid = QGridLayout()
    self.scrollBar = QScrollBar()
    self.scrollBar.hide()
    self.scrollBar.valueChanged.connect(self.setFirstLine)
    l = QHBoxLayout()
    l.addLayout(self.grid)
    l.addWidget(self.scrollBar)
    self.setLayout(l)

  def updateScrollBar(self):
    self.maxCount = self.getMaxCount()
    if (self.maxCount%self.columnCount == 0):
      self.scrollBar.setMaximum(self.maxCount//self.columnCount - 1)
    else:
      self.scrollBar.setMaximum(self.maxCount//self.columnCount)

  def setFirstLine(self, line):
    for i in range(self.grid.count()):
      self.grid.itemAt(i).widget().deleteLater()
    (names, images, indexes) = self.getApps(line)
    row = 0
    column = 0
    for i in range(len(names)):
      app = App(names[i], images[i], indexes[i])
      self.grid.addWidget(app, row, column)
      app.clicked.connect(lambda: self.appClicked.emit(QObject().sender().index))
      if column<self.columnCount-1:
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