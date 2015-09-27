# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:03:33 2015

@author: MarcosScholl
"""

import sys
from PyQt4 import Qt,QtGui, QtCore
import PyQt4.Qwt5 as Qwt
from PyQt4.QtCore import pyqtSlot, pyqtSignal


def enumList(enum, sentinel):
    '''
    '''
    return [enum(i) for i in range(sentinel)]

colorGroupList = enumList(
    Qt.QPalette.ColorGroup, Qt.QPalette.NColorGroups)
colorRoleList = enumList(
    Qt.QPalette.ColorRole, Qt.QPalette.NColorRoles)
handList  = enumList(
    Qwt.QwtAnalogClock.Hand, Qwt.QwtAnalogClock.NHands)

 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Dial_3(Widget, Qwt.QwtDial):
    def __init__(self, parent=None):
        Widget.__init__(self)
        Qwt.QwtDial.__init__(self,parent)
        self.label = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(28)
        #self.label.setFont(font)
        self.__label = 'km/h'
        #self.__label.resize(20)
        self.setWrapping(False)
        self.setReadOnly(True)
        self.setMode(self.RotateNeedle)
        
        self.setFrameShadow(self.Sunken)
        
        self.setOrigin(90)
        self.setScaleArc(45.0, 315.0)
        self.setNeedle(Qwt.QwtDialSimpleNeedle(
            Qwt.QwtDialSimpleNeedle.Arrow,
            True,
            Qt.QColor(Qt.Qt.red),
            Qt.QColor(Qt.Qt.gray).light(130)))

        self.setScaleOptions(Qwt.QwtDial.ScaleTicks | Qwt.QwtDial.ScaleLabel)
        self.setScaleTicks(0, 4, 8)
        self.setPalette(self.__colorTheme(Qt.QColor(Qt.Qt.darkGray).dark(150)))
        
        self._minValue = 0
        self._maxValue = 300
        self._lowerLimit = 0.0
        self._upperLimit =10.0
        self._step = 20.0
        self.setScale(self._lowerLimit,self._upperLimit,self._step)
        self.setRange( self._minValue, self._maxValue)  
        self._labelFix = False


    
        
    def setSizeLabel(self, text):
        self.__label
    # setLabel()
    
		
    QtCore.SLOT
    pyqtSlot 
    def setValue(self, value):
        super(Dial_3, self).setValue(value)
        self.setLabel(str(value))
  
  
    def setLabel(self, text):
        self.__label = text
        self.update()
    def getLabel(self):
        return self.__label
    label = QtCore.pyqtProperty(str, getLabel, setLabel)
    
    def setMinValue(self, minValue):
         self._minValue = minValue
         super(Dial_3, self).setRange(self._minValue,self._maxValue)
    def getMinValue(self):
         return self._minValue
    MinValue = QtCore.pyqtProperty(float, getMinValue, setMinValue)	 
	
    def setMaxValue(self, maxValue):
         self._maxValue = maxValue
         super(Dial_3, self).setRange(self._minValue,self._maxValue)
    def getMaxValue(self):
         return self._maxValue
    MaxValue = QtCore.pyqtProperty(float, getMaxValue, setMaxValue)	   
    
    def setLowerLimit(self, lowerLimit):
        self._lowerLimit = lowerLimit
        super(Dial_3,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getLowerLimit(self):
        return self._lowerLimit
    LowerLimitScale = QtCore.pyqtProperty(float, getLowerLimit, setLowerLimit)
    
    def setUpperLimit(self, upperLimit):
        self._upperLimit = upperLimit
        super(Dial_3,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getUpperLimit(self):
        return self._upperLimit
    UpperLimitScale = QtCore.pyqtProperty(float, getUpperLimit, setUpperLimit)
    
    def setStep(self, step):
        self._step = step
        super(Dial_3,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getStep(self):
        return self._step
    StepScale = QtCore.pyqtProperty(float, getStep, setStep)   
    
    def setName(self, name):
        self.name = name
        self.objectName = name  
    def getName(self):
        return self.objectName
    name = QtCore.pyqtProperty(str, getName, setName) 
      
    # label()
    def setLabelFix(self, flag):
        self._labelFix = flag

    def getLabelFix(self):
        return self._labelFix
    LabelFixed = QtCore.pyqtProperty(bool, getLabelFix, setLabelFix) 

    def setRange(self, minValue, maxValue):
         self._minValue = minValue
         self._maxValue = maxValue    
         super(Dial_3, self).setRange(self._minValue,self._maxValue)
    def setScale(self, lowerLimit, upperLimit, step):
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        self._step = step
        super(Dial_3,self).setScale( self._lowerLimit,self._upperLimit,self._step)
        
        
    def drawScaleContents(self, painter, center, radius):
        rect = Qt.QRect(0, 0, 2 * radius, 2 * radius - 10)
        rect.moveCenter(center)
        painter.setPen(self.palette().color(Qt.QPalette.Text))
        painter.setFont(QtGui.QFont('Helvetica', 20))
        painter.drawText(
            rect, Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter, self.__label)
            
    def __colorTheme(self, base):
        background = base.dark(150)
        foreground = base.dark(200)
        
        mid = base.dark(110)
        dark = base.dark(170)
        light = base.light(170)
        text = foreground.light(800)

        palette = Qt.QPalette()
        for colorGroup in colorGroupList:
            palette.setColor(colorGroup, Qt.QPalette.Base, base)
            palette.setColor(colorGroup, Qt.QPalette.Background, background)
            palette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            palette.setColor(colorGroup, Qt.QPalette.Light, light)
            palette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            palette.setColor(colorGroup, Qt.QPalette.Text, text)
            palette.setColor(colorGroup, Qt.QPalette.Foreground, foreground)
        
        return palette
    
    @property
    def value(self):
        return super(Dial_3, self).value()
        
    
    @value.setter
    def value(self, value):
        super(Dial_3, self).setValue(value)
        if self._labelFix == False: self.setLabel(str(value))
        
    def getValue(self):
        return super(Dial_3, self).value()
    Value = QtCore.pyqtProperty(float, getValue, setValue) 