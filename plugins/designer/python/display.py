# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created: Thu May 07 00:31:00 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

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
"""
class Scoreboard(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
"""        
class Display(Widget,QtGui.QLabel):
    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QLabel.__init__(self,parent)
        self.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.setFont(self.font)
        self.setTextFormat(QtCore.Qt.PlainText)
        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setIndent(0)
        self.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.setObjectName("label")
        self._staticText = ""
        self._text = ""
        self.value = "Display"
         
    @property
    def value(self):
        return self._text
        
        
    @value.setter
    def value(self, text):
        self._text =  str(text)
        self.setText(self._staticText + self._text)
        #print "-> ",self._staticText + self._text        
        self.notify(EventUpdated(self))
    
    """    
    def value(self, text):
        self.setText(str(text))  
    """    
    def setValue(self, text):
        self.value = (str(text))
    def getValue(self):
        return self._text
    TextValue = QtCore.pyqtProperty(str,fget=getValue,fset=setValue)
    
    @property
    def staticText(self):
        return self._staticText
    
    @staticText.setter
    def staticText(self, text):
        self._staticText = str(text)
        
    def setStaticText(self,text):
        self.staticText = (text)
    def getStaticText(self):
        return self._staticText
    TextStatic = QtCore.pyqtProperty(str,fget=getStaticText,fset=setStaticText)   
"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    display = Display()
    display.value = ("DISPLAY")
    print display.value
    
    
    layout.addWidget(display)
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""