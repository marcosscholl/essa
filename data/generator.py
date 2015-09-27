# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:19:12 2015

@author: scholl
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150430-2000"
__status__ = "stable"
__license__ = "GPL"


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from math import *
from aware import *

class DPGenerator(Subject):
    def __init__ (self, id, **kwargs):
        self._id = id
        pass
    
class SequenceGenerator (DPGenerator):
    def __init__ (self, id, **kwargs):
        DPGenerator.__init__(self, id, **kwargs)
        if 'min' in kwargs:
            self._min = kwargs['min']
        else:
            self._min = 0.0
        if 'max' in kwargs:
            self._max = kwargs['max']
        else:
            self._max = 10.0            
        if 'step' in kwargs:
            self._step = kwargs['step']
        else:
            self._step = 1.0
            
        self._value = self._min
        self._t = 0.0
            
    def next(self):
        if self._t > self._max:
            self._t = 0
            self._value = 0
           
            
        if self._t == 0.0:
            self._t += self._step
            return self._value
        else:            
            self._value += self._step
            self._t += self._step        
            return self._value
        

        
class SineGenerator (DPGenerator):
    def __init__ (self, id, **kwargs):
        DPGenerator.__init__(self, id, **kwargs)
        if 'min' in kwargs:
            self._min = kwargs['min']
        else:
            self._min = -1.0
        if 'max' in kwargs:
            self._max = kwargs['max']
        else:
            self._max = 1.0            
        if 'step' in kwargs:
            self._step = kwargs['step']
        else:
            self._step = 1.0
        self._value = min
        self._t = 0.0
            
    def next(self):
        self._value = sin(radians(self._t))*(self._max - self._min)/2
        self._t += self._step        
        return self._value
        
class SawToothGenerator (DPGenerator):
    def __init__ (self, id, **kwargs):
        DPGenerator.__init__(self, id, **kwargs)
        if 'min' in kwargs:
            self._min = kwargs['min']
        else:
            self._min = -1.0
        if 'max' in kwargs:
            self._max = kwargs['max']
        else:
            self._max = 1.0            
        if 'step' in kwargs:
            self._step = kwargs['step']
        else:
            self._step = 1.0
        if 'interval' in kwargs:
            self._interval = kwargs['interval']
        else:
            self._interval = 1.0
        self._value = self._min
        self._t = 0.0
            
    def next(self):
        if self._t > self._interval:
            self._t = 0
            self._value = 0
        
        #self._value += self._min 
        self._value += self._min + (self._max-self._min)*self._t/self._interval       
        self._t += self._step        
        return self._value    
