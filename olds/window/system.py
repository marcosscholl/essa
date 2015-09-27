# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created: Fri Jun 19 18:52:41 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.thermometer = Thermometer(self.centralwidget)
        self.thermometer.setGeometry(QtCore.QRect(300, 40, 81, 451))
        self.thermometer.setObjectName(_fromUtf8("thermometer"))
        self.thermo = Thermo(self.centralwidget)
        self.thermo.setGeometry(QtCore.QRect(420, 50, 93, 421))
        self.thermo.setObjectName(_fromUtf8("thermo"))
        self.led = Led(self.centralwidget)
        self.led.setGeometry(QtCore.QRect(710, 0, 88, 88))
        self.led.setObjectName(_fromUtf8("led"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(70, -10, 621, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setTextFormat(QtCore.Qt.PlainText)
        self.display.setObjectName(_fromUtf8("display"))
        self.dial_Widget = Dial(self.centralwidget)
        self.dial_Widget.setGeometry(QtCore.QRect(10, 50, 241, 241))
        self.dial_Widget.setObjectName(_fromUtf8("dial_Widget"))
        self.dial_2Widget = Dial_2(self.centralwidget)
        self.dial_2Widget.setGeometry(QtCore.QRect(550, 70, 221, 221))
        self.dial_2Widget.setObjectName(_fromUtf8("dial_2Widget"))
        self.dial_1Widget = Dial_1(self.centralwidget)
        self.dial_1Widget.setGeometry(QtCore.QRect(0, 300, 244, 244))
        self.dial_1Widget.setObjectName(_fromUtf8("dial_1Widget"))
        self.dial_3Widget = Dial_3(self.centralwidget)
        self.dial_3Widget.setGeometry(QtCore.QRect(550, 300, 234, 234))
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))
        self.displayLCD = DisplayLCD(self.centralwidget)
        self.displayLCD.setGeometry(QtCore.QRect(300, 460, 131, 81))
        self.displayLCD.setObjectName(_fromUtf8("displayLCD"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
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

        self.actionAlarm_Log.triggered.connect(self.openViewerLog)
        self.actionSystem_Logs.triggered.connect(self.openViewerLogs)
        self.actionRun.triggered.connect(self.run)
        self.actionStop.triggered.connect(self.stop)
        self.actionExit.triggered.connect(self.exiter)
        self.actionESSA_Config.triggered.connect(self.openViewerEssaXML)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESSA - Embeddable SCADA for Small Applications", None))
        self.thermometer.setToolTip(_translate("MainWindow", "Thermometer Widget", None))
        self.thermometer.setWhatsThis(_translate("MainWindow", "SCADA Thermometer", None))
        self.thermo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.thermo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.led.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "Simulation of Data Acquisition, Supervisory and Control", None))
        self.dial_Widget.setToolTip(_translate("MainWindow", "Dial Widget", None))
        self.dial_Widget.setWhatsThis(_translate("MainWindow", "Dial SCADA", None))
        self.dial_2Widget.setToolTip(_translate("MainWindow", "Dial Widget 2", None))
        self.dial_2Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 2", None))
        self.dial_1Widget.setToolTip(_translate("MainWindow", "Dial Widget 1", None))
        self.dial_1Widget.setWhatsThis(_translate("MainWindow", "Widgets SCADA dial", None))
        self.dial_3Widget.setToolTip(_translate("MainWindow", "Dial Widget 3", None))
        self.dial_3Widget.setWhatsThis(_translate("MainWindow", "SCADA Dial 3", None))
        self.displayLCD.setToolTip(_translate("MainWindow", "DisplayLCD Widget", None))
        self.displayLCD.setWhatsThis(_translate("MainWindow", "DisplayLCD SCADA", None))
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
    def run(self):
        exec("threadScan.start()")
        #pass
    
    def stop(self):
        exec("threadScan.stop()")
        #pass
    
    def compileRun(self):
       #ProcessUi()
        pass
    
    def exiter(self):
        app.exit()
        pass
    
    def openViewerLog(self):
        mainWin = Viewer()
        mainWin.show()
        mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log')
        mainWin.setWindowTitle("ESSA - Alarm Log")
        sys.exit(mainWin.exec_())
        
    def openViewerLogs(self):
        mainWin = Viewer()
        mainWin.open()
        mainWin.setWindowTitle("ESSA - Logs")
        mainWin.show()
        sys.exit(mainWin.exec_())
        
    def openViewerEssaXML(self):
        mainWin = Viewer()
        mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/ESSA01.xml')
        mainWin.setWindowTitle("ESSA - System Configuration")        
        mainWin.show()
        sys.exit(mainWin.exec_())



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

