# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:29:36 2015

@author: scholl
"""

from PyQt4 import QtCore, QtGui
 
class viwerLog(QtGui.QTextEdit):
    def __init__(self):
        super(viwerLog, self).__init__()
        self.curFile = ''
        self.readSettings()
  
    
  
    def open(self):
        #if self.maybeSave():
        fileName = QtGui.QFileDialog.getOpenFileName(self,directory="/home/scholl/Dropbox/Spyder/essa/logs")
        if fileName:
            self.loadFile(fileName)

    def readSettings(self):
        settings = QtCore.QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QtCore.QPoint(200, 200))
        size = settings.value("size", QtCore.QSize(200, 200))
        self.resize(size)
        self.move(pos)

    def loadFile(self, fileName='/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log'):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return
  
        inf = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.setPlainText(inf.readAll())
        self.setReadOnly(True)
        QtGui.QApplication.restoreOverrideCursor()
    
    def readyOnly(self, readOnly):
        self.setReadOnly(readOnly)
                

if __name__ == '__main__':
  
    import sys
  
    app = QtGui.QApplication(sys.argv)
    mainWin = viwerLog()
    mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log')

    mainWin.show()
    sys.exit(app.exec_())
  