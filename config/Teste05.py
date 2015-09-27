# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from hmi import *
from aware import *
from runtime import *
from alarm import *
from logger import *
from aware import _globals    
from PyQt4 import QtCore, QtGui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/scholl/Dropbox/Spyder/essa/config/Teste05.ui'
#
# Created: Thu Sep  3 18:45:27 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(759, 604)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.thermometer = Thermometer(self.centralwidget)
        self.thermometer.setGeometry(QtCore.QRect(330, 80, 121, 381))
        self.thermometer.setObjectName(_fromUtf8("thermometer"))
        self.led = Led(self.centralwidget)
        self.led.setGeometry(QtCore.QRect(670, 0, 88, 88))
        self.led.setObjectName(_fromUtf8("led"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 681, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setTextFormat(QtCore.Qt.PlainText)
        self.display.setObjectName(_fromUtf8("display"))
        self.dial_Widget = Dial(self.centralwidget)
        self.dial_Widget.setGeometry(QtCore.QRect(490, 170, 234, 234))
        self.dial_Widget.setMaxValue(255.0)
        self.dial_Widget.setObjectName(_fromUtf8("dial_Widget"))
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(320, 430, 131, 71))
        self.displayLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.plot = Plot(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(0, 50, 281, 231))
        self.plot.setObjectName(_fromUtf8("plot"))
        self.onOffButton = OnOffButton(self.centralwidget)
        self.onOffButton.setGeometry(QtCore.QRect(330, 510, 131, 29))
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))
        self.display_2 = Display(self.centralwidget)
        self.display_2.setGeometry(QtCore.QRect(330, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.display_2.setFont(font)
        self.display_2.setObjectName(_fromUtf8("display_2"))
        self.display_4 = Display(self.centralwidget)
        self.display_4.setGeometry(QtCore.QRect(480, 130, 251, 291))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.display_4.setFont(font)
        self.display_4.setFrameShape(QtGui.QFrame.Box)
        self.display_4.setTextFormat(QtCore.Qt.PlainText)
        self.display_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.display_4.setObjectName(_fromUtf8("display_4"))
        self.display_5 = Display(self.centralwidget)
        self.display_5.setGeometry(QtCore.QRect(15, 280, 251, 271))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.display_5.setFont(font)
        self.display_5.setFrameShape(QtGui.QFrame.Box)
        self.display_5.setTextFormat(QtCore.Qt.PlainText)
        self.display_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.display_5.setObjectName(_fromUtf8("display_5"))
        self.dial_3Widget = Dial_3(self.centralwidget)
        self.dial_3Widget.setGeometry(QtCore.QRect(25, 312, 234, 234))
        self.dial_3Widget.setMaxValue(3000.0)
        self.dial_3Widget.setProperty("UpperLimitScale", 100.0)
        self.dial_3Widget.setProperty("StepScale", 250.0)
        self.dial_3Widget.setProperty("LabelFixed", False)
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))
        self.slider = Slider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(510, 440, 181, 35))
        self.slider.setMaximum(255)
        self.slider.setObjectName(_fromUtf8("slider"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSystem = QtGui.QMenu(self.menubar)
        self.menuSystem.setObjectName(_fromUtf8("menuSystem"))
        self.menuLogs = QtGui.QMenu(self.menubar)
        self.menuLogs.setObjectName(_fromUtf8("menuLogs"))
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionAlarm_Log = QtGui.QAction(MainWindow)
        self.actionAlarm_Log.setObjectName(_fromUtf8("actionAlarm_Log"))
        self.actionSystem_Logs = QtGui.QAction(MainWindow)
        self.actionSystem_Logs.setObjectName(_fromUtf8("actionSystem_Logs"))
        self.actionESSA_Config = QtGui.QAction(MainWindow)
        self.actionESSA_Config.setObjectName(_fromUtf8("actionESSA_Config"))
        self.actionCompile_and_Run = QtGui.QAction(MainWindow)
        self.actionCompile_and_Run.setObjectName(_fromUtf8("actionCompile_and_Run"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuSystem.addAction(self.actionRun)
        self.menuSystem.addAction(self.actionStop)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionCompile_and_Run)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionExit)
        self.menuLogs.addAction(self.actionAlarm_Log)
        self.menuLogs.addAction(self.actionSystem_Logs)
        self.menuConfig.addAction(self.actionESSA_Config)
        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuLogs.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dial_Widget, self.onOffButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESSA - Embeddable SCADA for Small Applications", None))
        self.thermometer.setToolTip(_translate("MainWindow", "Thermometer Widget", None))
        self.thermometer.setWhatsThis(_translate("MainWindow", "SCADA Thermometer", None))
        self.led.setToolTip(_translate("MainWindow", "Alarm Warning", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "Simulação de Aquisição, Supervisão e Atuação", None))
        self.dial_Widget.setToolTip(_translate("MainWindow", "Dial Widget", None))
        self.dial_Widget.setWhatsThis(_translate("MainWindow", "Dial SCADA", None))
        self.dial_Widget.setLabel(_translate("MainWindow", "0", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
        self.plot.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.plot.setWhatsThis(_translate("MainWindow", "SCADA Plot", None))
        self.onOffButton.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.onOffButton.setTextTrue(_translate("MainWindow", "On", None))
        self.display_2.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_2.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_2.setText(_translate("MainWindow", "Caldeira", None))
        self.display_4.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_4.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_4.setText(_translate("MainWindow", "LED", None))
        self.display_5.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_5.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_5.setText(_translate("MainWindow", "RPM", None))
        self.dial_3Widget.setToolTip(_translate("MainWindow", "Dial Widget 3", None))
        self.dial_3Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))
        self.dial_3Widget.setLabel(_translate("MainWindow", "0", None))
        self.slider.setToolTip(_translate("MainWindow", "Slider Widget", None))
        self.slider.setWhatsThis(_translate("MainWindow", "SCADA Slider", None))
        self.menuSystem.setTitle(_translate("MainWindow", "System", None))
        self.menuLogs.setTitle(_translate("MainWindow", "Logs", None))
        self.menuConfig.setTitle(_translate("MainWindow", "Config", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionAlarm_Log.setText(_translate("MainWindow", "Alarm Log", None))
        self.actionSystem_Logs.setText(_translate("MainWindow", "System Logs", None))
        self.actionESSA_Config.setText(_translate("MainWindow", "ESSA Config", None))
        self.actionCompile_and_Run.setText(_translate("MainWindow", "Compile and Run", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


        self.actionAlarm_Log.triggered.connect(self.openViewerLog)
        self.actionSystem_Logs.triggered.connect(self.openViewerLogs)
        self.actionRun.triggered.connect(self.run)
        self.actionStop.triggered.connect(self.stop)
        self.actionExit.triggered.connect(self.exiter)
        self.actionESSA_Config.triggered.connect(self.openViewerEssaXML)
        self.actionCompile_and_Run.triggered.connect(self.compileRun)
        self.mainWin = Viewer()
        self._app = None
        try:
            self.led.eventOnClick(True)
        except:
            pass
        
    def run(self):
        _globals.objThread.resume()
        #pass
    
    def stop(self):
        _globals.objThread.pause()
        #pass
    
    def compileRun(self):
        #ProcessUi()
        pass
    
    def exiter(self):
        #self._app.exit()
        exec("os._exit(0)")
        pass
    
    def openViewerLog(self):
        self.mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log')
        self.mainWin.setWindowTitle("ESSA - Alarm Log")
        self.mainWin.show()
        
    def openViewerLogs(self):
        self.mainWin.open()
        self.mainWin.setWindowTitle("ESSA - Logs")
        self.mainWin.show()
        
    def openViewerEssaXML(self):
        self.mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/Teste05.xml')
        self.mainWin.setWindowTitle("ESSA - System Configuration")        
        self.mainWin.show()
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui._app = app
    MainWindow.show()
    sys.exit(app.exec_())