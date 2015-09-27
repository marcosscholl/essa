
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:49:29 2015

@author: MarcosScholl
"""

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150617-1600"
__status__ = "stable"
__license__ = "GPL"


"""
class adaptor(Listenner):
    init(self, x)
    
    def notify():
        
"""
u"""
Listener - Classe base para componentes data-aware
----------------------------------------------------------------------------
Listeners são entidades que são notificadas por instâncias de classes
derivadas de Subject quando algum evento ocorre. Eles devem implementar o
método processEvent() para processar os eventos que recebem.
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data import *
from aware import *
from logger import *
from PyQt4 import QtCore, QtGui

import threading 
lock =  threading.RLock()
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='/home/scholl/Dropbox/Spyder/essa/logs/ESSA_Adapter2.log',
                    filemode='w')     
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger

logging.getLogger('').addHandler(console) 

logger1 = logging.getLogger('AdapterContinuous') 
"""
#from logger.log import LogCreate
logger1 = LogCreate("logger1","ESSA_Adapter")            
class Adapter(Listener):
    def __init__ (self, id, **kwargs):
        Listener.__init__(self)
        global lock
        global console
        global logger1
    
class AdapterContinuous(Adapter):
    def __init__(self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1):
        Adapter.__init__(self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1)
        self._id = id
        self._v = startValue
        self._w = widget
        self._w_p = widgetProprierty
        self._t = tag
        self._t_p = tagProprierty
        self._direction = directionDataFlow #"t->w" "w->t" "t<->w" "w<->t"
        #self.connect()
        
        self._oldValue =  self._v
        self._oldMin = 1
        self._oldMax = 1
        self._newMin = 1
        self._newMax = 1
        self._newValue = 0
        
        
        
        if self._direction == 4: 
            self.setTag(self._w)
        self.setTag(tag)
        
        #if directionDataFlow == "w<->t": tag.attach(widget)
        #logging.info('Adapter Continuous Instanciado')
        
        #print "AdapterTag:", self._t
        #print "AdapterWidget:", self._w
        #print "AdapterDirection:", self._direction
        
    def scale(self, oldMin=1, oldMax=1, newMin=1, newMax=1):
        #self._oldValue = oldValue
        self._oldMin = oldMin
        self._oldMax = oldMax
        self._newMin =newMin
        self._newMax = newMax
        self.change()
        
    def setTag(self, tag):
        if tag._adapters is None:
            tag._adapters = []
            tag.addAdapter(self)
            self.connect()
        else: 
            tag.addAdapter(self)
            self.connect()
        logger1.info("Tag Add in Adapter '"+str(self._id)+"'")

        
    def process_event(self, event=None, subject=None):
        #QtCore.QCoreApplication.processEvents()
        if (isinstance(event, EventChanged)):
            try:
                lock.acquire()
                if self._direction ==1:
                     if subject == self._t:
                         if self._t_p == "value":
                             self.value = subject.value               
                         elif self._t_p == "text":
                             self.value = subject.text
                         elif self._t_p == "state":
                             self.value = subject._enable   
                         elif self._t_p == "provider":
                             #print "subject._providerEnable:", subject._providerEnable
                             self.value = subject._providerEnable
                         else:
                             self.value = subject.value                        
                             print "TAG: Sem Condição de propriedade, assume Value"
                         
                         if self._w_p == "value":
                             try:
                                 self._w.value = self.value 
                             except TypeError:
                                 self._w.setValue(self.value) 
                         elif self._w_p == "text":
                             self._w.value = str(self.value)
                         elif self._w_p == "state":
                             self._w.value = self.value
                             self._w._enable = self.value 
                         elif self._w_p == "provider":
                             self._w.providerEnable = self.value
                         else:
                             self._w.value = self.value
                             print "WIDGET: Sem Condição de propriedade, assume Value"
                         
                         #logger1.info("EventChanged: t->w: Widget "+ self._w.getName()+" new value: "+ str(self.value))       
                elif self._direction == 2:
                     """
                     print "Tag Value:", self._t.value
                     
                     print "subject:", subject
                     print "self._w:",self._w
                     """
                     if subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         elif self._w_p == "self":
                             self.value = subject
                         else:
                             self.value = subject.value                        
                             print "WIDGET: Sem Condição de propriedade, assume Value"
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t.value = self.value
                             self._t._enable = self.value 
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: Sem Condição de propriedade, assume Value" 
                     
                elif self._direction ==4:
                     #print u"\nDireção, Tag -> Tag"
                     if subject == self._t:
                         if self._t_p == "value":
                             self.value = subject.value              
                         elif self._t_p == "text":
                             self.value = subject.text
                         elif self._t_p == "state":
                             self.value = subject._enable    
                         elif self._t_p == "provider":
                             self.value = subject._enable
                         else:
                             self.value = subject.value                        
                             print "TAG: Sem Condição de propriedade, assume Value"
                         

                     if self._w_p == "value":
                         self._w.value = self.value 
                     elif self._w_p == "text":
                         self._w.value = str(self.value)
                     elif self._w_p == "state":
                         self._w.value = self.value
                         self._w._enable = self.value  
                     elif self._w_p == "provider":
                         self._w._providerEnable = self.value
                     else:
                         self._w.value = self.value
                         print "WIDGET: Sem Condição de propriedade, assume Value"  
                     
                elif (self._direction == 3):
                    #print u"\nDireção, Tag <-> Widget or Widget <-> Tag\n"
                    if subject == self._t:    
                        if self._t_p == "value":
                             self.value = subject.value               
                        elif self._t_p == "text":
                             self.value = subject.text
                        elif self._t_p == "state":
                             self.value = subject._enable                       
                        elif self._t_p == "provider":
                             self.value = subject._enable
                        elif self._t_p == "bool":
                             self.value = subject.value
                        else:
                             self.value = subject.value                        
                             print "TAG: Sem Condição de propriedade, assume Value"
                        
                 
                        if self._w_p == "value":
                            self._w.value = self.value 
                        elif self._w_p == "text":
                            self._w.value = str(self.value)
                        elif self._w_p == "state":
                            self._w._enable = self.value  
                        elif self._w_p == "provider":
                            self._w._providerEnable = self.value
                        else:
                            self._w.value = self.value
                            print "WIDGET: Sem Condição de propriedade, assume Value" 
                        
                    
                    elif subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         elif self._w_p == "bool":
                             self.value = subject.value
                         else:
                             self.value = subject.value                        
                             print "WIDGET: Sem Condição de propriedade, assume Value"
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t._enable = self.value  
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: Sem Condição de propriedade, assume Value" 
                         
            finally:
                lock.release()
            
    @property
    def value(self):
        return self._v
        
    @value.setter    
    def value(self, value):
        self._v = value        
        self.change()
        
    def change(self):
        if (self._newMin != 1 and self._oldMax != 1):
            self._oldValue = float(self._v)
            OldRange = (self._oldMax - self._oldMin) 
            if (OldRange == 0): 
                self._v = self._newMin
            else:
                #NewRange = (self._newMax - self._newMin)              
                #self._v = ((((self._oldValue - self._oldMin)*NewRange)/OldRange ) + self._newMin)
                self._v = self.remap(self._v, self._oldMin, self._oldMax, self._newMin, self._newMax)

        elif (self._newMin != 1 and self._newMax != self._oldMax):
            OldRange = (self._oldMax - self._oldMin) 
            if (OldRange == 0): 
                self._v = self._newMin
            else:
                self._v = self.remap(self._v, self._oldMin, self._oldMax, self._newMin, self._newMax)

    
    def remap(self, x, oMin, oMax, nMin, nMax ):  
        #range check
        if oMin == oMax:
            print "Warning: Zero input range"
            return None
    
        if nMin == nMax:
            print "Warning: Zero output range"
            return None
    
        #check reversed input range
        reverseInput = False
        oldMin = min( oMin, oMax )
        oldMax = max( oMin, oMax )
        if not oldMin == oMin:
            reverseInput = True
    
        #check reversed output range
        reverseOutput = False   
        newMin = min( nMin, nMax )
        newMax = max( nMin, nMax )
        if not newMin == nMin :
            reverseOutput = True
    
        portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
        if reverseInput:
            portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)
    
        result = portion + newMin
        if reverseOutput:
            result = newMax - portion
    
        return result
    
    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:###############
            self._t._enable = False
    
    
    def connect(self):
        #print "self._t:", self._t
        self._t.attach(self)
        if ((self._w_p == "state" and self._t_p == "state") or (self._w_p == "provider" and self._t_p == "provider") or (self._w_p == "state" and self._t_p == "provider") or (self._w_p == "provider" and self._t_p == "state")):
            print "CONNECT"
            self._w.attach(self)
        
           
        
class AdapterRange(Adapter):
    def __init__ (self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1):
        Adapter.__init__(self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1)
        self._id = id
        self._v = startValue
        self._w = widget
        self._w_p = widgetProprierty
        self._t = tag
        self._t_p = tagProprierty
        self._direction = directionDataFlow #"t->w" "w->t" "t<->w" "w<->t"
        #self.conect()
        
        if self._direction == 4: 
            print "4"
            self.setTag(self._w)
        else: self.setTag(tag)
        
        self._min = None
        self._ave = None
        self._max = None
        self._lim = None
        self._outputRule = None
        #################
        self._oldValue =  self._v
        self._oldMin = 1
        self._oldMax = 1
        self._newMin = 1
        self._newMax = 1
        self._newValue = 0
        
        
        self._limits = None
        self._rules = None
        
        

    def setTag(self, tag):
        if tag._adapters is None:
            tag._adapters = []
            tag.addAdapter(self)
            self.connect()
        else: 
            tag.addAdapter(self)
            self.connect()
        logger1.info("Tag Add in Adapter '"+str(self._id)+"'")
        
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            try:
                lock.acquire()
                if self._direction ==1:
                     #print "t->w"
  
                     if subject == self._t:
                         if self._t_p == "value":
                             self.value = subject.value               
                         elif self._t_p == "text":
                             self.value = subject.text
                         elif self._t_p == "state":
                             self.value = subject._enable   
                         elif self._t_p == "provider":
                             print "SUJEITO:", subject
                             #print "subject._providerEnable:", subject._providerEnable
                             self.value = subject._providerEnable
                         else:
                             self.value = subject.value                        
                             print "TAG: No property condition, assumes value."
                         
                         if self._w_p == "value":
                             try:
                                 self._w.value = self.value 
                             except TypeError:
                                 self._w.setValue(self.value) 
                         elif self._w_p == "text":
                             self._w.value = str(self.value)
                         elif self._w_p == "state":
                             self._w._enable = self.value 
                         elif self._w_p == "provider":
                             self._w.providerEnable = self.value
                         else:
                             self._w.value = self.value
                             print "WIDGET: No property condition, assumes value."
                         
                         #logger1.info("EventChanged: t->w: Widget "+ self._w.getName()+" new value: "+ str(self.value))       
                elif self._direction == 2:
                     """
                     print "Tag Value:", self._t.value
                     
                     print "subject:", subject
                     print "self._w:",self._w
                     """
                     if subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         else:
                             self.value = subject.value                        
                             print "WIDGET: No property condition, assumes value."
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t._enable = self.value
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: No property condition, assumes value." 
                     

                elif self._direction ==4:
                     #print u"\nDireção, Tag -> Tag"
       
                     if subject == self._t:
                         if self._t_p == "value":
                             self.value = subject.value              
                         elif self._t_p == "text":
                             self.value = subject.text
                         elif self._t_p == "state":
                             self.value = subject._enable    
                         elif self._t_p == "provider":
                             self.value = subject._enable
                         else:
                             self.value = subject.value                        
                             print "TAG: No property condition, assumes value."
                         
                     
                     if self._w_p == "value":
                         self._w.value = self.value 
                     elif self._w_p == "text":
                         self._w.value = str(self.value)
                     elif self._w_p == "state":
                         self._w._enable = self.value  
                     elif self._w_p == "provider":
                         self._w._providerEnable = self.value
                     else:
                         self._w.value = self.value
                         print "WIDGET: No property condition, assumes value."  
                     
                elif (self._direction == 3):
                    #print u"\nDireção, Tag <-> Widget or Widget <-> Tag\n"
                   
                    
                    if subject == self._t:        
                        if self._t_p == "value":
                             self.value = subject.value               
                        elif self._t_p == "text":
                             self.value = subject.text
                        elif self._t_p == "state":
                             self.value = subject._enable                       
                        elif self._t_p == "provider":
                             self.value = subject._enable
                        elif self._t_p == "bool":
                             self.value = subject.value
                        else:
                             self.value = subject.value                        
                             print "TAG: No property condition, assumes value."
                        
                 
                        if self._w_p == "value":
                            self._w.value = self.value 
                        elif self._w_p == "text":
                            self._w.value = str(self.value)
                        elif self._w_p == "state":
                            self._w._enable = self.value  
                        elif self._w_p == "provider":
                            self._w._providerEnable = self.value
                        else:
                            self._w.value = self.value
                            print "WIDGET: No property condition, assumes value." 
                        
                    
                    elif subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         elif self._w_p == "bool":
                             self.value = subject.value
                         else:
                             self.value = subject.value                        
                             print "WIDGET: No property condition, assumes value."
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t._enable = self.value  
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: No property condition, assumes value." 
                         
            finally:
                lock.release()
        
    @property
    def value(self):
        return self._v
        
    @value.setter    
    def value(self, value):
        if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
            self._v = value
            self.change()
            if self._outputRule is not None:
                self._v = self.rules()
        
    def change(self):        
        OldRange = (self._oldMax - self._oldMin)    
        if (OldRange == 0): 
            self._newValue = self._newMin
        else:
            NewRange = (self._newMax - self._newMin)             
            self._v = (((self._oldValue - self._oldMin)*NewRange)/OldRange ) + self._newMin  
        
    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:
            self._t._enable = False
            
    def connect(self):
        self._t.attach(self)
        if ((self._w_p == "state" and self._t_p == "state") or (self._w_p == "provider" and self._t_p == "provider") or (self._w_p == "state" and self._t_p == "provider") or (self._w_p == "provider" and self._t_p == "state")):
            self._w.attach(self)
            print "attach"
            
    def scale(self, oldValue=0, oldMin=1, oldMax=1, newMin=1, newMax=1):
        self._oldValue = oldValue
        self._oldMin = oldMin
        self._oldMax = oldMax
        self._newMin =newMin
        self._newMax = newMax
        self.change()
    
    def condition(self, outputRule):
        self._outputRule = outputRule    
        self._rules = outputRule
        
    def limits(self, **kwargs):
        self._limits = kwargs
        if 'minimum'in kwargs:
            self._min = kwargs['minimum']
        if 'average'in kwargs:
            self._ave = kwargs['average']
        if 'maximum'in kwargs:
            self._max = kwargs['maximum']
        if 'limit'in kwargs:
            self._lim = kwargs['limit']
    
    def rules(self):
        cond = None
        if self._lim is not None:
            if self._lim >= self._v :               
                cond = ("Cond4")
        if self._max is not None:
            if self._max >= self._v:               
                cond = ("Cond3")
        if self._ave is not None:
            if self._ave >= self._v:               
                cond = ("Cond2")        
        if self._min is not None:
            if self._v < self._min:               
                cond = ("Cond1")
            
        if self._min is not None and self._ave is not None:
            if self._v >= self._min and self._v < self._ave:                
                cond = ("Cond2")
                
        if self._ave is not None and self._max is not None:
            if self._v >= self._ave and self._v < self._max:
                cond = ("Cond3")
                
        if self._max is not None and self._lim is not None:
            if self._v >= self._max and self._v <= self._lim:             
                cond = ("Cond4")
                
        try:
            """if value is Boolean, min=0, ave=1"""
            if self._max is not None:
                if self._max == self._v:               
                    cond = ("Cond3")
                    
            if self._ave is not None:
                if self._v == self._ave:
                    cond = ("Cond2")
                #print "True"        
            if self._min is not None:
                if self._v == self._min:
                    cond = ("Cond1")
                #print "False"   
        except:
            pass
        
        if cond is not None:
            return self._outputRule.get(cond)
            

class AdapterDiscret(Adapter):
    def __init__ (self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1, valueTrue=None, valueFalse=None):
        Adapter.__init__(self, id=0, startValue=0, widget=None, widgetProprierty="value", tag=None,  tagProprierty="value", directionDataFlow=1,valueTrue=None, valueFalse=None)
        self._id = id
        self._v = startValue
        self._w = widget
        self._w_p = widgetProprierty
        self._t = tag
        self._t_p = tagProprierty
        self._direction = directionDataFlow #"t->w" "w->t" "t<->w" "w<->t"
        self._valueTrue = valueTrue
        self._valueFalse = valueFalse
        
        #if self._direction == 4: self.setTag(self._w)
        self.setTag(tag) 
        

    def setTag(self, tag):
        if tag._adapters is None:
            tag._adapters = []
            tag.addAdapter(self)
            self.connect()
        else: 
            tag.addAdapter(self)
            self.connect()
        logger1.info("Tag Add in Adapter '"+str(self._id)+"'")
        
            
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            try:
                lock.acquire()
                if self._direction ==1:
                     #print "t->w"    
                     if subject == self._t:
                         if self._t_p == "value":
                             value = subject.value               
                         elif self._t_p == "text":
                             value = subject.text
                         elif self._t_p == "state":
                             value = subject._enable   
                         elif self._t_p == "provider":
                             value = subject._providerEnable
                         else:
                             value = subject.value                        
                             print "TAG: No property condition, assumes value."
                         #print "##"
                         #print "1 value:", value
                         #print self.value
                         #print "##"
                         if self.value != value and value is not None:
                             self.value = (value)
                             
                         if self._w_p == "value":
                             try:
                                 self._w.value = self.value 
                             except TypeError:
                                 self._w.setValue(self.value) 
                         elif self._w_p == "text":
                             self._w.value = str(self.value)
                         elif self._w_p == "state":
                             self._w._enable = self.value 
                         elif self._w_p == "provider":
                             self._w.providerEnable = self.value
                         else:
                             self._w.value = self.value
                             print "WIDGET: No property condition, assumes value."
                         
                         #logger1.info("EventChanged: t->w: Widget "+ self._w.getName()+" new value: "+ str(self.value))       
                elif self._direction == 2:
                     if subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         else:
                             self.value = subject.value                        
                             print "WIDGET: No property condition, assumes value."
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t._enable = self.value  
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: No property condition, assumes value." 
                     
                elif self._direction ==4:
                     #print u"\nDireção, Tag -> Tag"
        
                     if subject == self._t:
                         if self._t_p == "value":
                             self.value = subject.value              
                         elif self._t_p == "text":
                             self.value = subject.text
                         elif self._t_p == "state":
                             self.value = subject._enable    
                         elif self._t_p == "provider":
                             self.value = subject._enable
                         else:
                             self.value = subject.value                        
                             print "TAG: No property condition, assumes value."
                         
                     
                     if self._w_p == "value":
                         self._w.value = self.value 
                     elif self._w_p == "text":
                         self._w.value = str(self.value)
                     elif self._w_p == "state":
                         self._w._enable = self.value  
                     elif self._w_p == "provider":
                         self._w._providerEnable = self.value
                     else:
                         self._w.value = self.value
                         print "WIDGET: No property condition, assumes value."  
                     
                elif (self._direction == 3):
                    #print u"\nDireção, Tag <-> Widget or Widget <-> Tag\n"
                    
                    if subject == self._t:        
                        if self._t_p == "value":
                             self.value = subject.value               
                        elif self._t_p == "text":
                             self.value = subject.text
                        elif self._t_p == "state":
                             self.value = subject._enable                       
                        elif self._t_p == "provider":
                             self.value = subject._enable
                        elif self._t_p == "bool":
                             self.value = subject.value
                        else:
                             self.value = subject.value                        
                             print "TAG: No property condition, assumes value."
                        
                 
                        if self._w_p == "value":
                            self._w.value = self.value 
                        elif self._w_p == "text":
                            self._w.value = str(self.value)
                        elif self._w_p == "state":
                            self._w._enable = self.value  
                        elif self._w_p == "provider":
                            self._w._providerEnable = self.value
                        else:
                            self._w.value = self.value
                            print "WIDGET: No property condition, assumes value." 
                        
                    
                    elif subject == self._w:
                         if self._w_p == "value":
                             self.value = subject.value                 
                         elif self._w_p == "text":
                             self.value = subject.text
                         elif self._w_p == "state":
                             self.value = subject._enable
                         elif self._w_p == "provider":
                             self.value = subject._enable
                         elif self._w_p == "bool":
                             self.value = subject.value
                         else:
                             self.value = subject.value                        
                             print "WIDGET: No property condition, assumes value."
                         
                             
                         if self._t_p == "value":
                             self._t.value = self.value 
                         elif self._t_p == "text":
                             self._t.value = str(self.value)
                         elif self._t_p == "state":
                             self._t._enable = self.value  
                         elif self._t_p == "provider":
                            self._t._providerEnable = self.value    
                         else:
                             self._t.value = self.value
                             print "WIDGET: No property condition, assumes value." 
                         
            finally:
                lock.release()
    
    def change(self, val):
        if self._v == True:
            return self._valueTrue
        elif self._v == False:
            return self._valueFalse
        
    @property
    def value(self):
        
        if self._v == True:
            return self._valueTrue
        elif self._v == False:
            return self._valueFalse
        
        #return self._v
        
    @value.setter    
    def value(self, value):
        self._v = value
          
        
    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:
            self._t._enable = False
            
    def connect(self):
        self._t.attach(self)
        """
        if self._direction == 3:
            self._w.attach(self)
        """
        if ((self._w_p == "state" and self._t_p == "state") or (self._w_p == "provider" and self._t_p == "provider") or (self._w_p == "state" and self._t_p == "provider") or (self._w_p == "provider" and self._t_p == "state")):
            self._w.attach(self)
      