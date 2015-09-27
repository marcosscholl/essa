import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from data import *
from aware import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import threading 
lock =  threading.RLock()
 
class Dialog(Listener, QtGui.QDialog):
 
    def __init__(self, parent=None):
         QtGui.QDialog.__init__(self, parent)
         Listener.__init__(self)
         global lock
         self.resize(300,200)
         self.setObjectName(u"Atencao22")
         self.resize(370, 411)
         self.setWindowTitle("Dialog")
         self.label = QtGui.QLabel(self)
         self.label.setGeometry(QtCore.QRect(0, 20, 371, 20))
         self.label.setAlignment(QtCore.Qt.AlignCenter)
         self.label.setObjectName("label")        
         self.label.setText(u"XXXXX")
         self.pushButton = QtGui.QPushButton(self)
         self.pushButton.setGeometry(QtCore.QRect(120, 350, 131, 41))
         font = QtGui.QFont()
         font.setFamily("Arial")
         font.setPointSize(12)
         font.setBold(False)
         font.setWeight(50)
         self.pushButton.setFont(font)
         self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
         self.pushButton.setObjectName("pushButton")
         self.pushButton.setText("Ciente")
         self.label_2 = QtGui.QLabel(self)
         self.label_2.setGeometry(QtCore.QRect(0, 60, 371, 271))
         self.label_2.setPixmap(QtGui.QPixmap("/home/scholl/Dropbox/Spyder/essa/images/alert.png"))
         self.label_2.setAlignment(QtCore.Qt.AlignCenter)
         self.label_2.setObjectName("label_2")
         self.pushButton.clicked.connect(self.buttonPressed)
         
    def showEvent(self, event):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.setGeometry(qr)
        """
        geom = self.frameGeometry()
        geom.moveCenter(QtGui.QCursor.pos())
        self.setGeometry(geom)
        """
        super(Dialog, self).showEvent(event)
  
 
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.hide()
            event.accept()
        else:
            super(Dialog, self).keyPressEvent(event)
                 
    def buttonPressed(self,event):
         print "CLICKADO"  
         self.close()
         self.deleteLater()
         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
         
    def handleButton(self):
         dialog = Dialog(self)
         if dialog.exec_() == QtGui.QDialog.Accepted:
             print('Option one: %s' % dialog.checkbox1.isChecked())
             print('Option two: %s' % dialog.checkbox2.isChecked())
         else:
            print('Cancelled')
         dialog.deleteLaterthreaded()
         
    def process_event(self, event=None, subject=None):
         if (isinstance(event, EventGui)):
             print "Subject:", subject
             
             try:
                 lock.acquire()
                 #self.activateAlarm(subject, subject._id.name,subject.value)
                 print "PRECISA Abrir uma janela"
                 subject.alarmGui.show()
             finally:
                lock.release()
         elif (isinstance(event,EventGuiClose)):
            try:
                lock.acquire()
                #self.activateAlarm(subject, subject._id.name,subject.value)
                print "PRECISA FECHAR uma janela"
                self.buttonPressed()
            finally:
                lock.release()
         else:
            print "OUTRO EVENTO"
 
if __name__ == "__main__":
    app = QtGui.QApplication([])
 
    d = Dialog()
    d.show()
    d.raise_()
    e = Dialog()
    e.show()
    f = Dialog()
    f.show()
    app.exec_()
