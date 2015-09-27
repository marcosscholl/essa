# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:50:23 2015

@author: MarcosScholl
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data import *
from aware import *
import time
import datetime

from PyQt4 import QtCore


"""
class Tag(Subject):
    def __init__(self):
        #Thread.__init__(self)
        Subject.__init__(self)
        self.attribute = Atrribute()
        self.info = Identity()
"""
u"""
Listener - Classe base para componentes data-aware
----------------------------------------------------------------------------
Listeners são entidades que são notificadas por instâncias de classes
derivadas de Subject quando algum evento ocorre. Eles devem implementar o
método processEvent() para processar os eventos que recebem.
"""        
"""
Subject - Classe base de elementos observáveis
----------------------------------------------------------------------------
Subjects são entidades observáveis que em determinadas operações podem
afetar o comportamento de outras entidades. Nesse caso, elas podem notificar
as interessadas através do envio de Events com o metodo notify().
Os observadores (Listeners) devem se vincular aos Subjects através do método
attach(). Se não quiser mais receber notificações, pode se desvincular do
Subject atraves do método detach().
"""
class Tag(Subject):
#class Link(Subject):
    """
    Define os parametros e identidade de um elo da cadeia cinemática
    Descende de Subject para ser data-aware
    Os elos componentes estruturais da cadeia cinematica. Alem disso, varios
    parametros que as proprias juntas utilizam na definicao de seus heligiros
    sao inerentes as juntas que sao vinculadas por eles. 
    """
    #changed = EventChanged()

    def __init__(self, identity = None,
                 value=0, readonly=True):
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
        self._provider = None
        self._providerEnable = False
        self._bidirectional = False
        self._scan = 0.5
        self._timeUpdate = int(time.time() * 1000) 
        self._adapter = None
        
     
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
        self._v = value
        self.notify(EventChanged(self))
        
    @property
    def providerEnable(self):
        return self._providerEnable 
        
    @providerEnable.setter    
    def providerEnable(self, boolean):
        self._providerEnable = boolean
        #self.notify(EventUpdated(self))
        
    def update(self):
        if self._enable:
            """
            self.value(self._provider.next())
            self._timeUpdate = int(time.time() * 1000) 
            self._adapter._oldValue = self._v
            self._adapter.change()
            """
            if self._providerEnable:
                self.value = self._provider.next()
                self._timeUpdate = int(time.time() * 1000)
               
                if not((self._adapter._oldMax - self._adapter._oldMin) == 0):  
                    self._adapter._oldValue = self._v
                    self._adapter.change()
                
                    
            else:
                #print "Provedor DESATIVADO"
                #print self._adapter._w_p
                #if self._adapter._t_p == "provider":
                    #print self.value
                if not(self._adapter._direction == "t->w"):
                    if not (self.value == self._adapter._w.value):
                        #print "self.value:", self.value
                        #print "self._adapter._w.value:", self._adapter._w.value
                        self.value = self._adapter._w.value
                        #print "self._adapter._w:",self._adapter._w
                        self._timeUpdate = int(time.time() * 1000) 
                else:
                    #print "self.value:", self.value
                    #print "self._adapter._direction=", self._adapter._direction                    
                    #print "self._adapter._w.value:", self._adapter._w.value
                    #print "self._adapter._w:",self._adapter._w
                    #print "self._adapter._t.value:", self._adapter._w.value
                    #print "self._adapter._t:",self._adapter._w
                    #time.sleep(1)
                    pass
                    
            
            
            """
            if self._bidirectional:
                for widget in self._adapter._w:
                    if not (self.value == widget.value):
                        self.value(widget.value)
                        self._timeUpdate = int(time.time() * 1000) 
            """
            """
            if not (self.value == self._adapter._w.value):
                self.value(self._adapter._w.value)
                self._timeUpdate = int(time.time() * 1000) 
            """
                
    def update2(self):
        #print "Tag Update22"
        #print "TAG.VALUE:|", self.value(), "|   ADAPTER.VALUE", self._adapter.value()
        """
        self.value(self._adapter.value)
        self._timeUpdate = int(time.time() * 1000) 
        #self._adapter._oldValue = self._v
        self._adapter._v = self._adapter.value
        """
        if self._enable:
            if not (self.value == self._adapter._w.value):
                self.value = self._adapter._w.value
                self._timeUpdate = int(time.time() * 1000) 
            #print "Atualizou com o Valor:",self.value
    
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            print "ENTREI AQUI"
            if subject == self._adapter._w:
                 if self._adapter._w_p == "value":
                     self.value = subject.value 
                 elif self._adapter._w_p == "text":
                     self.value = subject.text
                 elif self._adapter._w_p == "state":
                     self.value = subject._enable   
                  
                 elif self._adapter._w_p == "provider":
                     self.value = subject._providerEnable

                 else:
                     self.value = subject.value                        
                     print "WIDGET: Sem Condição de propriedade, assume Value"
                         
                 if self._adapter._t_p == "value":
                     self._adapter._t.value = self.value 
                 elif self._adapter._t_p == "text":
                     self._adapter._t.value = str(self.value)
                 elif self._adapter._t_p == "state":
                     self._adapter._t._enable = self.value                       
                 elif self._adapter._t_p == "provider":
                     self._adapter._t._providerEnable = self.value
                 else:
                     self.value = self.value
                     print "WIDGET: Sem Condição de propriedade, assume Value"
        if (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.name) 

        else:
            print u"Outro evento aleatório"


"""
if __name__ == "__main__":
    
    
    from gerador import Gerador
    from geradores01 import *
   
 
    tag2 = Tag(Identity(10, 'Tag10'), 100, True)
     
    inspetor = Observador()
    tag2.attach(inspetor)  
    #tag.dataProvider(driverModbus,250)
    #tag.dataProvider(GeradorRandom(10,1000,250))
    print tag2.__repr__
    

    
    tag2.dataProvider(SequenceGenerator(1,min=0,max=10,step=1),0.5)
    
    print tag2._v
    
    print tag2._v
"""    
   
    
