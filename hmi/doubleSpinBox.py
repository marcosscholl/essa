# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:45:35 2015

@author: root
"""

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150405-1500"
__status__ = "stable"
__license__ = "GPL"

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
class DoubleSpinBox(Widget,QtGui.QDoubleSpinBox):
    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QDoubleSpinBox.__init__(self,parent)
        self.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.setGeometry(QtCore.QRect(10, 40, 87, 33))
        self.setObjectName("doubleSpinBox")
        self._value = 0.0
        self.valueChanged.connect(self.valueHandler)

    def valueHandler(self,value):
        self.value = value     
        
    @property
    def value(self):
        return self._value
        
        
    @value.setter
    def value(self, value):
        self._value = value
        self.setValue(value)
        self.notify(EventUpdated(self))
        
    Value = QtCore.pyqtProperty(str,fget=value,fset=value)

    def setName(self, nome):
        self.objectName = nome  
        
    def getName(self):
        return self.objectName()
        
             
"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    display = DoubleSpinBox()
    display.value =  (99.99)
  
    
    layout.addWidget(display)
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())  
"""