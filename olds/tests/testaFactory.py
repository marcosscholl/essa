"""
import sys
from PyQt4.QtGui import *

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

app = QApplication(sys.argv)
window = QWidget()
layout = QHBoxLayout(window)

button = PicButton(QPixmap("/home/scholl/Dropbox/Spyder/essa/images/alert.png"))
layout.addWidget(button)

window.show()
sys.exit(app.exec_())
"""
import sys
from PyQt4.QtGui import *
 
app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap("/home/scholl/Dropbox/Spyder/essa/images/alert.png")
print pixmap.size()
label.setPixmap(pixmap)
label.show()
sys.exit(app.exec_())