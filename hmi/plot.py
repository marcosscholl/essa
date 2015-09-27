# -*- coding: utf-8 -*-
"""
Created on Thu May 07 01:57:41 2015

@author: MarcosScholl
"""

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150507-0100"
__status__ = "stable"
__license__ = "GPL"



import sys

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


from PyQt4.QtCore import *
from PyQt4.QtGui import *


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from collections import deque


"""        
class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        Embed in QT4
""" 
    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Plot(Widget, QtGui.QWidget):
    def __init__(self, parent=None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self, parent)
        self._data = 0
        self._amostras = 100
        self._datas = deque(maxlen=self._amostras)
        
        self.create_main_frame()
        #self.plot()

    def create_main_frame(self):
        self.main_frame = QWidget()

        self.fig = Figure((5.0, 4.0), dpi=90)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()
        self.axis = self.fig.add_subplot(111, axisbg='w')
        self.axis.hold(False)
        

        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        self.mpl_toolbar.hide()
        self.canvas.mpl_connect('key_press_event', self.on_key_press)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)

        #self.main_frame.setLayout(vbox)
        self.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)
        
  
    def plot(self):
        ''' plot some random stuff '''
        self.axis.plot(self._datas, '*-')
        self.canvas.draw()
    
    @property
    def value(self):
        return self._data
    
    def add(self, value):
        self._datas.append(value)
            
    @value.setter
    def value(self, data):
        self._data = data
        self.add(data)
        self.plot()
    
        
    def setValue(self, data):
        self._data = data
        self.add(data)
        self.plot()

        
    def amostras(self, amostras):
        self._amostras = amostras
        self._datas = deque(maxlen=self._amostras)
        
    def on_key_press(self, event):
        print('Plot pressed', event.key)
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        try:
            key_press_handler(event, self.canvas, self.mpl_toolbar)
        except:
            pass
      
"""
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
 
    main = Plot()
    main.value = [1,2,3,4,5,6,7,8,9,10]
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()
 
    sys.exit(app.exec_())    
"""

















"""
import sys
from PyQt4 import QtGui
 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import random

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from collections import deque



    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

class Plot(Widget, QtGui.QDialog):
    def __init__(self, parent=None):
        Widget.__init__(self)
        QtGui.QDialog.__init__(self)
        
        self.figure = Figure(figsize=(5, 4), dpi=80)
        self.canvas = FigureCanvas(self.figure)
        
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
         
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()
 
        # Just some button 
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)
 
        self.button1 = QtGui.QPushButton('Zoom')
        self.button1.clicked.connect(self.zoom)
         
        self.button2 = QtGui.QPushButton('Pan')
        self.button2.clicked.connect(self.pan)
         
        self.button3 = QtGui.QPushButton('Home')
        self.button3.clicked.connect(self.home)
        self._data = 0
        self._amostras = 20
        self._datas = deque(maxlen=self._amostras)

 
 
        # set the layout
        forma = QtGui.QVBoxLayout()
        layout = QtGui.QVBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        layout2.addWidget(self.button1)
        layout2.addWidget(self.button2)
        layout2.addWidget(self.button3)
       
        forma.addItem(layout)
        forma.addItem(layout2)
        #forma.setGeometry(10,10,50,50)
        
        self.setLayout(forma)
    
    def home(self):
        self.toolbar.home()
    def zoom(self):
        self.toolbar.zoom()
        
    def pan(self):
        self.toolbar.pan()
         
    def plot(self):
        ''' plot some random stuff '''
        #data = [random.random() for i in range(25)]
        #print data
        ax = self.figure.add_subplot(111, axisbg='w')
        #ax = self.figure.add_subplot(111)
        #print ax
        ax.hold(False)
        ax.plot(self._datas, '*-')
        self.canvas.draw()
    
    @property
    def value(self):
        return self._data
    
    def add(self, value):

        self._datas.append(value)
        #print "ADD Depois:", self._datas
            
    @value.setter
    def value(self, data):
        self._data = data
        self.add(data)
        self.plot()
        
        
        
    def setValue(self, data):
        self._data = data
        self.add(data)
        self.plot()
        

    def setName(self, name):
        self.objectName = name
    
    def getName(self):
        return self.objectName() 
    def amostras(self, amostras):
        self._amostras = amostras
        self._datas = deque(maxlen=self._amostras)
"""
"""        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
 
    main = Plot()
    main.value = [1,2,3,4,5,6,7,8,9,10]
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()
 
    sys.exit(app.exec_())
"""