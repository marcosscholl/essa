# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela1.ui'
#
# Created: Sun May 17 13:39:06 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *

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
        MainWindow.resize(654, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.display.setProperty("StartText", _fromUtf8(""))
        self.display.setProperty("DisplayVisible", True)
        self.display.setObjectName(_fromUtf8("display"))
        self.thermo = Thermo(self.centralwidget)
        self.thermo.setGeometry(QtCore.QRect(460, 90, 93, 401))
        self.thermo.setProperty("MinimumValue", 0)
        self.thermo.setProperty("MaximumValue", 100)
        self.thermo.setProperty("AlarmLevel", 80)
        self.thermo.setProperty("DisplayVisible", True)
        self.thermo.setObjectName(_fromUtf8("thermo"))
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(300, 240, 81, 51))
        self.displayLCD.setProperty("Value", 0)
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.led = Led(self.centralwidget)
        self.led.setGeometry(QtCore.QRect(290, 120, 88, 88))
        self.led.setProperty("MinimumSizeX", 50)
        self.led.setProperty("MinimumSizeY", 50)
        self.led.setProperty("MaximumSizeX", 50)
        self.led.setProperty("MaximumSizey", 50)
        self.led.setObjectName(_fromUtf8("led"))
        self.display_2 = Display(self.centralwidget)
        self.display_2.setGeometry(QtCore.QRect(320, 300, 40, 16))
        self.display_2.setProperty("StartText", _fromUtf8(""))
        self.display_2.setProperty("DisplayVisible", True)
        self.display_2.setObjectName(_fromUtf8("display_2"))
        self.dial_2Widget = Dial_2(self.centralwidget)
        self.dial_2Widget.setGeometry(QtCore.QRect(40, 80, 196, 196))
        self.dial_2Widget.setProperty("Value", 0)
        self.dial_2Widget.setProperty("MinimumRange", 0)
        self.dial_2Widget.setProperty("MaximumRange", 100)
        self.dial_2Widget.setProperty("MinimumScale", 0)
        self.dial_2Widget.setProperty("MaximumScale", 3)
        self.dial_2Widget.setProperty("StepScale", 5)
        self.dial_2Widget.setObjectName(_fromUtf8("dial_2Widget"))
        self.dial_3Widget = Dial_3(self.centralwidget)
        self.dial_3Widget.setGeometry(QtCore.QRect(40, 280, 191, 191))
        self.dial_3Widget.setProperty("Value", 0)
        self.dial_3Widget.setProperty("MinimumRange", 0)
        self.dial_3Widget.setProperty("MaximumRange", 100)
        self.dial_3Widget.setProperty("MinimumScale", 0)
        self.dial_3Widget.setProperty("MaximumScale", 3)
        self.dial_3Widget.setProperty("StepScale", 5)
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setProperty("StaticText", _translate("MainWindow", "Simulação Supervisório", None))
        self.thermo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.thermo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
        self.led.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.led.setProperty("Value", _translate("MainWindow", "BLUE", None))
        self.display_2.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_2.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_2.setProperty("StaticText", _translate("MainWindow", "Temperatura Caldeira", None))
        self.dial_2Widget.setToolTip(_translate("MainWindow", "Dial Widget 2", None))
        self.dial_2Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 2", None))
        self.dial_3Widget.setToolTip(_translate("MainWindow", "Dial Widget 3", None))
        self.dial_3Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

