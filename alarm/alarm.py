# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:25:00 2015

@author: scholl
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150606-1800"
__status__ = "beta"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data import *
from aware import *
from aware import _globals
from opengui import PopUp
from logger import *
import time

import threading
lock =  threading.RLock()

from PyQt4 import QtCore, QtGui
alarmLog = None
warningAlarm = None

#from sound import Music

class Alarm(Listener, Subject):
    def __init__ (self, id=0,name="Alarm", tags=None, scan=5, minmin=None,min=-10,max=9999,maxmax=None,lifeGui=5):
        Listener.__init__(self)
        Subject.__init__(self)
        self._id = id
        self._name = name
        self._tags = tags
        self._scan = scan
        self._minmin = minmin
        self._min = min
        self._max = max
        self._maxmax = maxmax
        self._activated = False
        self._guiEnable = False
        self._previousState = False
        global lock
        self.addAlarmOnTag()
        self.alarmGui = PopUp()
        #self._gui = Botao
        self.attach(self.alarmGui)
        self.alarmGui._lifeGui = lifeGui
        self._lifeGui = lifeGui
        self._alarmEvent = None
        self._subjectAlarm = None
        global alarmLog, warningAlarm
                
        

        alarmLog = LogAlarm("logAlarm",None)
        
        #warningAlarm = LogAlarm(logger_name="ESSA_WarningAlarm", log_file="ESSA_WarningAlarm")
        
        for tag in self._tags:
            alarmLog.warning("Alarm Active for:"+ str(tag._id.name))
            alarmLog.warning("instant;tag;event;value;")
        self._alarmLog = alarmLog
        
    def addAlarmOnTag(self):
        for tag in self._tags:
            tag.addAlarm(self)
            tag.attach(self)  
            
            
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventAlarm)):
            
            try:
                lock.acquire()
                self.activateAlarm(subject, subject._id.name,subject.value)
            finally:
                lock.release()
    
    def OpenAlarm(self,subject):
        if subject._guiEnable is True:
            self.notify(EventGui(self))
            pass
        
        
    def activateAlarm(self, subject, name, value):
        subject._alarmEvent = None
        if self._minmin is not None:
            if value <= self._minmin:
                subject._alarmEvent = "minmin"
                subject._alarmActivated = True
                
        if value <= self._min:
            subject._alarmActivated = True
            subject._alarmEvent = "min"
        elif value >= self._max:
            subject._alarmActivated = True
            subject._alarmEvent = "max"
            subject._guiEnable = True
        
        if self._maxmax is not None:
            if value >= self._maxmax:
                subject._alarmActivated = True 
                subject._alarmEvent = "maxmax"
                subject._guiEnable = True
                
        if subject._alarmEvent is None:        
            if subject._alarmPreviousState is True:
                alarmLog.warning(str(name)+";Normalized Alarm;"+str(value)+";")
                _globals.warningAlarm.warning(str(name)+";Normalized Alarm;"+str(value)+";")
                #_globals.sound.stop()
                self.notify(EventGuiClose(self))              
            subject._alarmPreviousState = False 
            subject._alarmActivated = False
            

        if subject._alarmPreviousState is False and subject._alarmActivated is True:
                self._alarmEvent = subject._alarmEvent
                self._subjectAlarm = str(name)
                alarmLog.warning(str(name)+";exceeded "+subject._alarmEvent+";"+str(value)+";") 
                _globals.warningAlarm.warning(str(name)+";exceeded "+subject._alarmEvent+";"+str(value)+";") 
                _globals.alarmAlerts += 1
                self.OpenAlarm(subject)
                subject._alarmPreviousState = True 
                subject._alarmEvent = None
                subject._guiEnable = False
