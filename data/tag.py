# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:50:23 2015

@author: MarcosScholl
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150616-1600"
__status__ = "stable"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data import *
from aware import *
#from aware import _globals
from alarm import *
from logger import *
import time
import datetime

from logger.log import LogCreate
from PyQt4 import QtCore

loggerTag = None
class Tag(Subject):

    def __init__(self, identity = None,
                 value=0, readonly=True, scan=2, providerEnable=False, provider=None,script=None):
        """
        Inicializador - Define os parametros do elo
        identity - Identidade do elo (instancia de Identity)
        attributes - Dicionario onde sao armazenados os atributos da cadeia
                     (instancia de AttributeList)
        params - Relacao de parametros relativos ao elo que sao relevantes para
                 a definicao dos heligiros da cadeia cinematica
        """        
        Subject.__init__(self)
        # Definindo identidade
        self._id = Identity(-1, 'Tag0') if identity is None else identity
        self._id.attach (self)
        self._enable = True
        self._v = value
        self._ro = readonly
        self._provider = provider
        self._providerEnable = providerEnable
        self._bidirectional = False
        self._scan = scan
        self._timeUpdate = int(time.time() * 1000) 
        self._adapters = None
        self._alarms = None
        global loggerTag 
        loggerTag = LogCreate("loggerTag",None,"INFO")
        
        loggerTag.info("New Tag | Name:"+str(self._id.name)+" Id:"+ str(self._id.id)+" | Enable:"+ str(self._enable)+" | ReadyOnly:"+ str(readonly) \
        + " | ProviderEnable:" +str(providerEnable) + " | Scan:" + str(scan) )

        self._alarmPreviousState = False 
        self._alarmActivated = False
        self._alarmEvent = None
        self._alarmGui = False
        self._guiEnable = False
        self._script = script

    """ 
    def __repr__(self):
        return "TAG: {0} - Id {1}".format(self._id.name, self._id.id)
    """
    @property
    def id(self):
        """
        Retorna o id
        """
        return self._id.id
        
    @id.setter    
    def id(self, value):
        """
        Modifica o id
        """
        self._id.id = value

    @property
    def name(self):
        """
        Retorna o name
        """
        return self._id.name
        
    @name.setter    
    def name(self, value):
        """
        Modifica o name
        """
        self._id.name = value
        self.notify(EventUpdated(self))
    
    @property
    def script(self):
        return self._script
    
    @script.setter
    def script(self, script):
        self._script = script
        
    @property
    def description(self):
        """
        Retorna a descricao
        """
        return self._id.description
        
    @description.setter    
    def description(self, value):
        """
        Modifica a descricao
        """
        self._id.description = value
    
    @property    
    def value(self):
        """
        Retorna o valor
        """
        return self._v
        
    @value.setter    
    def value(self, value=0.0):
        """
        Modifica o valor
        """
        #if value >= 200: print "DESLIGA"
        #if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
        if self._script is not None:
            exec(self._script)
        self._v = value
        loggerTag.info(str(self._id.name)+" Update Value: "+ str(self._v))   
        self.notify(EventAlarm(self))
        self.notify(EventComm(self))
        try:
            if self._provider._type != "o": self.notify(EventChanged(self))
        except:
            self.notify(EventChanged(self))   
     
    @property
    def value2(self):
        return self._v 
        
    @value2.setter    
    def value2(self, value=0.0):
        """
        Modifica o valor
        """
        #if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
        self._v = value
        loggerTag.info(str(self._id.name)+" Update Value: "+ str(self._v))   
        self.notify(EventAlarm(self))
        #self.notify(EventComm(self))
        try:
            if self._provider._type != "o": self.notify(EventChanged(self))
        except:
            self.notify(EventChanged(self)) 
            

        
    @property
    def providerEnable(self):
        """
        Retorna se tem provedor
        """
        return self._providerEnable 
        
    @providerEnable.setter    
    def providerEnable(self, boolean):
        """
        Modifica se tem provedor
        """
        self._providerEnable = boolean
        #self.notify(EventUpdated(self))
        
    def addAlarm(self,alarm):
        """
        Modifica alarmers
        """
        self._alarms = alarm
        
    def addAdapter(self,adapter):
        """
        Modifica adaptadores
        """
        self._adapters.append(adapter)
        
        
    @property
    def provider(self):
        return self._provider
    @provider.setter
    
    def provider(self, provider):
        self._provider = provider
        try:
            if provider._type != "i": self.attach(provider)
        except:
            try:
                if provider._registers is not None: self.attach(provider)
            except:
                pass
    def update(self):
        """
        Modifica valor da Tag
        """
        if self._enable:
            if self._providerEnable:
                if self._adapters is not None:
                    for adapter in self._adapters:
                        try:
                            if (adapter._direction == 1):                           
                                """"Not Bidirectional"""
                                try:
                                    value = self._provider.next()
                                    if value is not None:
                                        if self.value != value:
                                            self._timeUpdate = int(time.time() * 1000)
                                            self.value = value
                                            return
                                   
                                except:
                                    try:
                                        """Update Led Warning of Window"""
                                        value = _globals.alarmAlerts
                                        if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
                                            if value is not None:
                                                if self.value != value:
                                                    self._timeUpdate = int(time.time() * 1000)
                                                    self.value = value
                                                    return
                                    except:
                                        print u"Active provider but could not update value! 1"
                                        #elif (self._adapter._direction == "t<->w") or (self._adapter._direction == "t<->w"):
                            elif (adapter._direction == 2):
                                try:
                                    value = self._w.value
                                    if value is not None:
                                        if self.value != value:
                                            self._timeUpdate = int(time.time() * 1000)
                                            self.value = value
                                            return
                                   
                                except:
                                    print self._id.name
                                    print u"Active provider but could not update value! 2"
                            
                            
                            elif (adapter._direction == 3):  
                                """Bidirectional - Analysis any change on widget or Instrument"""
                                try:                           
                                    value = self._provider.next()
                                    if value is not None:                                    
                                        if (self.value != value):
                                            """On change, update"""
                                            self._timeUpdate = int(time.time() * 1000)
                                            self.value2 = value 
                                            
                                    value = adapter._w.value 
                                    try:
                                        #if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
                                        if value is not None:                                    
                                            if (self.value != adapter._w.value):
                                                self._timeUpdate = int(time.time() * 1000)
                                                self.value = adapter._w.value
                                                return
                                    except: 
                                        pass  
                                except:
                                    print u"Bidirectional failed update value."
                            
                            else:
                                #print "adapter._direction=",adapter._direction
                                pass
                        except AttributeError:
                            print "AttributeError"
                            try:
                                """ Simple Tag, sim Direction - AttributeError"""
                                value = self._provider.next()
                                if value is not None:
                                    if self.value != value:
                                        self._timeUpdate = int(time.time() * 1000)
                                        self.value = value
                                 
                            except:
                                print u"Active provider but could not update value! 3"             
                        
                    
            else:
                # direction 4
                if self._adapters is not None:
                    for adapter in self._adapters:
                        if not(adapter._direction == 1) and not(adapter._direction == 4):
                            try:
                                value = adapter._w.value
                                if value is not None:
                                    if not (self.value == value):
                                        self._timeUpdate = int(time.time() * 1000)
                                        self.value = adapter._w.value
                            except AttributeError:
                                try:
                                    #print adapter._direction
                                    #print adapter._w_p
                                    value = adapter._w
                                    #print "V=", value
                                    if value is not None:
                                        if isinstance(value,(str,int,float,complex,bin,long,hex,list,tuple,dict,bytes,bytearray,bool)):
                                            if not (self.value == value):
                                                self._timeUpdate = int(time.time() * 1000)
                                                #self.value = adapter._w
                                except:
                                    pass
                                    
                        #elif (adapter._direction == 2) and adapter._w_p    
                

    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            #print "CHANGEE"
            for adapter in self._adapters:
                if subject == adapter._w:
                     if adapter._w_p == "value":
                         self.value = subject.value 
                     elif adapter._w_p == "text":
                         self.value = subject.text
                     elif adapter._w_p == "state":
                         self.value = subject._enable   
                      
                     elif adapter._w_p == "provider":
                         self.value = subject._providerEnable
    
                     else:
                         self.value = subject.value                        
                         print "WIDGET: No property condition, assumes value."
                             
                     if adapter._t_p == "value":
                         adapter._t.value = self.value 
                     elif adapter._t_p == "text":
                         adapter._t.value = str(self.value)
                     elif adapter._t_p == "state":
                         adapter._t._enable = self.value                       
                     elif adapter._t_p == "provider":
                         adapter._t._providerEnable = self.value
                     else:
                         self.value = self.value
                         print "WIDGET: No property condition, assumes value."
        if (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.name) 

        else:
            ##########################################
            ##########################################
            ##########################################
            #self.value = subject.value 
            pass
        
