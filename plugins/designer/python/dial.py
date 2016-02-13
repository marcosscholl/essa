# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:30:18 2015

@author: MarcosScholl
"""
import sys
from PyQt4 import Qt,QtGui, QtCore
import PyQt4.Qwt5 as Qwt

import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *


class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Dial(Widget, Qwt.QwtDial):
    def __init__(self, parent=None):
        Widget.__init__(self)
        Qwt.QwtDial.__init__(self,parent)
        self.setGeometry(QtCore.QRect(90, 10, 266, 261))

        self.name = "Dial"
        self.setReadOnly(True)
        self.setLineWidth(5)
        self.setFrameShadow(Qwt.QwtDial.Sunken)
        self.setMode(Qwt.QwtDial.RotateNeedle)
        self.setOrigin(90.0)
        self.setWrapping(False)
        self.setObjectName("qwtDial")
        
        self._minValue = 0
        self._maxValue = 500
        self._lowerLimit = 0.0
        self._upperLimit =10.0
        self._step = 25.0
        self.setScale(self._lowerLimit,self._upperLimit,self._step)
        self.setRange( self._minValue, self._maxValue)  
       
        self._labelFix = False


        #-- paramétrage initial du QwtDial -- 
        self.setOrigin(90.0) # point de référence du tracé - 0°=3H, 90° = 6H, etc..
        #self.qwtDial.setScaleArc(90.0, 270.0) # angle début / angle fin du tracé par rapport à l'origine
        self.setScaleArc(45.0, 315.0) # angle début / angle fin du tracé par rapport à l'origine
        self.__label = 'km/h'
        
        
        
        
        
        
        #self.setScaleOptions(Qwt.QwtDial.ScaleTicks | Qwt.QwtDial.ScaleLabel)
        #self.setScaleTicks(0, 4, 8)

        #-- création de l'aiguille et association au QwtDial 
        #QwtDialSimpleNeedle    (       Style   style, bool     hasKnob = true, const QColor &          mid = Qt::gray, const QColor &          base = Qt::darkGray ) 
        aiguille= Qwt.QwtDialSimpleNeedle(Qwt.QwtDialSimpleNeedle.Arrow,True,QtGui.QColor(QtCore.Qt.red),QtGui.QColor(QtCore.Qt.blue)) # défini un QwtDialSimpleNeedle = aiguille simple
        # .Arrow = style aiguille "flèche" | .Ray = style simple ligne 
        self.setNeedle(aiguille) # associe l
     
            
    def drawScaleContents(self, painter, center, radius):
        rect = Qt.QRect(0, 0, 2 * radius, 2 * radius - 10)
        rect.moveCenter(center)
        painter.setPen(self.palette().color(Qt.QPalette.Text))
        painter.setFont(QtGui.QFont('Helvetica', 20))
        painter.drawText(
            rect, Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter, self.__label)
            
    @property
    def text(self):
        return self.__label
        
    @text.setter   
    def text(self, text):
        self.__label = text
        self.update()
        
        
    def setSizeLabel(self, text):
        self.__label
    # setLabel()
    

    def setValue(self, value):
        super(Dial, self).setValue(value)
        self.setLabel(str(value))
        

    def setRange(self, minValue, maxValue):
         self._minValue = minValue
         self._maxValue = maxValue    
         super(Dial, self).setRange(self._minValue,self._maxValue)
         
        
    def setScale(self, lowerLimit, upperLimit, step):
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        self._step = step
        super(Dial,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    
    def setLabel(self, text):
        self.__label = text
        self.update()
    def getLabel(self):
        return self.__label
    label = QtCore.pyqtProperty(str, getLabel, setLabel)
    
    def setLabelFix(self, flag):
        self._labelFix = flag

    def getLabelFix(self):
        return self._labelFix
    LabelFixed = QtCore.pyqtProperty(bool, getLabelFix, setLabelFix)  

    def setMinValue(self, minValue):
         self._minValue = minValue
         super(Dial, self).setRange(self._minValue,self._maxValue)
    def getMinValue(self):
         return self._minValue
    MinValue = QtCore.pyqtProperty(float, getMinValue, setMinValue)	 
	
    def setMaxValue(self, maxValue):
         self._maxValue = maxValue
         super(Dial, self).setRange(self._minValue,self._maxValue)
    def getMaxValue(self):
         return self._maxValue
    MaxValue = QtCore.pyqtProperty(float, getMaxValue, setMaxValue)	   
    
    def setLowerLimit(self, lowerLimit):
        self._lowerLimit = lowerLimit
        super(Dial,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getLowerLimit(self):
        return self._lowerLimit
    LowerLimitScale = QtCore.pyqtProperty(float, getLowerLimit, setLowerLimit)
    
    def setUpperLimit(self, upperLimit):
        self._upperLimit = upperLimit
        super(Dial,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getUpperLimit(self):
        return self._upperLimit
    UpperLimitScale = QtCore.pyqtProperty(float, getUpperLimit, setUpperLimit)
    
    def setStep(self, step):
        self._step = step
        super(Dial,self).setScale( self._lowerLimit,self._upperLimit,self._step)
    def getStep(self):
        return self._step
    StepScale = QtCore.pyqtProperty(float, getStep, setStep)   
    
    def setName(self, nome):
        self.objectName = nome  
        
    def getName(self):
        return self.objectName
    name = QtCore.pyqtProperty(str, getName, setName) 
        
    @property
    def value(self):
        return super(Dial, self).value()
    
    @value.setter
    def value(self, value):
        super(Dial, self).setValue(value)
        if self._labelFix == False: self.setLabel(str(value))
		#self.notify(EventChanged(self))
    def getValue(self):
        return super(Dial, self).value()
    Value = QtCore.pyqtProperty(int, getValue, setValue) 
"""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
   
    dial = Dial(window)
    #dial.setRange(0,100)
    dial.setValue(50)
    dial.setScale(0,3.0,5.0)
    dial.setStep(50)
   
    
    layout = QtGui.QVBoxLayout()

    layout.addWidget(dial)
    window.setLayout(layout)
    
    window.show()
    
    sys.exit(app.exec_())
"""