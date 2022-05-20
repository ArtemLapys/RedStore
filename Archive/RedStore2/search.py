#тут потом вместо * указать, какие классы точно нужны, нет смысла импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5           import QtCore, QtGui, QtWidgets

class Search(QWidget):
  def __init__(self):
    super().__init__()
    self.searchBar = QLineEdit()
    self.searchBar.setGeometry(QtCore.QRect(0, 0, 1280, 44))
    self.searchBar.setStyleSheet("background-color:black")
    l = QVBoxLayout()
    l.addWidget(self.searchBar)
    self.setLayout(l)

  def startEdit(self, text):
    self.searchBar.setText(text)
    self.searchBar.setFocus()