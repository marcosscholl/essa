# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:38:06 2015

@author: MarcosScholl
"""
import math
import random
import sys
from PyQt4 import Qt,QtGui, QtCore
import PyQt4.Qwt5 as Qwt
from PyQt4.QtCore import pyqtSlot, pyqtSignal

import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Dial_2(Widget, Qwt.QwtDial):
    def __init__(self, parent=None):
        Widget.__init__(self)
        Qwt.QwtDial.__init__(self,parent)
        self.name = "Dial"
        self.label = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(28)
        #self.label.setFont(font)
        self.__label = 'km/h'
        #self.__label.resize(20)
        self.setWrapping(False)
        self.setReadOnly(True)
        self.setMode(self.RotateNeedle)
        self.setReadOnly(True)
        #self.qwtDial.scaleDraw().setPenWidth(3)
        self.setLineWidth(5)
        #self.setFrameShadow(Qwt.QwtDial.Sunken)
        self.setFrameShadow(self.Sunken)
        #self.setScale(0.0,10.0,20.0)
        self.setRange(0,100)
        self._labelFix = False
        self.setOrigin(90)
        self.setScaleArc(45.0, 315.0)

        self.setNeedle(Qwt.QwtDialSimpleNeedle(
            Qwt.QwtDialSimpleNeedle.Arrow,
            True,
            Qt.QColor(Qt.Qt.red),
            Qt.QColor(Qt.Qt.gray).light(130)))

        self.setScaleOptions(Qwt.QwtDial.ScaleTicks | Qwt.QwtDial.ScaleLabel)
        self.setScaleTicks(0, 4, 8)
        self._minValue = 0
        self._maxValue = 100
        self._lowerLimit = 0.0
        self._upperLimit =10.0
        self._step = 5.0
        self.setScale(self._lowerLimit,self._upperLimit,self._step)

    # __init__()
    def drawScaleContents(self, painter, center, radius):
        rect = Qt.QRect(0, 0, 2 * radius, 2 * radius - 10)
        rect.moveCenter(center)
        painter.setPen(self.palette().color(Qt.QPalette.Text))
        painter.setFont(QtGui.QFont('Helvetica', 20))
        painter.drawText(
            rect, Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter, self.__label)
            
            
    

        
    def setSizeLabel(self, text):
        self.__label
    # setLabel()
     
    @pyqtSlot(float)        
    def setValue(self, value):
        super(Dial_2, self).setValue(value)
        self.setLabel(str(value))
        
         
    def setRange(self, minValue, maxValue):
         self._minValue = minValue
         self._maxValue = maxValue    
         super(Dial_2, self).setRange(self._minValue,self._maxValue)         
         
    def setScale(self, lowerLimit, upperLimit, step):
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        self._step = step
        super(Dial_2,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    

    def setLabel(self, text):
        self.__label = text
        self.update()
    def getLabel(self):
        return self.__label
    label = QtCore.pyqtProperty(str, getLabel, setLabel)
    
    def setMinValue(self, minValue):
         self._minValue = minValue
         super(Dial_2, self).setRange(self._minValue,self._maxValue)
    def getMinValue(self):
         return self._minValue
    MinValue = QtCore.pyqtProperty(float, getMinValue, setMinValue)	 
	
    def setMaxValue(self, maxValue):
         self._maxValue = maxValue
         super(Dial_2, self).setRange(self._minValue,self._maxValue)
    def getMaxValue(self):
         return self._maxValue
    MaxValue = QtCore.pyqtProperty(float, getMaxValue, setMaxValue)	   
    
    def setLowerLimit(self, lowerLimit):
        self._lowerLimit = lowerLimit
        super(Dial_2,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getLowerLimit(self):
        return self._lowerLimit
    LowerLimitScale = QtCore.pyqtProperty(float, getLowerLimit, setLowerLimit)
    
    def setUpperLimit(self, upperLimit):
        self._upperLimit = upperLimit
        super(Dial_2,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getUpperLimit(self):
        return self._upperLimit
    UpperLimitScale = QtCore.pyqtProperty(float, getUpperLimit, setUpperLimit)
    
    def setStep(self, step):
        self._step = step
        super(Dial_2,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getStep(self):
        return self._step
    StepScale = QtCore.pyqtProperty(float, getStep, setStep)   
    
    def setName(self, name):
        self.objectName = name  
    def getName(self):
        return self.objectName
    name = QtCore.pyqtProperty(str, getName, setName) 

    def setLabelFix(self, flag):
        self._labelFix = flag

    def getLabelFix(self):
        return self._labelFix
    LabelFixed = QtCore.pyqtProperty(bool, getLabelFix, setLabelFix) 
       
    @property
    def value(self):
        return super(Dial_2, self).value()
    
    @value.setter
    def value(self, value):
        super(Dial_2, self).setValue(value)
        if self._labelFix == False: self.setLabel(str(value))
        
    def getValue(self):
        return super(Dial_2, self).value()
    Value = QtCore.pyqtProperty(float, getValue, setValue)   

        


"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
   
    dial = Dial_2(window)
    dial.setRange(0,50)
    dial.setMaxValue(100)
    #dial.setStep(10)
    dial.setValue(50)
    dial.setName("Componente DIal")
    layout = QtGui.QVBoxLayout()

    layout.addWidget(dial)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""