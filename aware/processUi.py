# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:00:48 2015

@author: root
"""

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150618-1000"
__status__ = "beta"
__license__ = "GPL"

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from aware import _globals
from runtime import *


def ProcessUi(pathInstall, window):
    os.system("pyuic4 {}essa/config/{} -o {}essa/config/{}{}".format(pathInstall,window,pathInstall,window[:-3],".py"))
    os.system("chmod 777 {}essa/config/{}{}".format(pathInstall,window[:-3],".py"))    

    with open("{}essa/config/{}{}".format(pathInstall,window[:-3],".py"), 'r') as fin, open("{}essa/config/{}1{}".format(pathInstall,window[:-3],".py"), 'w') as fout:
        for line in fin:
           if line.startswith('from '):
               pass
           else:
               fout.write(line)
    
    string = """# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from hmi import *
from aware import *
from runtime import *
from alarm import *
from logger import *
from aware import _globals    
from PyQt4 import QtCore, QtGui"""
    
    with file("{}/essa/config/{}1{}".format(pathInstall,window[:-3],".py"), 'r') as original: data = original.read()
    with file("{}/essa/config/{}{}".format(pathInstall,window[:-3],".py"), 'w') as modified: modified.write(string+"\n" + data)
        
    string2 = """        self.actionAlarm_Log.triggered.connect(self.openViewerLog)
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
        self.mainWin.loadFile('"""+"{}essa/logs/Essa_Alarm.log".format(pathInstall)+"""')
        self.mainWin.setWindowTitle("ESSA - Alarm Log")
        self.mainWin.show()
        
    def openViewerLogs(self):
        self.mainWin.open()
        self.mainWin.setWindowTitle("ESSA - Logs")
        self.mainWin.show()
        
    def openViewerEssaXML(self):
        self.mainWin.loadFile('"""+"{}".format(_globals.fileConfigPath)+"""')
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
    sys.exit(app.exec_())"""  
    os.system("rm {}essa/config/{}1{}".format(pathInstall,window[:-3],".py"))  
    with file("{}/essa/config/{}{}".format(pathInstall,window[:-3],".py"), 'r') as original: data = original.read()
    with file("{}/essa/config/{}{}".format(pathInstall,window[:-3],".py"), 'w') as modified: modified.write(data + "\n"+string2)
    #os.system("rm {}essa/window/{}1{}".format(pathInstall,window[:-3],".py"))   
    

#ProcessUi()