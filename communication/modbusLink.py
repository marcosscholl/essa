# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:40:43 2015

@author: root
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150611-1700"
__status__ = "stable"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
import threading 
lock =  threading.RLock()


class ModbusLink(Listener):    

    def __init__(self, name="ModbusLink", board=None,register=1,type="register"):
        Listener.__init__(self)
        self._name = name
        self._board = board
        self._register = register
        self._type = type
        
        self._currentVal = None
        self._previusVal = None
        global lock
        
        
        if self._type == "register":    
            self._instrumentRead = self._board.read_register    
        elif self._type == "bit":
            self._instrumentRead = self._board.read_bit
        elif self._type == "long":
            self._instrumentRead = self._board.read_long
        elif self._type == "float":
            self._instrumentRead = self._board.read_float
        elif self._type == "string":
            self._instrumentRead = self._board.read_string
        elif self._type == "registers":
            self._instrumentRead = self._board.read_registers
        else:
            self._instrumentRead = self._board.read_register
            
            
        if self._type == "register":    
            self._instrumentWrite = self._board.write_register    
        elif self._type == "bit":
            self._instrumentWrite = self._board.write_bit
        elif self._type == "long":
            self._instrumentWrite = self._board.write_long
        elif self._type == "float":
            self._instrumentWrite = self._board.write_float
        elif self._type == "string":
            self._instrumentWrite = self._board.write_string
        elif self._type == "registers":
            self._instrumentWrite = self._board.write_registers
        else:
            self._instrumentWrite = self._board.write_register
        
               
    def next(self):
        
        
        while self._instrumentRead(self._register) is None:
            pass
        self._currentVal = self._instrumentRead(self._register)
        if self._currentVal is not None:   
            if self._currentVal is not self._previusVal:
                self._previusVal = self._currentVal
                return self._currentVal
            
    @property            
    def value(self):
        return self._currentVal
    
    @value.setter            
    def value(self, val):
        self._currentVal = val      
        try: 
            self._instrumentWrite(self._register, val) 
        except:
            #print u"Unable to Burn value in Modbus", "Register='",self._name,"'."
            pass
        
    def process_event(self, event=None, subject=None):

        if (isinstance(event, EventComm)):
            try:
                lock.acquire()
                if subject.value is not None:
                    if self.value != subject.value:
                        self.value = subject.value
            except:
                lock.release()
        elif (isinstance(event, EventUpdated)):
                 print u"{0} mudou seu nome para {1}.".format(subject, subject.value)
    
        else:
            #print u"Outro evento aleatório"
            pass

