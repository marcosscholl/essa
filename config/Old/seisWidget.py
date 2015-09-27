import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from hmi import *
from aware import *
    
from PyQt4 import QtCore, QtGui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/scholl/Dropbox/Spyder/essa/config/seisWidget.ui'
#
# Created: Fri Jun 19 20:03:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(521, 532)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dial_3Widget = Dial_3(self.centralwidget)
        self.dial_3Widget.setGeometry(QtCore.QRect(0, 0, 234, 234))
        self.dial_3Widget.setMaxValue(1000)
        self.dial_3Widget.setProperty("StepScale", 50)
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))
        self.dial_3Widget_2 = Dial_3(self.centralwidget)
        self.dial_3Widget_2.setGeometry(QtCore.QRect(0, 240, 234, 234))
        self.dial_3Widget_2.setMaxValue(1000)
        self.dial_3Widget_2.setProperty("StepScale", 50)
        self.dial_3Widget_2.setObjectName(_fromUtf8("dial_3Widget_2"))
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(170, 10, 161, 91))
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.thermometer = Thermometer(self.centralwidget)
        self.thermometer.setGeometry(QtCore.QRsub(_globals,1)ect(260, 160, 121, 331))
        self.thermometer.setProperty("MaxValue", 1000.0)
        self.thermometer.setMinLimit(25.0)
        self.thermometer.setMaxLimit(75.0)
        self.thermometer.setObjectName(_fromUtf8("thermometer"))
        self.slider = Slider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(350, 20, 141, 61))
        self.slider.setProperty("Maximum_Value", 1000.0)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.thermo = Thermo(self.centralwidget)
        self.thermo.setGeometry(QtCore.QRect(392, 160, 101, 331))
        self.thermo.setAlarmLevel(800.0)
        self.thermo.setProperty("MaximumValue", 1000.0)
        self.thermo.setObjectName(_fromUtf8("thermo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.dial_3Widget.setToolTip(_translate("MainWindow", "Dial Widget 3", None))
        self.dial_3Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))
        self.dial_3Widget_2.setToolTip(_translate("MainWindow", "Dial Widget 3", None))
        self.dial_3Widget_2.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
        self.thermometer.setToolTip(_translate("MainWindow", "Thermometer Widget", None))
        self.thermometer.setWhatsThis(_translate("MainWindow", "SCADA Thermometer", None))
        self.slider.setToolTip(_translate("MainWindow", "Slider Widget", None))
        self.slider.setWhatsThis(_translate("MainWindow", "SCADA Slider", None))
        self.thermo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.thermo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())