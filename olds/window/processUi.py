# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:30:42 2015

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

from aware.resolvePath import ResolvePath
import xml.etree.ElementTree as ET
"""
essaXML = '/home/scholl/Dropbox/Spyder/essa/config/ESSA.xml'
pathInstall, pathLog = ResolvePath(essaXML)
window = None

tree = ET.parse(essaXML)
root = tree.getroot()
for scada in root.iter('scada'):
    window = scada.find('window')
    if window.attrib['name'] is not None:
        try:
            window = window.attrib['name']
        except AttributeError:
            pass
"""           
pathInstall = '/home/scholl/Dropbox/Spyder/'
window = 'system2.ui'
def ProcessUi():
    global pathInstall, window
    os.system("pyuic4 {}essa/window/{} -o {}essa/window/{}{}".format(pathInstall,window,pathInstall,window[:-3],".py"))
    os.system("chmod 777 {}essa/window/{}{}".format(pathInstall,window[:-3],".py"))    

    with open("{}essa/window/{}{}".format(pathInstall,window[:-3],".py"), 'r') as fin, open("{}essa/window/{}1{}".format(pathInstall,window[:-3],".py"), 'w') as fout:
        for line in fin:
           if line.startswith('from '):
               pass
           else:
               fout.write(line)
    
    string = """import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from hmi import *
from aware import *
    
from PyQt4 import QtCore, QtGui"""
    
    with file("{}/essa/window/{}1{}".format(pathInstall,window[:-3],".py"), 'r') as original: data = original.read()
    with file("{}/essa/window/{}{}".format(pathInstall,window[:-3],".py"), 'w') as modified: modified.write(string+"\n" + data)
        
    string2 = """        self.actionAlarm_Log.triggered.connect(self.openViewerLog)
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
    sys.exit(app.exec_())"""  
    os.system("rm {}essa/window/{}1{}".format(pathInstall,window[:-3],".py"))  
    with file("{}/essa/window/{}{}".format(pathInstall,window[:-3],".py"), 'r') as original: data = original.read()
    with file("{}/essa/window/{}{}".format(pathInstall,window[:-3],".py"), 'w') as modified: modified.write(data + "\n"+string2)
    #os.system("rm {}essa/window/{}1{}".format(pathInstall,window[:-3],".py"))    

#ProcessUi()