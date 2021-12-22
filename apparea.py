from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QScrollBar, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore    import Qt, pyqtSignal, QObject
from PyQt5.QtGui     import QPixmap

#PAGE_SIZE = WIDTH*HEIGHT
APP_WIDTH = 135
APP_HEIGHT = 135

class App(QWidget):
  clicked = pyqtSignal()
  def __init__(self, text, image):
    super().__init__(None)
    self.setFixedWidth(APP_WIDTH)
    self.setFixedHeight(APP_HEIGHT)
    w1 = QLabel()
    w1.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
    self.w2 = QLabel(text)
    self.w2.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    self.w2.setWordWrap(True)
    pixmap = QPixmap()
    if not isinstance(image,bytes):
      image = image.read()
    pixmap.loadFromData(image)
    pixmap = pixmap.scaled(85,85, QtCore.Qt.KeepAspectRatio)
    w1.setPixmap(pixmap)
    l = QVBoxLayout()
    l.setContentsMargins(0,0,0,0)
    l.addWidget(w1)
    l.addWidget(self.w2)
    self.setLayout(l)
  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      self.clicked.emit()

class AppArea(QWidget):
  appClicked = pyqtSignal(str)
  def __init__(self):
    super().__init__(None)
    self.columnCount = 10
    self.rowCount = 5
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
    (names, images) = self.getApps(line)
    row = 0
    column = 0
    for i in range(len(names)):
      app = App(names[i], images[i])
      self.grid.addWidget(app, row, column)
      app.clicked.connect(lambda: self.appClicked.emit(QObject().sender().w2.text()))
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