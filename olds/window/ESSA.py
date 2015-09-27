# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Jun 19 14:24:57 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os

from viwerLog import viwerLog
"""
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
"""

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
"""        
def __init__(self, parent=None):
    Widget.__init__(self)
    Qwt.QwtDial.__init__(self,parent)
"""        
class ESSA(object):
    def setupUi(self, MainWindow, parent=None):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        
        self.actionAlarm_Log.triggered.connect(self.openViwerLog)
        self.actionSystem_Logs.triggered.connect(self.openViwerLogs)
        self.actionRun.triggered.connect(self.run)
        self.actionStop.triggered.connect(self.stop)
        self.actionExit.triggered.connect(self.exiter)
        self.actionESSA_Config.triggered.connect(self.openViwerEssaXML)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESSA - Embeddable SCADA for Small Applications", None))
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
    
    def openViwerLog(self):
        mainWin = viwerLog()
        mainWin.show()
        mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log')
        mainWin.setWindowTitle("ESSA - Alarm Log")
        sys.exit(mainWin.exec_())
        
    def openViwerLogs(self):
        mainWin = viwerLog()
        mainWin.open()
        mainWin.setWindowTitle("ESSA - Logs")
        mainWin.show()
        sys.exit(mainWin.exec_())
        
    def openViwerEssaXML(self):
        mainWin = viwerLog()
        mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/config/ESSA01.xml')
        mainWin.setWindowTitle("ESSA - System Configuration")        
        mainWin.show()
        sys.exit(mainWin.exec_())
        
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = ESSA()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

