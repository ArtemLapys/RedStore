#тут потом вместо * указать, какие классы точно нужны, нет смысла импортить всё
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

class Search(QWidget):
  def __init__(self):
    super().__init__()
    self.searchBar = QLineEdit()
    l = QVBoxLayout()
    l.addWidget(self.searchBar)
    self.setLayout(l)

  def startEdit(self, text):
    self.searchBar.setText(text)
    self.searchBar.setFocus()