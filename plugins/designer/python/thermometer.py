# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:08:23 2015

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:05:05 2015

@author: MarcosScholl
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

OFFSET = 10
SCALE_HEIGHT = 224
    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

        
class Thermometer(Widget, QtGui.QWidget):

    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self,parent)
        self._v = 0
        self.name = "Thermomether"
        self.normal = 25.0
        self.critical = 75.0
        self.m_min = 0.0
        self.m_max = 100.0
        
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.initDrawing(painter)
        self.drawTemperature(painter)
        self.drawBackground(painter)
        painter.end()
        


    def initDrawing(self, painter):
        #self.normal = 25.0
        #self.critical = 75.0
        #self.m_min = 0.0
        #self.m_max = 100.0
        
        

        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width()/2.0, 0.0)
        painter.scale(self.height()/300.0, self.height()/300.0)

    def drawBackground(self, painter):
        path = QtGui.QPainterPath()

        path.moveTo(-7.5, 257.0)
        path.quadTo(-12.5, 263.0, -12.5, 267.5)
        path.quadTo(-12.5, 278.0, 0.0, 280.0)
        path.quadTo(12.5, 278.0, 12.5, 267.5)
        path.moveTo(12.5, 267.5)
        path.quadTo(12.5, 263.0, 7.5, 257.0)

        path.lineTo(7.5, 25.0)
        path.quadTo(7.5, 12.5, 0, 12.5)
        path.quadTo(-7.5, 12.5, -7.5, 25.0)
        path.lineTo(-7.5, 257.0)

        p1 = QtCore.QPointF(-2.0, 0.0)
        p2 = QtCore.QPointF(12.5, 0.0)
        linearGrad = QtGui.QLinearGradient(p1, p2)
        linearGrad.setSpread(QtGui.QGradient.ReflectSpread)
        linearGrad.setColorAt(1.0, QtGui.QColor(0, 150, 225, 170))
        linearGrad.setColorAt(0.0, QtGui.QColor(255, 255, 255, 0))

        painter.setBrush(QtGui.QBrush(linearGrad))
        painter.setPen(QtCore.Qt.black)
        painter.drawPath(path)

        pen = QtGui.QPen()
        length = 12

        for i in range(33):
            pen.setWidthF(1.0)
            length = 12

            if i % 4:
                length = 8
                pen.setWidthF(0.8)

            if i % 2:
                length = 5
                pen.setWidthF(0.6)

            painter.setPen(pen)
            painter.drawLine(-7, 28+i*7, -7*length, 28+i*7)

        for i in range(9):
            num = self.m_min + i * (self.m_max - self.m_min) / 8.0
            val = "{0}".format(num)
            fm = painter.fontMetrics()
            size = fm.size(QtCore.Qt.TextSingleLine, val)
            point = QtCore.QPointF(OFFSET, 252-i*28+size.width()/4.0)

            painter.drawText(point, val)

    def drawTemperature(self, painter):
        if self._v >= self.critical:
            color = QtGui.QColor(255, 0, 0)

        elif self._v >= self.normal:
            color = QtGui.QColor(0, 200, 0)

        else:
            color = QtGui.QColor(0, 0, 255)

        scale = QtGui.QLinearGradient(0.0, 0.0, 5.0, 0.0)
        bulb = QtGui.QRadialGradient(0.0, 267.0, 10.0, -5.0, 262.0)

        scale.setSpread(QtGui.QGradient.ReflectSpread)
        bulb.setSpread(QtGui.QGradient.ReflectSpread)

        color.setHsv(color.hue(), color.saturation(), color.value())
        scale.setColorAt(1.0, color)
        bulb.setColorAt(1.0, color)

        color.setHsv(color.hue(), color.saturation()-200, color.value())
        scale.setColorAt(0.0, color)
        bulb.setColorAt(0.0, color)

        #print "self.value:", self.value 
        #print "self.m_min:", self.m_min
        #print "self.m_max:", self.m_max
        #print "self.value - self.m_min:", self.value - self.m_min
        
        factor = self._v - self.m_min
        
        #print "(factor / self.m_max) - self.m_min:", (factor / self.m_max) - self.m_min
        
        
        factor = (factor / self.m_max) - self.m_min
        
        #print "factor:", factor

        temp = SCALE_HEIGHT * factor
        #print "temp:", temp
        height = temp + OFFSET
        
        #print "temp + OFFSET:", height

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(scale)
        painter.drawRect(-5, 252+OFFSET-height, 10, height)
        painter.setBrush(bulb)
        rect = QtCore.QRectF(-10.0, 258, 20.0, 20.0)
        painter.drawEllipse(rect)

    def getValue(self):
        return self._v
        
    def setValue(self, valor):
        self._v = float(valor)


    def getValueMin(self):
        return self.m_min
        
    def setValueMin(self,valueMin=0.0):
        self.m_min = float(valueMin)
    MinValue = QtCore.pyqtProperty(float,fget=getValueMin,fset=setValueMin)
    
    def getValueMax(self):
        return self.m_max
        
    def setValueMax(self,valueMax=100):
        self.m_max = float(valueMax)
    MaxValue = QtCore.pyqtProperty(float,fget=getValueMax,fset=setValueMax)   
    
    def getRange(self):
        return "(getRange) valueMin:" + self.m_min + "  valueMax:" + self.m_max
        
    def setRange(self,valueMin=0.0,valueMax=100):
        self.m_min = float(valueMin)
        self.m_max = float(valueMax)
    
    def changeVal(self, newValue):
        self._v = float(newValue)
        self.repaint()   
    
    def getMinLimit(self):
        return self.normal
   
    def setMinLimit(self, normal):
        self.normal = normal     
    MinLimit = QtCore.pyqtProperty(float,fget=getMinLimit,fset=setMinLimit)
    
    def getMaxLimit(self):
        return self.critical
   
    def setMaxLimit(self, critical):
        self.critical = critical  
    MaxLimit = QtCore.pyqtProperty(float,fget=getMaxLimit,fset=setMaxLimit)
    def getLimits(self):
        return "(getLimit) normal:", self.normal ,"  critical:" , self.critical 
   
    def setLimits(self, normal, critical):
        self.normal = normal
        self.critical = critical
      
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    Name = QtCore.pyqtProperty(str,fget=getName,fset=setName) 
    
    @property
    def value(self):
        self._v
    
    @value.setter
    def value(self, value):
        self._v = value   
        self.repaint()
    
    def valueGetter(self):
        return self._v
    
    @pyqtSlot()
    def valueSetter(self, value):
        self._v = value   
        self.repaint()
    Value = QtCore.pyqtProperty(float,fget=valueGetter,fset=valueSetter) 
    
"""
if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = QWidget()
    window.setMinimumWidth(150)
    window.setMinimumHeight(300)
    thermo = Thermometer()
    thermo.setRange(0,100)
    #thermo.setValue(90)
    layout = QVBoxLayout()
    
    #p = window.palette()
    #p.setColor(window.backgroundRole(), Qt.white)
    #window.setPalette(p)
    
    layout.addWidget(thermo)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""