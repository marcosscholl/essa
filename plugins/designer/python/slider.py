# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slider.ui'
#
# Created: Tue May 12 23:28:10 2015
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

class Slider(Widget, QtGui.QSlider):
    def __init__(self, parent = None):
        Widget.__init__(self)
        #super(Widget,self).__init__()
        QtGui.QSlider.__init__(self,parent)
        self._min_value = 0.0
        self._max_value = 100.0
        self._max_int = 10000
        self.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setInvertedAppearance(False)
        self.setInvertedControls(True)
        self.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.setTickInterval(10)
        self.setObjectName("horizontalSlider")
        self.setMinimum(0)
        
        self.setMaximum(self._max_value)
        
        self.setProperty("value", self._min_value)
        self.valueChanged.connect(self.valueHandler)

    def valueHandler(self,value):
        self.value= value
        #print self.value  #type of "value" is int so you need to convert it to float in order to get float type for "scaledValue" 
       

    @property
    def name(self):
        return self.objectName
        
    @name.setter
    def name(self,name):
        #self.name = name
        self.setObjectName(name)
    
    
    def geometry(self, x, y, width, heigth):
        self.setGeometry(QtCore.QRect( x, y, width, heigth))
        

    """
    def setRange(self, minValue, maxValue):
         super(Slider, self).setRange(minValue,maxValue)
    """

    def setScale(self, lowerLimit, upperLimit, step):
        super(Slider,self).setScale(lowerLimit,upperLimit,step)
    
    def setName(self, name):
        self.name = name
        self.objectName = name
    
    def getName(self):
        return self.name
    Name = QtCore.pyqtProperty(str,fget=getName,fset=setName)     
    @property
    def value(self):
        return super(Slider, self).value()
    
    @value.setter
    def value(self, value):
        super(Slider, self).setValue(value)
        self.notify(EventChanged(self))
        #self.setLabel(str(value))
        
    def setValue(self, value):
        super(Slider, self).setValue(value)
        self.notify(EventChanged(self))
        #self.setLabel(str(value))
    def getValue(self):
        return super(Slider, self).value() 
    Value = QtCore.pyqtProperty(float,fget=getValue,fset=setValue) 
    
    @property
    def _value_range(self):
        return self._max_value - self._min_value
 
    def setMinimumValue(self, value):
        self.setRange(value, self._max_value)
        
    def getMinimumValue(self):
        return self._min_value
        
    Minimum_Value = QtCore.pyqtProperty(float,fget=getMinimumValue,fset=setMinimumValue)     
    def setMaximumValue(self, value):
        self.setRange(self._min_value, value)
    def getMaximumValue(self):
        return self._max_value
    Maximum_Value = QtCore.pyqtProperty(float,fget=getMaximumValue,fset=setMaximumValue)      
        
    def setRange(self, minimum, maximum):
        old_value = self.value
        self._min_value = minimum
        self.setMinimum(minimum)
        self._max_value = maximum
        self.setMaximum(maximum)
        self.setValue(old_value)  # Put slider in correct position
    """    
    def value(self):
        print "Value"
        return float(super(Slider, self).value()) / self._max_int * self._value_range
 
    def setValue(self, value):
        super(Slider, self).setValue(int(value / self._value_range * self._max_int))
    """
    def proportion(self):
        return (self.value() - self._min_value) / self._value_range

"""     
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    botao = Slider()
    layout.addWidget(botao)
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""