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
from PyQt4.Qwt5 import *
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/scholl/Dropbox/Spyder/essa/config/MPCT_Simulation.ui'
#
# Created: Fri Feb 12 21:42:05 2016
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
        MainWindow.resize(1305, 631)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.onOffButton = OnOffButton(self.centralwidget)
        self.onOffButton.setGeometry(QtCore.QRect(670, 220, 91, 51))
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))
        self.slider = Slider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(630, 480, 181, 61))
        self.slider.setObjectName(_fromUtf8("slider"))
        self.thermometer = Thermometer(self.centralwidget)
        self.thermometer.setGeometry(QtCore.QRect(430, 90, 171, 611))
        self.thermometer.setObjectName(_fromUtf8("thermometer"))
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(640, 290, 141, 71))
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        self.plot = Plot(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(0, 390, 400, 321))
        self.plot.setObjectName(_fromUtf8("plot"))
        self.dial1 = Dial_3(self.centralwidget)
        self.dial1.setGeometry(QtCore.QRect(60, 70, 300, 300))
        self.dial1.setProperty("LabelFixed", True)
        self.dial1.setObjectName(_fromUtf8("dial1"))
        self.thermo = Thermo(self.centralwidget)
        self.thermo.setGeometry(QtCore.QRect(792, 100, 161, 581))
        self.thermo.setProperty("MaximumValue", 250.0)
        self.thermo.setObjectName(_fromUtf8("thermo"))
        self.led = Led(self.centralwidget)
        self.led.setGeometry(QtCore.QRect(1190, 0, 88, 88))
        self.led.setObjectName(_fromUtf8("led"))
        self.dial3 = Dial_1(self.centralwidget)
        self.dial3.setGeometry(QtCore.QRect(960, 400, 300, 300))
        self.dial3.setObjectName(_fromUtf8("dial3"))
        self.doubleSpinBox = DoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(670, 400, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 1271, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setObjectName(_fromUtf8("display"))
        self.dial2 = Dial(self.centralwidget)
        self.dial2.setGeometry(QtCore.QRect(960, 70, 300, 300))
        self.dial2.setProperty("LabelFixed", True)
        self.dial2.setMaxValue(1500.0)
        self.dial2.setProperty("StepScale", 100.0)
        self.dial2.setObjectName(_fromUtf8("dial2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1305, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSystem = QtGui.QMenu(self.menubar)
        self.menuSystem.setObjectName(_fromUtf8("menuSystem"))
        self.menuLogs = QtGui.QMenu(self.menubar)
        self.menuLogs.setObjectName(_fromUtf8("menuLogs"))
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        self.menuAnalisys = QtGui.QMenu(self.menubar)
        self.menuAnalisys.setObjectName(_fromUtf8("menuAnalisys"))
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
        self.actionHistogram = QtGui.QAction(MainWindow)
        self.actionHistogram.setObjectName(_fromUtf8("actionHistogram"))
        self.menuSystem.addAction(self.actionRun)
        self.menuSystem.addAction(self.actionStop)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionCompile_and_Run)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionExit)
        self.menuLogs.addAction(self.actionAlarm_Log)
        self.menuLogs.addAction(self.actionSystem_Logs)
        self.menuConfig.addAction(self.actionESSA_Config)
        self.menuAnalisys.addAction(self.actionHistogram)
        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuLogs.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuAnalisys.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESSA - Embeddable SCADA for Small Applications", None))
        self.onOffButton.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.slider.setToolTip(_translate("MainWindow", "Slider Widget", None))
        self.slider.setWhatsThis(_translate("MainWindow", "SCADA Slider", None))
        self.thermometer.setToolTip(_translate("MainWindow", "Thermometer Widget", None))
        self.thermometer.setWhatsThis(_translate("MainWindow", "SCADA Thermometer", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
        self.plot.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.plot.setWhatsThis(_translate("MainWindow", "SCADA Plot", None))
        self.dial1.setToolTip(_translate("MainWindow", "Dial1", None))
        self.dial1.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))
        self.dial1.setLabel(_translate("MainWindow", "volts", None))
        self.thermo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.thermo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.led.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.dial3.setToolTip(_translate("MainWindow", "Dial Widget 1", None))
        self.dial3.setWhatsThis(_translate("MainWindow", "Widgets SCADA dial", None))
        self.doubleSpinBox.setWhatsThis(_translate("MainWindow", "DoubleSpinBox SCADA", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "Simulation Data Acquisition, Sypervisory and Control", None))
        self.dial2.setToolTip(_translate("MainWindow", "Dial Widget", None))
        self.dial2.setWhatsThis(_translate("MainWindow", "Dial SCADA", None))
        self.dial2.setLabel(_translate("MainWindow", "kHz", None))
        self.menuSystem.setTitle(_translate("MainWindow", "System", None))
        self.menuLogs.setTitle(_translate("MainWindow", "Logs", None))
        self.menuConfig.setTitle(_translate("MainWindow", "Config", None))
        self.menuAnalisys.setTitle(_translate("MainWindow", "Analisys", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionAlarm_Log.setText(_translate("MainWindow", "Alarm Log", None))
        self.actionSystem_Logs.setText(_translate("MainWindow", "System Logs", None))
        self.actionESSA_Config.setText(_translate("MainWindow", "ESSA Config", None))
        self.actionCompile_and_Run.setText(_translate("MainWindow", "Compile and Run", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram", None))


        self.actionAlarm_Log.triggered.connect(self.openViewerLog)
        self.actionSystem_Logs.triggered.connect(self.openViewerLogs)
        self.actionHistogram.triggered.connect(self.openHistogram)
        self.actionRun.triggered.connect(self.run)
        self.actionStop.triggered.connect(self.stop)
        self.actionExit.triggered.connect(self.exiter)
        self.actionESSA_Config.triggered.connect(self.openViewerEssaXML)
        self.actionCompile_and_Run.triggered.connect(self.compileRun)
        self.mainWin = Viewer()
        self.histogram = Histogram()
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
        self.mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/MPCT_Simulation.xml')
        self.mainWin.setWindowTitle("ESSA - System Configuration")        
        self.mainWin.show()
        
    def openHistogram(self):
        self.histogram.setWindowTitle("ESSA - Histogram")
        self.histogram.show()
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui._app = app
    MainWindow.show()
    sys.exit(app.exec_())