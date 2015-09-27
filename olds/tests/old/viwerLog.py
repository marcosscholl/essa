# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:29:36 2015

@author: scholl
"""
import os
#from easygui import *
"""
filename = os.path.normcase("/home/scholl/Dropbox/Spyder/essa/logs/Essa_test.log")
f = open(filename, "r")
text = f.readlines()
f.close()
resposta = codebox("Contents of file " + filename, "Show File Contents", text)
"""
"""
image = "/home/scholl/Dropbox/Spyder/essa/images/alert.png"
msg = "Warning: Temperatura Exedida do Limite"
choices = ["Ciente","Atuar sobre Alarme"]
reply = buttonbox(msg, image=image, choices=choices)

"""
"""
import threading 
def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

class MyClass:
    somevar = 'someval'

    @threaded
    def func_to_be_threaded(self, teste):
        print teste
        
teste = MyClass()
teste.func_to_be_threaded("jbaishbad")
"""
import sip
sip.setapi('QVariant', 2)
  
from PyQt4 import QtCore, QtGui
  
  
  
class viwerLog(QtGui.QMainWindow):
    def __init__(self):
        super(viwerLog, self).__init__()
  
        self.curFile = ''
  
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
  
        self.createActions()
        self.createMenus()
        self.createToolBars()
        #self.createStatusBar()
  
        self.readSettings()
  
        self.textEdit.document().contentsChanged.connect(self.documentWasModified)
  
        self.setCurrentFile('')
        self.setUnifiedTitleAndToolBarOnMac(True)
  
    def closeEvent(self, event):
        """        
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
        """
        event.accept()
  
    def newFile(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile('')
  
    def open(self):
        #if self.maybeSave():
        fileName = QtGui.QFileDialog.getOpenFileName(self,directory="/home/scholl/Dropbox/Spyder/essa/logs")
        if fileName:
            self.loadFile(fileName)
  
    def save(self):
        if self.curFile:
            return self.saveFile(self.curFile)
  
        return self.saveAs()
  
    def saveAs(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self)
        if fileName:
            return self.saveFile(fileName)
  
        return False
  
    def about(self):
        QtGui.QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")
  
    def documentWasModified(self):
        self.setWindowModified(self.textEdit.document().isModified())
        
    def createActions(self):
        self.newAct = QtGui.QAction(QtGui.QIcon(':/images/new.png'), "&New",
                self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=self.newFile)
  
        self.openAct = QtGui.QAction(QtGui.QIcon(':/images/open.png'),
                "&Open...", self, shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.open)
                
        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)
  
        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QtGui.qApp.aboutQt)
  
        #self.cutAct.setEnabled(False)
        #self.copyAct.setEnabled(False)
        #self.textEdit.copyAvailable.connect(self.cutAct.setEnabled)
        #self.textEdit.copyAvailable.connect(self.copyAct.setEnabled)
    
    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        #self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        #self.fileMenu.addAction(self.saveAct)
        #self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.exitAct)
  
        #self.editMenu = self.menuBar().addMenu("&Edit")
        #self.editMenu.addAction(self.cutAct)
        #self.editMenu.addAction(self.copyAct)
        #self.editMenu.addAction(self.pasteAct)
  
        #self.menuBar().addSeparator()
  
        #self.helpMenu = self.menuBar().addMenu("&Help")
        #self.helpMenu.addAction(self.aboutAct)
        #self.helpMenu.addAction(self.aboutQtAct)
  
    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        #self.fileToolBar.addAction(self.newAct)
        #self.fileToolBar.addAction(self.openAct)
        #self.fileToolBar.addAction(self.saveAct)
  
        #self.editToolBar = self.addToolBar("Edit")
        #self.editToolBar.addAction(self.cutAct)
        #self.editToolBar.addAction(self.copyAct)
        #self.editToolBar.addAction(self.pasteAct)
    def readSettings(self):
        settings = QtCore.QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QtCore.QPoint(200, 200))
        size = settings.value("size", QtCore.QSize(200, 200))
        self.resize(size)
        self.move(pos)
    """
    def createStatusBar(self):
        self.statusBar().showMessage("Ready")
  
  
    def writeSettings(self):
        settings = QtCore.QSettings("Trolltech", "Application Example")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())
  
    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QtGui.QMessageBox.warning(self, "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                    QtGui.QMessageBox.Cancel)
            if ret == QtGui.QMessageBox.Save:
                return self.save()
            elif ret == QtGui.QMessageBox.Cancel:
                return False
        return True
    """    
    def loadFile(self, fileName):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return
  
        inf = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.textEdit.setPlainText(inf.readAll())
        self.textEdit.setReadOnly(True)
        QtGui.QApplication.restoreOverrideCursor()
                
        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)
  
    def saveFile(self, fileName):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Application",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False
  
        outf = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        outf << self.textEdit.toPlainText()
        QtGui.QApplication.restoreOverrideCursor()
  
        self.setCurrentFile(fileName);
        self.statusBar().showMessage("File saved", 2000)
        return True
  
    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        self.setWindowModified(False)
  
        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'ESSA.log'
  
        self.setWindowTitle("%s[*] - Application" % shownName)
  
    def strippedName(self, fullFileName):
        return QtCore.QFileInfo(fullFileName).fileName()
  
  
if __name__ == '__main__':
  
    import sys
  
    app = QtGui.QApplication(sys.argv)
    mainWin = viwerLog()
    mainWin.loadFile('/home/scholl/Dropbox/Spyder/essa/logs/Essa_Alarm.log')
    mainWin.show()
    sys.exit(app.exec_())
  