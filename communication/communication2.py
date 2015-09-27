# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:18:48 2015

@author: root
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *

from pyfirmata import Arduino, util
from PyQt4.QtCore import *
from PyQt4 import QtCore

import threading
from threading import Thread
lock =  threading.RLock()
"""
'a' analog pin     Pin number   'i' for input
'd' digital pin    Pin number   'o' for output
                                'p' for pwm (Pulse-width modulation)
"""
class COMM(Thread,Listener):
    def threaded(fn):
        def wrapper(*args, **kwargs):    
            threading.Thread(target=fn, args=args, kwargs=kwargs).start()
        return wrapper
    
    
    def __init__(self, port=None, pin=None):
        # Pyfirmata code
        Thread.__init__(self)
        Listener.__init__(self)
        self._port = port
        self._pin = pin
        self._component = None
        self._iterator = None
        self._currentVal = None
        self._previousVal = None
        global lock
        self.createCom()
    
    def createCom(self):
        print "create"
        if self._port is None:
            self._port = '/dev/ttyACM0'

        if self._pin is None:
            self._pin = 'a:0:i'
        
        self._board = Arduino(self._port)
        self._component = self._board.get_pin(self._pin)
        self._component.enable_reporting()
        
        self._iterator = util.Iterator(self._board)
        self._iterator.start()

    def cleanup(self):
        self._board.exit()
        
    
    def next(self):
        while self._component.read() is None:
            pass
        self._currentVal = self._component.read()
        if self._currentVal is not None:
            if self._currentVal != self._previousVal:
                self._previousVal = self._currentVal
                #self.notify()
            return self._previousVal
    @property            
    def value(self):
        return self._currentVal
    
    @value.setter            
    def value(self, val):
        self._currentVal = val
        
    def process_event(self, event=None, subject=None):
        #print "Foi Notificado"
        #print "Event", event
        if (isinstance(event, EventComm)):
            try:
                lock.acquire()
                print "ATUALIZANDO"
                if subject.value is not None:
                    self.value = subject.value
            except:
                lock.release()
        elif (isinstance(event, EventUpdated)):
                 print u"{0} mudou seu nome para {1}.".format(subject, subject.value)
    
        else:
            print u"Outro evento aleatório"
        
    
    