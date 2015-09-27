# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150504-0900"
__status__ = "stable"
__license__ = "GPL"

import sys
from PyQt4 import QtGui, QtCore, QtSvg

RED = 0
GREEN = 1
ORANGE = 2
BLACK = 3
BLUE = 4

import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *
from aware import _globals
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from svg import *
import time
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class GenerateLed(Widget, QtGui.QWidget): 
    def __init__(self,  parent = None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self, parent)
        self.color = GREEN
        self.setMinimumSize(QtCore.QSize(70, 70))
        self.setMaximumSize(QtCore.QSize(70, 70))

        #self.colors = ["./svg/widget/led/red.svg", "./svg/widget/led/green.svg", "./svg/widget/led/orange.svg", "./svg/widget/led/gray.svg", "./svg/widget/led/blue.svg"]
        self.colors = [QByteArray(red), QByteArray(green), QByteArray(orange), QByteArray(gray), QByteArray(blue)]
        self.show()
        

       

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawCustomWidget(painter)
        painter.end()

    def drawCustomWidget(self, painter):
        renderer = QtSvg.QSvgRenderer()
        renderer.load(self.colors[self.color])
        renderer.render(painter)

    def setColor(self, newColor):
        self.color = newColor
        self.update()
    
    

class Led(Widget,QtGui.QWidget):
    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self,parent)
        
        
        #self.setGeometry(300, 300, 300, 200)
        #self.setWindowTitle("LED Widget")
        self.create()
        self.led.setColor(GREEN)
        self._eventClick = False
        try:
            self.viwerLogAlarm = Viewer()
        except:
            pass
     
    def create(self):
        #vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        self.led = GenerateLed(self)
        
        hbox.addWidget(self.led)
        
        self.setLayout(hbox)
        
    def eventOnClick(self, eventClick):
        self._eventClick = eventClick
        
    def mousePressEvent(self, event):
        if self._eventClick is not None:
            try:
                if (os.stat("../logs/ESSA_WarningAlarm.log").st_size == 0):
                    return
                else:
                    self.viwerLogAlarm.loadFile("../logs/ESSA_WarningAlarm.log")  
                    self.viwerLogAlarm.setWindowTitle("ESSA - Warning Alarm")
                    self.viwerLogAlarm.resizeWindow(500,200)
                    self.viwerLogAlarm.show()          
                    time.sleep(1)
                    _globals.alarmAlerts = 0
                    #os.system("sudo rm ../logs/ESSA_WarningAlarm.log")
                    open('../logs/ESSA_WarningAlarm.log', 'w').close()
            except:
                pass
    def onClick(self):
        sender = self.sender()
        text = sender.text()

        if text == "Normal":
            self.normal

        elif text == "Warning":
            self.warning

        elif text == "Emergency":
            self.emergency

        elif text == "Off":
            self.off
            
        elif text == "Blue":
            self.wait
            
    @property
    def normal(self):
        self.led.setColor(GREEN)
        
    @property    
    def warning(self):
         self.led.setColor(ORANGE)
         
    @property     
    def emergency(self):
        self.led.setColor(RED)
        
    @property    
    def off(self):
        self.led.setColor(BLACK)
        
    @property    
    def wait(self):
        self.led.setColor(BLUE)
    
    @property
    def value(self):
        return self.led
        
    @value.setter    
    def value(self, value):
        if value == "Normal":
            self.normal
        elif value == "Warning":
            self.warning
        elif value == "Emergency":
            self.emergency
        elif value == "Off":
            self.off            
        elif value == "Blue":
            self.wait
        
            
    def setValue(self, value):
        self.value = (value)
        
    Value = QtCore.pyqtProperty(str,fget=value,fset=setValue) 
    def minimunSize(self,x,y):   
        self.led.setMinimumSize(QtCore.QSize(x, y))
        
    def maximumSize(self,x,y): 
        self.led.setMaximumSize(QtCore.QSize(x, x))
        
    def setName(self, name):
        self.objectName = name
    
    def getName(self):
        return self.objectName()   
    Name = QtCore.pyqtProperty(str,fget=getName,fset=setName) 
    

"""
if __name__ == "__main__":
    app = QtGui.QApplication([])
    root = Led()
    #root.value = "Warning"
    root.show()
    sys.exit(app.exec_())
"""