# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:36:29 2015

@author: scholl
"""

import sys
from PyQt4 import Qt, QtCore, QtGui
import PyQt4.Qwt5 as Qwt
import PyQt4.Qwt5.anynumpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

        
class ThermoTop(Widget, Qwt.QwtThermo):

    def __init__(self,parent = None):
         Widget.__init__(self)
         Qwt.QwtThermo.__init__(self,parent)

         self.font = QtGui.QFont()
         self.font.setPointSize(10)
         self.font.setBold(True)
         self.setFont(self.font)
         
         self.setAutoFillBackground(False)
         self.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
         #self.setInputMethodHints(QtCore.Qt.ImhNone)
         brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
         brush.setStyle(QtCore.Qt.SolidPattern)
         self.setAlarmBrush(brush)
         self.setAlarmColor(QtGui.QColor(255, 0, 0))
         self.setAlarmEnabled(True)
         self.setAlarmLevel(80.0)
         self.setScalePosition(Qwt.QwtThermo.TopScale)
         self.setBorderWidth(3)
         brush = QtGui.QBrush(QtGui.QColor(0,170,0))
         brush.setStyle(QtCore.Qt.SolidPattern)
         self.setFillBrush(brush)
         self.setMaxValue(100.0)
         self.setPipeWidth(20)
         self.setObjectName("Thermo")
         self.minVal = 0
         self.maxVal = 100
                    
 

         
         
         
    def getName(self):
        return self.objectName
    
    def setName(self,name):
        self.setObjectName(name)
    Name = QtCore.pyqtProperty(str,fget=getName,fset=setName)    
    
    def setAlarmLevelThermo(self,value):
        self.setAlarmLevel(value)     
        
    def getAlarmLevelThermo(self):
        return self.alarmLevel()
    AlarmLevel = QtCore.pyqtProperty(float,fget=getAlarmLevelThermo,fset=setAlarmLevelThermo) 
    
    
    def setValueThermo(self, value):               
        if (value < 40):
            brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.setFillBrush(brush)
        self.setValue(value)
        
            
        
    def setMinValueThermo(self,minValue):
        self.setMinValue(minValue)
        self.minVal = minValue
        
    def getMinValueThermo(self):
        return self.minVal
    MinimumValue = QtCore.pyqtProperty(float,fget=getMinValueThermo,fset=setMinValueThermo)     
        
    def setMaxValueThermo(self,maxValue):
        self.setMaxValue(maxValue)
        self.maxVal = maxValue
        
    def getMaxValueThermo(self):
        return self.maxVal
    MaximumValue = QtCore.pyqtProperty(float,fget=getMaxValueThermo,fset=setMaxValueThermo)  
    
    def setRange(self,minValue,maxValue):
        self.setRange(minValue,maxValue)
        self.minVal = minValue
        self.maxVal = maxValue
        
    def setThermoGeometry(self,left, top, width, height):
        self.setGeometry(QtCore.QRect(left, top, width, height))
    

        
    def setFonteThermo(self,pointSize=10,bold=True):
        self.font.setPointSize(pointSize)
        self.font.setBold(bold)
        self.setFont(self.font) 
        
        
    def setLarguraThermo(self, largura):
        self.setPipeWidth(largura)
        
    def setThermoFontZize(self, value):
        self.setPipeWidth(value)
        
    @property
    def value(self):
        self.value()
    
    @value.setter
    def value(self, value):
        self._v = (float(value)) 
        self.setValueThermo(float(value))
        
    def valueSetter(self,value):
        self._v = (float(value)) 
        self.value = (float(value)) 
        
    def getValue(self):
        return self.value()
    
    
    Value = QtCore.pyqtProperty(float,fget=getValue,fset=valueSetter) 


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
    #window.setAutoFillBackground(False)
    
    #window.setMinimumWidth(150)
    #window.setMinimumHeight(300)
    thermo = ThermoTop()
    thermo.value = 50
    #print thermo.getMaxValueThermo()
    #thermo.setLargura(80)
    #thermo.setGeometry(10,10,60,350)
    thermo.show()
    
    #thermo.setRange(0,100)
    #thermo.setValue(50)

    sys.exit(app.exec_())
