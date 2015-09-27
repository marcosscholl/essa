# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150328-1900"
__status__ = "stable"
__license__ = "GPL"

from PyQt4 import QtCore, QtGui



import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class DisplayLCD(Widget,QtGui.QLCDNumber):
    def __init__(self, parent = None):
        Widget.__init__(self)
        QtGui.QLCDNumber.__init__(self,parent)
        self.setGeometry(QtCore.QRect(-10, 10, 111, 41))
        self.font = QtGui.QFont()
        self.font.setPointSize(16)
        self.setFont(self.font)
        self.setFrameShape(QtGui.QFrame.NoFrame)
        self.setFrameShadow(QtGui.QFrame.Plain)
        self.setLineWidth(1)
        self.setMidLineWidth(1)
        self.setSmallDecimalPoint(False)
        self.setNumDigits(5)
        self.setSegmentStyle(QtGui.QLCDNumber.Outline)
        self.setProperty("value", 0.0)
        self.setObjectName("lcdNumber")

    def setName(self, nome):
        self.objectName = nome  
        
    def getName(self):
        return self.objectName()
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, text):
        self.setValue(text)
        
        
    def setValue(self, text):
        self.setProperty("value", float(text))
              
    Value = QtCore.pyqtProperty(str,fget=value,fset=setValue)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    display = DisplayLCD()
    display.value =  ("99.99")
  
    
    layout.addWidget(display)
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())


