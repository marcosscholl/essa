# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:47:24 2015

@author: root
"""


__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150618-1000"
__status__ = "beta"
__license__ = "GPL"

#from thread import 

import sys, os, threading
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
from communication import *
from aware import _globals
from PyQt4 import QtGui
class ESSA():
    #global threadTeste
    def __init__(self,pathConfigXML):
        self.sys = sys
        self.app = QtGui.QApplication(self.sys.argv)
        self.MainWindow = QtGui.QMainWindow()
        self.pathConfigXML = pathConfigXML
        
        self.create()
    
    def create(self):
        
        _window, _scan, _comms, _tags,_adapter, _alarms = ESSAParser(self.pathConfigXML).create
        
        _globals.fileConfigPath = self.pathConfigXML
        #_adapter.append()
        
        ProcessUi(_globals.pathInstall, _window)
        exec("from config.{} import *".format(_window[:-3]))
        ui = Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        

        #scan = Scan(float(_scan))
        scan = Scan(1)
        
        TagLed = Tag(Identity(-15, 'Tag Led Warning of Window'))
        TagLed._scan = 1
        adapterLed = AdapterRange(0,0,ui.led ,"value", TagLed, "value", 1)       
        adapterLed.limits(minimum=0,average=1)
        adapterLed.condition({"Cond1":"Normal","Cond2":"Emergency"}) 
        TagLed.provider = _globals.alarmAlerts
        TagLed.providerEnable = True
        
        scan.add(TagLed)
        
        for comm in _comms:     
            try:
                exec(comm)  
            except NameError:
                print u"Error in COMM definition."
                raise
        
        for tag in _tags:   
            try:
                exec(tag)  
                if not ('provider' in tag):
                    tag_ = tag[:len(tag)-1].split(",")
                    tag_ = (tag_[1]).replace(")","").replace("'","")
                    if not ('pin' in tag_) and not ('commModbus' in tag_): 
                        scan.add(eval(tag_))
            except NameError:
                print u"Error in Tag definition."
                raise
                    
        for adapter in _adapter:
            try:
                
                try:
                    exec(adapter)
                except AttributeError:
                    try:
                        """Tag is with Widget"""
                        tag = adapter.split(',')[2][3:]
                        adpt = adapter.split(',')
                        adpt[2] = tag
                        adpt = str(adpt)[1:-1]
                        adpt = adpt.replace("u'",'').replace("'",'')
                        exec(adpt)
                    except:
                        pass
            except NameError:
                
                print u"Error in Adapter definition."
                raise
                
        for alarm in _alarms:
            exec(alarm)   
        
        
        _globals.objThread = scan
        _globals.objThread.start()
        _globals.objThread.pause()
        self.MainWindow.show()
        self.sys.exit(self.app.exec_())
        
    def exit(self):
        self.app.exit()
        
    def start():
        _globals.objThread.resume()
    
    
def stop():
    _globals.objThread.stop()
        
