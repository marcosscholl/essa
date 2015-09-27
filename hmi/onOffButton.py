# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150624-2200"
__status__ = "stable"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image

    
class Widget(Subject, Listener):
    def __init__ (self):
        Subject.__init__(self)
        Listener.__init__(self)
        pass

class OnOffButton(Widget, QtGui.QPushButton):
    def __init__(self, parent = None):
        Widget.__init__(self)
        QtGui.QPushButton.__init__(self,parent)
        self.setGeometry(QtCore.QRect(0, 0, 51, 23))
        self.setToolTip("")
        self.setStatusTip("")
        self.setWhatsThis("")
        self.setShortcut("")
        self.setAutoRepeat(False)
        self.setAutoExclusive(False)
        self.setAutoDefault(False)
        self.setDefault(False)
        self.setFlat(False)
        self.setObjectName("OnOffButton")
        self.buttonActivated = False
        self.setText("On")
        self._state = True
        self._enable = True
        self._textTrue = "On"
        self._textFalse = "Off"
        self._imageTrue = None
        self._imageFalse = None
        #self.clicked.connect(self.toggleLED(self))
        self.connect(self, SIGNAL('clicked()'), self.changeState)
        #self.connect(self, SIGNAL('clicked()'), self.changePicture)
        #self.name = name
    
    @property
    def name(self):
        return self.objectName
        
    @name.setter
    def name(self,name):
        #self.name = name
        self.setObjectName(name)
    def setName(self,name):
        self.name = name
        self.objectName = nome     
        
    def getName(self):
        return self.objectName()    
    
    def geometry(self, x, y, width, heigth):
        self.setGeometry(QtCore.QRect( x, y, width, heigth))
        
    def changeState(self):
        
        if self.buttonActivated == True:
            self.setText(self.textTrue)
            self.buttonActivated = False
            if self._imageTrue is not None: self.imageTrue()
        else:
            self.setText(self.textFalse)
            self.buttonActivated = True      
            if self._imageFalse is not None: self.imageFalse()
        self.notify(EventChanged(self))
        self.actionOnChangeState()
                 
    def actionOnChangeState(self):
        if self.buttonActivated == True:
            self.value = False
        else:
            self.value = True 
        self.notify(EventChanged(self))
    
    def changePicture(self):
         if self.buttonActivated == True:
             if self._imageTrue is not None: 
                 self.imageFalse()
         else:
             if self._imageFalse is not None: 
                 self.imageTrue()
    @property
    def value(self):     
        return self._state
    
    @value.setter
    def value(self, value):        
        self._state = value
        self._enable = self._state
        if value is 0:
            self.buttonActivated = False
            #self.emit(SIGNAL('clicked()'))
            #self.changePicture()
            self.changeState()
            self.notify(EventChanged(self))
        elif value is 1:
            self.buttonActivated = True         
            #self.emit(SIGNAL('clicked()'))
            #self.changePicture()
            self.changeState()
            self.notify(EventChanged(self))
                
    

        
    def setValue(self, value):
        self.value = value
        #self._state = value
        #self._enable = self._state
        
    Value = QtCore.pyqtProperty(bool,fget=value,fset=setValue) 
    
    @property
    def textTrue(self):
        return self._textTrue
    
    @textTrue.setter
    def textTrue(self, text):
        self._textTrue = text
        self.setText(text)
        
        
    def getTextTrue(self):
        return self._textTrue
        
    def setTextTrue(self,txt):
        self.textTrue = (txt)
    TextTrue = QtCore.pyqtProperty(str,fget=getTextTrue,fset=setTextTrue)
    
    
    @property
    def textFalse(self):
        return self._textFalse
    
    @textFalse.setter
    def textFalse(self, text):
        self._textFalse = text 
        
    def setTextFalse(self,txt):
        self.textFalse = (txt)
        
    def getTextFalse(self):
        return self._textFalse
    TextFalse = QtCore.pyqtProperty(str,fget=getTextFalse,fset=setTextFalse) 

    def getImageTrue(self):
        return self._imageTrue
    def setImageTrue(self, img):
        self._imageTrue = img
        self.imageTrue()
        
    PathImageTrue = QtCore.pyqtProperty(str,fget=getImageTrue,fset=setImageTrue)  
    
    def imageTrue(self):
        #self.setStyleSheet("background-image: url("+self._imageTrue+");")
        im = Image.open(self._imageTrue)
        width, height = im.size
        #self.setMinimumHeight(height)
        #self.setMinimumWidth(width)        
        #self.setMaximumHeight(height)
        #self.setMaximumWidth(width)
        ##self.update()
        self.setIcon(QtGui.QIcon(self._imageTrue))
        self.setIconSize(QtCore.QSize(width,height))
        
    def getImageFalse(self):
        return self._imageFalse
    def setImageFalse(self,img):
        self._imageFalse = img
        self.imageFalse()
    PathImageFalse = QtCore.pyqtProperty(str,fget=getImageFalse,fset=setImageFalse)  
    
    def imageFalse(self):
        #self.setStyleSheet("background-image: url("+self._imageFalse+");")      
        
        im = Image.open(self._imageFalse)
        width, height = im.size
        #self.setMinimumHeight(height)
        #self.setMinimumWidth(width)        
        #self.setMaximumHeight(height)
        #self.setMaximumWidth(width)
        self.setIcon(QtGui.QIcon(self._imageFalse))
        self.setIconSize(QtCore.QSize(width,height))
    """
    def process_event(self, event=None, subject=None):
        
        if (isinstance(event, EventWidget)):
            try:
                print "Notificado"
                #lock.acquire()
                if subject.value is not None:
                    #self.value = subject.value
                        print "VALOR=", subject.value
                
            except:
                #lock.release()
                pass
        elif (isinstance(event, EventChanged)):
                 print u"{0} mudou seu nome para {1}.".format(subject, subject.value)
                 if subject.value is 1:
                     print "É TRUE"
                     self.emit(SIGNAL('clicked()'))
                 elif subject.value is 0:
                     print "é false"
                     self.imageFalse()
    
        else:
            #print u"Outro evento aleatório"
            pass
    """
    
"""       
if __name__ == "__main__":
    import sys, time
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    botao = OnOffButton()
    botao.geometry(0, 0, 51, 23)
    botao.value = 1
    botao.setImageFalse('/home/scholl/Dropbox/Spyder/essa/images/closed-2.png')
    botao.setImageTrue('/home/scholl/Dropbox/Spyder/essa/images/opened-2.png')
    
    
    
   
    
    layout.addWidget(botao)
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""