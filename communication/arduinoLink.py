# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:11:33 2015

@author: root
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150610-2100"
__status__ = "beta"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
import threading 
lock =  threading.RLock()
import time
class ArduinoLink(Listener):
    def __init__(self, board=None,pin=None):
        Listener.__init__(self)
        self._board = board
        self._pin = pin
        self._type = "o"
        global lock
        
        if self._pin is None:
            self._pin = 'a:0:i'
            
        self._component = self._board.get_pin(self._pin)
        if self._pin.split(":")[2] == "i":
            self._component.enable_reporting()
            self._type = "i"
        
        
        
    def next(self):  
        while self._component.read() is None:
            pass
        self._currentVal = self._component.read()
        if self._currentVal is not None:     
            return self._currentVal
            
    @property            
    def value(self):
        return self._currentVal
    
    @value.setter            
    def value(self, val):
        self._currentVal = val

        try:
            self._board.get_pin(self._pin).write(val)
        except:
            try:
                self._board.digital[int(self._pin.split(":")[1])].write(val)
            except:
                print u"Unable to Burn value in Arduino", "Pin='",self._pin,"'."
        
    def process_event(self, event=None, subject=None):
        #print "Foi Notificado"
        #print "Event", event
        if (isinstance(event, EventComm)):
            try:
                lock.acquire()
                if subject.value is not None:
                    self.value = subject.value
            except:
                lock.release()
        elif (isinstance(event, EventUpdated)):
                 print u"{0} mudou seu nome para {1}.".format(subject, subject.value)
    
        else:
            pass
        