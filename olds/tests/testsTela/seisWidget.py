# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seisWidget.ui'
#
# Created: Tue Jun  2 22:15:29 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 532)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial_3Widget = Dial_3(self.centralwidget)
        self.dial_3Widget.setGeometry(QtCore.QRect(0, 0, 234, 234))
        self.dial_3Widget.setMaxValue(1000)
        self.dial_3Widget.setProperty("StepScale", 50)
        self.dial_3Widget.setObjectName("dial_3Widget")
        self.dial_3Widget_2 = Dial_3(self.centralwidget)
        self.dial_3Widget_2.setGeometry(QtCore.QRect(0, 240, 234, 234))
        self.dial_3Widget_2.setMaxValue(1000)
        self.dial_3Widget_2.setProperty("StepScale", 50)
        self.dial_3Widget_2.setObjectName("dial_3Widget_2")
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(170, 10, 161, 91))
        self.displayLCD.setObjectName("displayLCD")
        self.thermometer = Thermometer(self.centralwidget)
        self.thermometer.setGeometry(QtCore.QRect(260, 160, 121, 331))
        self.thermometer.setProperty("MaxValue", 1000.0)
        self.thermometer.setMinLimit(500.0)
        self.thermometer.setMaxLimit(750.0)
        self.thermometer.setObjectName("thermometer")
        self.slider = Slider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(350, 20, 141, 61))
        self.slider.setProperty("Maximum_Value", 1000.0)
        self.slider.setObjectName("slider")
        self.thermo = Thermo(self.centralwidget)
        self.thermo.setGeometry(QtCore.QRect(392, 160, 101, 331))
        self.thermo.setAlarmLevel(800.0)
        self.thermo.setProperty("MaximumValue", 1000.0)
        self.thermo.setObjectName("thermo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)