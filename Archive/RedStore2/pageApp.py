from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtGui     import QPixmap

#import fdb

#hostDB = 'localhost'
#DB = '/var/REDStore/RedStore.fdb'
#userLogin = 'SYSDBA'
#userPassword ='000000'
#nameAppInstall = "vlc"

class Page(QWidget):
  def __init__(self, con):
    super().__init__()
    self.con = con
    self.image = QLabel()
    self.label = QLabel()
    l = QVBoxLayout()
    l.addWidget(self.image)
    l.addWidget(self.label)
    self.setLayout(l)

#    def activated(self):
#        self.con = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')

#    def deactivated(self):
#     self.con.close()

  def setInformation(self, index):
    cur = self.con.cursor()
    cur.execute("SELECT AppName, Image FROM Apps WHERE Id=" +str(index)+ ";")
    result = cur.fetchone()
    self.label.setText(result[0])
    pixmap = QPixmap()
    pixmap.loadFromData(result[1])
    self.image.setPixmap(pixmap)
#        cur = self.con.cursor()
#        cur.execute('SELECT TITLE, FIRST_NAME, LAST_NAME, MINI_DESCRIPTION, DESCRIPTION FROM APP JOIN AUTHORS ON APP.AUTHOR=AUTHORS.ID WHERE TITLE='' + nameApp + ";"')
#        print(cur.fetchall())


