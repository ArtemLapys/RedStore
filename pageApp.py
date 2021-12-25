from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtGui     import QPixmap



class Page(QWidget):
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.image = QLabel()
    self.label = QLabel()
    self.button = QPushButton()
    l = QVBoxLayout()
    l.addWidget(self.image)
    l.addWidget(self.label)
    l.addWidget(self.button)
    self.setLayout(l)



  def setInformation(self, index):
    cur = self.con.cursor()
    cur.execute("SELECT Title, Icon, INSTALL_PACK  FROM App WHERE Id=" +str(index)+ ";")
    result = cur.fetchone()
    self.label.setText(result[0])
    pixmap = QPixmap()
    pixmap.loadFromData(result[1])
    self.image.setPixmap(pixmap)
    self.button.setText(result[2])




