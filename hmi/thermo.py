# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150409-1500"
__status__ = "stable"
__license__ = "GPL"

import sys
from PyQt4 import Qt, QtCore, QtGui
import PyQt4.Qwt5 as Qwt
import PyQt4.Qwt5.anynumpy as np

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

        
class Thermo(Widget, QtGui.QWidget):

    def __init__(self,parent = None):
         Widget.__init__(self)
         QtGui.QWidget.__init__(self,parent)
         self.thermo = Qwt.QwtThermo(self)

         self.font = QtGui.QFont()
         self.font.setPointSize(10)
         self.font.setBold(True)
         self.thermo.setFont(self.font)
         
         self.thermo.setAutoFillBackground(False)
         self.thermo.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
         #self.thermo.setInputMethodHints(QtCore.Qt.ImhNone)
         brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
         brush.setStyle(QtCore.Qt.SolidPattern)
         self.thermo.setAlarmBrush(brush)
         self.thermo.setAlarmColor(QtGui.QColor(255, 0, 0))
         self.thermo.setAlarmEnabled(True)
         self.thermo.setAlarmLevel(80.0)
         self.thermo.setScalePosition(Qwt.QwtThermo.LeftScale)
         self.thermo.setBorderWidth(3)
         brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
         brush.setStyle(QtCore.Qt.SolidPattern)
         self.thermo.setFillBrush(brush)
         self.thermo.setMaxValue(100.0)
         self.thermo.setPipeWidth(20)
         self.thermo.setObjectName("Thermo")
                    
 
         self.lcdNumber = QtGui.QLCDNumber()
         
         self.fontDisplay = QtGui.QFont()
         self.fontDisplay.setPointSize(16)
         self.fontDisplay.setKerning(False)
         self.lcdNumber.setFont(self.fontDisplay)
         self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
         self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
         self.lcdNumber.setSmallDecimalPoint(False)
         self.lcdNumber.setDigitCount(5)
         self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
         self.lcdNumber.setObjectName("lcdNumber")
         self.lcdNumber.setMinimumHeight(45)
         self.lcdNumber.setMinimumWidth(75)
         layout = QtGui.QVBoxLayout(self)
         #layout.setMargin(0)
         #layout.setSpacing(0)
         layout.addWidget(self.thermo,0,QtCore.Qt.AlignHCenter)
         layout.addWidget(self.lcdNumber)
         
         
    def getName(self):
        return self.thermo.objectName()
    
    def setName(self,name):
        self.thermo.setObjectName(name)
        
    Name = QtCore.pyqtProperty(str,fget=getName,fset=setName)    
    
    def setAlarmLevel(self,value):
        self.thermo.setAlarmLevel(value) 
        
    def getAlarmLevel(self):
        return self.thermo.alarmLevel
    AlarmLevel = QtCore.pyqtProperty(float,fget=getAlarmLevel,fset=setAlarmLevel) 
    
    def setValue(self, value):               
        if (value < 40):
            brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.thermo.setFillBrush(brush)
        self.thermo.setValue(value)
        self.lcdNumber.display(str(value))
        
        
            
        
    def setMinValue(self,minValue):
        self.thermo.setMinValue(minValue)
        
        
    def getMinValue(self):
        return self.thermo.minimumSize
    MinimumValue = QtCore.pyqtProperty(float,fget=getMinValue,fset=setMinValue)     
        
    def setMaxValue(self,maxValue):
        self.thermo.setMaxValue(maxValue)
        
    def getMaxValue(self):
        return self.thermo.maximumSize
    MaximumValue = QtCore.pyqtProperty(float,fget=getMaxValue,fset=setMaxValue)  
    
    def setRange(self,minValue,maxValue):
        self.thermo.setRange(minValue,maxValue)
        
        
    def setThermoGeometry(self,left, top, width, height):
        self.thermo.setGeometry(QtCore.QRect(left, top, width, height))
        
    
    def setDysplayGeometry(self,left, top, width, height):
        self.lcdNumber.setGeometry(QtCore.QRect(left, top, width, height))
        
        
    def setFonteThermo(self,pointSize=10,bold=True):
        self.font.setPointSize(pointSize)
        self.font.setBold(bold)
        self.thermo.setFont(self.font) 
        
        
    def setLarguraThermo(self, largura):
        self.thermo.setPipeWidth(largura)
        
    def setThermoFontZize(self, value):
        self.thermo.setPipeWidth(value)
    @property
    def value(self):
        self.thermo.value()
    
    @value.setter
    def value(self, value):
        self.setValue(float(value)) 
        
        
    def getValue(self):
        return self.thermo.value
    Value = QtCore.pyqtProperty(float,fget=getValue,fset=setValue) 

"""        
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
    #window.setAutoFillBackground(False)
    
    #window.setMinimumWidth(150)
    #window.setMinimumHeight(300)
    thermo = Thermo()
    thermo.setValue(89.98)
    #thermo.setLargura(80)
    #thermo.setGeometry(10,10,60,350)
    thermo.show()
    
    #thermo.setRange(0,100)
    #thermo.setValue(50)

    sys.exit(app.exec_())
"""