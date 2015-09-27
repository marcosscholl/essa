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
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/scholl/Dropbox/Spyder/essa/config/planta.ui'
#
# Created: Tue Jul 21 22:58:50 2015
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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(690, 517)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.led = Led(self.centralwidget)
        self.led.setGeometry(QtCore.QRect(607, 0, 91, 81))
        self.led.setObjectName(_fromUtf8("led"))
        self.tanque2 = Thermo(self.centralwidget)
        self.tanque2.setGeometry(QtCore.QRect(150, 160, 87, 156))
        self.tanque2.setObjectName(_fromUtf8("tanque2"))
        self.tanque3 = Thermo(self.centralwidget)
        self.tanque3.setGeometry(QtCore.QRect(270, 160, 87, 156))
        self.tanque3.setObjectName(_fromUtf8("tanque3"))
        self.tanque4 = Thermo(self.centralwidget)
        self.tanque4.setGeometry(QtCore.QRect(370, 100, 141, 181))
        self.tanque4.setObjectName(_fromUtf8("tanque4"))
        self.tanqueResiduo = Thermo(self.centralwidget)
        self.tanqueResiduo.setGeometry(QtCore.QRect(550, 160, 87, 156))
        self.tanqueResiduo.setObjectName(_fromUtf8("tanqueResiduo"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(50, 140, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setObjectName(_fromUtf8("display"))
        self.display_2 = Display(self.centralwidget)
        self.display_2.setGeometry(QtCore.QRect(170, 140, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display_2.setFont(font)
        self.display_2.setObjectName(_fromUtf8("display_2"))
        self.display_3 = Display(self.centralwidget)
        self.display_3.setGeometry(QtCore.QRect(290, 140, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display_3.setFont(font)
        self.display_3.setObjectName(_fromUtf8("display_3"))
        self.display_4 = Display(self.centralwidget)
        self.display_4.setGeometry(QtCore.QRect(420, 80, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display_4.setFont(font)
        self.display_4.setObjectName(_fromUtf8("display_4"))
        self.display_5 = Display(self.centralwidget)
        self.display_5.setGeometry(QtCore.QRect(570, 140, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.display_5.setFont(font)
        self.display_5.setObjectName(_fromUtf8("display_5"))
        self.tanque1 = Thermo(self.centralwidget)
        self.tanque1.setGeometry(QtCore.QRect(30, 160, 87, 156))
        self.tanque1.setObjectName(_fromUtf8("tanque1"))
        self.display_6 = Display(self.centralwidget)
        self.display_6.setGeometry(QtCore.QRect(150, 18, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.display_6.setFont(font)
        self.display_6.setObjectName(_fromUtf8("display_6"))
        self.display_7 = Display(self.centralwidget)
        self.display_7.setGeometry(QtCore.QRect(290, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.display_7.setFont(font)
        self.display_7.setObjectName(_fromUtf8("display_7"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(85, 310, 501, 151))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.display_8 = Display(self.groupBox)
        self.display_8.setGeometry(QtCore.QRect(380, 40, 101, 19))
        self.display_8.setObjectName(_fromUtf8("display_8"))
        self.onOffButton = OnOffButton(self.groupBox)
        self.onOffButton.setGeometry(QtCore.QRect(190, 100, 111, 35))
        self.onOffButton.setValue(False)
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))
        self.display_9 = Display(self.groupBox)
        self.display_9.setGeometry(QtCore.QRect(25, 40, 61, 20))
        self.display_9.setObjectName(_fromUtf8("display_9"))
        self.display_10 = Display(self.groupBox)
        self.display_10.setGeometry(QtCore.QRect(150, 40, 71, 20))
        self.display_10.setObjectName(_fromUtf8("display_10"))
        self.display_11 = Display(self.groupBox)
        self.display_11.setGeometry(QtCore.QRect(270, 40, 71, 20))
        self.display_11.setObjectName(_fromUtf8("display_11"))
        self.dsb3 = DoubleSpinBox(self.groupBox)
        self.dsb3.setGeometry(QtCore.QRect(270, 60, 71, 33))
        self.dsb3.setObjectName(_fromUtf8("dsb3"))
        self.dsb2 = DoubleSpinBox(self.groupBox)
        self.dsb2.setGeometry(QtCore.QRect(160, 60, 71, 33))
        self.dsb2.setObjectName(_fromUtf8("dsb2"))
        self.dsb1 = DoubleSpinBox(self.groupBox)
        self.dsb1.setGeometry(QtCore.QRect(20, 60, 71, 33))
        self.dsb1.setObjectName(_fromUtf8("dsb1"))
        self.dspVolume = DoubleSpinBox(self.centralwidget)
        self.dspVolume.setGeometry(QtCore.QRect(480, 370, 71, 33))
        self.dspVolume.setObjectName(_fromUtf8("dspVolume"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 31))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESSA - Embeddable SCADA for Small Applications", None))
        self.led.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.tanque2.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.tanque2.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.tanque3.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.tanque3.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.tanque4.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.tanque4.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.tanqueResiduo.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.tanqueResiduo.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "TQ-01", None))
        self.display_2.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_2.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_2.setText(_translate("MainWindow", "TQ-02", None))
        self.display_3.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_3.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_3.setText(_translate("MainWindow", "TQ-03", None))
        self.display_4.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_4.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_4.setText(_translate("MainWindow", "TQ-04", None))
        self.display_5.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_5.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_5.setText(_translate("MainWindow", "Residuo", None))
        self.tanque1.setToolTip(_translate("MainWindow", "Thermo Widget", None))
        self.tanque1.setWhatsThis(_translate("MainWindow", "SCADA Thermo", None))
        self.display_6.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_6.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_6.setText(_translate("MainWindow", "Planta didática-Automação 2015/1", None))
        self.display_7.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_7.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_7.setText(_translate("MainWindow", "Mistura", None))
        self.groupBox.setTitle(_translate("MainWindow", "Percentuais de  Mistura", None))
        self.display_8.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_8.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_8.setText(_translate("MainWindow", "Volume Mistura", None))
        self.onOffButton.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.onOffButton.setText(_translate("MainWindow", "Rodar Mistura", None))
        self.onOffButton.setTextTrue(_translate("MainWindow", "Rodar Mistura", None))
        self.onOffButton.setTextFalse(_translate("MainWindow", "Standby", None))
        self.display_9.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_9.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_9.setText(_translate("MainWindow", "TQ-01", None))
        self.display_10.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_10.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_10.setText(_translate("MainWindow", "TQ-01", None))
        self.display_11.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display_11.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display_11.setText(_translate("MainWindow", "TQ-03", None))
        self.dsb3.setWhatsThis(_translate("MainWindow", "DoubleSpinBox SCADA", None))
        self.dsb2.setWhatsThis(_translate("MainWindow", "DoubleSpinBox SCADA", None))
        self.dsb1.setWhatsThis(_translate("MainWindow", "DoubleSpinBox SCADA", None))
        self.dspVolume.setWhatsThis(_translate("MainWindow", "DoubleSpinBox SCADA", None))
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
        self.mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/planta.xml')
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
    
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui._app = app
    MainWindow.show()
    sys.exit(app.exec_())
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
        self.mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/planta.xml')
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