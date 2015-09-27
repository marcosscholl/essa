# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Mon Jun  8 02:48:57 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from data import *
from aware import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import threading 
lock =  threading.RLock()
def threaded(fn):
    def wrapper(*args, **kwargs):
        
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper
    
   
class PopUpAlarm(Listener, QDialog):
    
    def __init__(self):
        Listener.__init__(self)
        QDialog.__init__(self)
        global lock
        self.setObjectName(u"Atenção22")
        self.resize(370, 411)
        self.setWindowTitle("Dialog")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 20, 371, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")        
        self.label.setText(u"ATENÇÃO22")
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
        self.pushButton.clicked.connect(self.retornButton)
        self.clicked = False
    
    def retornButton(self):
        self.clicked = True
        return self.close() and True
        
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventGui)):
            print "sUBJECT:", subject
            print "Gui:", subject.alarmGui
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
                subject.alarmGui.close()
            finally:
                lock.release()
        else:
            print "OUTRO EVENTO"
            
            
def bota():            
    a = PopUpAlarm()
    return a
#import imagem_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #Dialog = QtGui.QDialog()
    

    a = bota()
    a.show()
    
    
    app.exec_()

