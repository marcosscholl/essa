# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:30:18 2015

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#
# Created: Sat Sep 21 07:44:37 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import Qt,QtGui, QtCore
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.Qwt5 import * # module Qwt 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Dial_1(Widget, Qwt.QwtDial):
    def __init__(self, parent=None):
        Widget.__init__(self)
        Qwt.QwtDial.__init__(self,parent)
        #self.qwtDial = QwtDial()
        self.setGeometry(QtCore.QRect(90, 10, 266, 261))
        self.setReadOnly(True)
        self.setLineWidth(5)
        self.setFrameShadow(QwtDial.Sunken)
        self.setMode(QwtDial.RotateNeedle)
        self.setOrigin(90.0)
        self.setWrapping(False)
        self.setObjectName("qwtDial")
        
        
        self._minValue = 0
        self._maxValue = 200
        self._lowerLimit = 0.0
        self._upperLimit =10.0
        self._step = 10.0
        self._labelFix = False
        
        self.setScale(self._lowerLimit,self._upperLimit,self._step)
        self.setRange( self._minValue, self._maxValue)  
        #-- paramétrage initial du QwtDial -- 
        self.setOrigin(90.0) # point de référence du tracé - 0°=3H, 90° = 6H, etc..
        #self.qwtDial.setScaleArc(90.0, 270.0) # angle début / angle fin du tracé par rapport à l'origine
        self.setScaleArc(45.0, 315.0) # angle début / angle fin du tracé par rapport à l'origine
        self.__label = 'km/h'
        self.setScaleOptions(Qwt.QwtDial.ScaleTicks | Qwt.QwtDial.ScaleLabel)
        self.setScaleTicks(0, 4, 8)


        #-- création de l'aiguille et association au QwtDial 
        #QwtDialSimpleNeedle    (       Style   style, bool     hasKnob = true, const QColor &          mid = Qt::gray, const QColor &          base = Qt::darkGray ) 
        aiguille=QwtDialSimpleNeedle(QwtDialSimpleNeedle.Arrow,True,QtGui.QColor(QtCore.Qt.red),QtGui.QColor(QtCore.Qt.blue)) # défini un QwtDialSimpleNeedle = aiguille simple
        # .Arrow = style aiguille "flèche" | .Ray = style simple ligne 
        self.setNeedle(aiguille) # associe l
        #layout = QtGui.QVBoxLayout(self)
        #layout.setMargin(0)
        #layout.setSpacing(0)
        #layout.addWidget(self,0,QtCore.Qt.AlignHCenter)
        
    def drawScaleContents(self, painter, center, radius):
        rect = Qt.QRect(0, 0, 2 * radius, 2 * radius - 10)
        rect.moveCenter(center)
        painter.setPen(self.palette().color(Qt.QPalette.Text))
        painter.setFont(QtGui.QFont('Helvetica', 20))
        painter.drawText(
            rect, Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter, self.__label)
            
            
    
  
    @pyqtSlot(float)    
    def setValue(self, value):
        super(Dial_1, self).setValue(value)
        self.setLabel(str(value))
      
         
    def setRange(self, minValue, maxValue):
         self._minValue = minValue
         self._maxValue = maxValue    
         super(Dial_1, self).setRange(self._minValue,self._maxValue)
         
         
    def setScale(self, lowerLimit, upperLimit, step):
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        self._step = step
        super(Dial_1,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    
    def setLabel(self, text):
        self.__label = text
        self.update()
    def getLabel(self):
        return self.__label
    label = QtCore.pyqtProperty(str, getLabel, setLabel)
    
    def setMinValue(self, minValue):
         self._minValue = minValue
         super(Dial_1, self).setRange(self._minValue,self._maxValue)
    def getMinValue(self):
         return self._minValue
    MinValue = QtCore.pyqtProperty(float, getMinValue, setMinValue)	 
	
    def setMaxValue(self, maxValue):
         self._maxValue = maxValue
         super(Dial_1, self).setRange(self._minValue,self._maxValue)
    def getMaxValue(self):
         return self._maxValue
    MaxValue = QtCore.pyqtProperty(float, getMaxValue, setMaxValue)	   
    
    def setLowerLimit(self, lowerLimit):
        self._lowerLimit = lowerLimit
        super(Dial_1,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getLowerLimit(self):
        return self._lowerLimit
    LowerLimitScale = QtCore.pyqtProperty(float, getLowerLimit, setLowerLimit)
    
    def setUpperLimit(self, upperLimit):
        self._upperLimit = upperLimit
        super(Dial_1,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getUpperLimit(self):
        return self._upperLimit
    UpperLimitScale = QtCore.pyqtProperty(float, getUpperLimit, setUpperLimit)
    
    def setStep(self, step):
        self._step = step
        super(Dial_1,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getStep(self):
        return self._step
    StepScale = QtCore.pyqtProperty(float, getStep, setStep)   
    
    def setName(self, name):
        self.name = name
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
        return super(Dial_1, self).value()
    
    @value.setter
    def value(self, value):
        super(Dial_1, self).setValue(value)
        if self._labelFix == False: self.setLabel(str(value))
        
    def getValue(self):
        return super(Dial_1, self).value()
    Value = QtCore.pyqtProperty(float, getValue, setValue)   

"""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
   
    dial = Dial_1(window)
    #dial.setRange(0,100)
    dial.setValue(50)
   
    
    layout = QtGui.QVBoxLayout()

    layout.addWidget(dial)
    window.setLayout(layout)
    
    window.show()
    
    sys.exit(app.exec_())
"""