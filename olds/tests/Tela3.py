# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela3.ui'
#
# Created: Thu May 21 17:53:32 2015
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.dial_3Widget = Dial_3(self.widget)
        self.dial_3Widget.setGeometry(QtCore.QRect(250, 40, 186, 186))
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))
        self.display_2 = Display(self.widget)
        self.display_2.setGeometry(QtCore.QRect(470, 380, 151, 31))
        self.display_2.setObjectName(_fromUtf8("display_2"))
        self.dial_2Widget = Dial_2(self.widget)
        self.dial_2Widget.setGeometry(QtCore.QRect(50, 30, 196, 196))
        self.dial_2Widget.setObjectName(_fromUtf8("dial_2Widget"))
        self.displayLCD = DisplayLCD(self.widget)
        self.displayLCD.setGeometry(QtCore.QRect(480, 320, 91, 61))
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.thermo = Thermo(self.widget)
        self.thermo.setGeometry(QtCore.QRect(580, 20, 93, 401))
        self.thermo.setObjectName(_fromUtf8("thermo"))
        self.onOffButton = OnOffButton(self.widget)
        self.onOffButton.setGeometry(QtCore.QRect(280, 480, 75, 23))
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))
        self.thermometer = Thermometer(self.widget)
        self.thermometer.setGeometry(QtCore.QRect(480, 20, 121, 311))
        self.thermometer.setObjectName(_fromUtf8("thermometer"))
        self.led = Led(self.widget)
        self.led.setGeometry(QtCore.QRect(110, 430, 88, 88))
        self.led.setObjectName(_fromUtf8("led"))
        self.slider = Slider(self.widget)
        self.slider.setGeometry(QtCore.QRect(460, 460, 191, 29))
        self.slider.setObjectName(_fromUtf8("slider"))
        self.dial_1Widget = Dial_1(self.widget)
        self.dial_1Widget.setGeometry(QtCore.QRect(50, 230, 196, 196))
        self.dial_1Widget.setObjectName(_fromUtf8("dial_1Widget"))
        self.display = Display(self.widget)
        self.display.setGeometry(QtCore.QRect(250, 10, 221, 20))
        self.display.setObjectName(_fromUtf8("display"))
        self.dial_Widget = Dial(self.widget)
        self.dial_Widget.setGeometry(QtCore.QRect(250, 240, 202, 202))
        self.dial_Widget.setMaxValue(150)
        self.dial_Widget.setProperty("UpperLimitScale", 5)
        self.dial_Widget.setProperty("StepScale", 10)
        self.dial_Widget.setObjectName(_fromUtf8("dial_Widget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.display_2.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_2.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_2.setText(_translate("MainWindow", "Temperatura Caldeira", None))
        self.dial_2Widget.setToolTip(_translate("MainWindow", "Dial Widget 2", None))
        self.dial_2Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 2", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
        self.thermo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.thermo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.onOffButton.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.thermometer.setToolTip(_translate("MainWindow", "Thermometer Widget", None))
        self.thermometer.setWhatsThis(_translate("MainWindow", "SCADA Thermometer", None))
        self.led.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.slider.setToolTip(_translate("MainWindow", "Slider Widget", None))
        self.slider.setWhatsThis(_translate("MainWindow", "SCADA Slider", None))
        self.dial_1Widget.setToolTip(_translate("MainWindow", "Dial Widget 1", None))
        self.dial_1Widget.setWhatsThis(_translate("MainWindow", "Widgets SCADA dial", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "Simulação de Supervisório", None))
        self.dial_Widget.setToolTip(_translate("MainWindow", "Dial Widget", None))
        self.dial_Widget.setWhatsThis(_translate("MainWindow", "Dial SCADA", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

