# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:49:29 2015

@author: MarcosScholl
"""


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

from aware import *
            
class Adapter(Listener):
    def __init__ (self, id, **kwargs):
        Listener.__init__(self)
    
    
    def init(self):
        for widget in self._w:
            try:
                widget.attach(self)
            except AttributeError:
                pass
            self._t.attach(self)


class AdapterContinuous(Adapter):
    def __init__ (self, id=0, startValue=0, widget=None, tag=None, directionDataFlow="t->w", proprierty="value"):
        Adapter.__init__(self, id=0, value=0, widget=None, tag=None)
        self._id = id
        self._v = startValue
        self._w = widget
        self._t = tag
        self._direction = directionDataFlow #"t->w" "w->t" "t<->w" "w<->t"
        self._proprierty = proprierty
        self.conect()
        
        self._oldValue =  self._v
        self._oldMin = 1
        self._oldMax = 1
        self._newMin = 1
        self._newMax = 1
        self._newValue = 0
        
    def scale(self, oldValue=0, oldMin=1, oldMax=1, newMin=1, newMax=1):
        self._oldValue = oldValue
        self._oldMin = oldMin
        self._oldMax = oldMax
        self._newMin =newMin
        self._newMax = newMax
        self.change()
        
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            if self._direction =="t->w":
                 print u"\nDireção, Tag -> Widget"
                 if subject == self._t:
                     if self._proprierty == "value":
                         self.value = subject.value                        
                         print "self.Value:", subject.value,"\n"
                         
                         self._w.setValue(self.value)                       
                     elif self._proprierty == "text":
                         self.value = subject.text
                         self._w.setText(self.value)
                     else:
                         self.value = subject.value
                         self._w.setValue(self.value)
                         print "Sem Condição de propriedade, assume Value"
                    
            elif self._direction =="w->t":
                 
                 print u"\nDireção, Widget -> Tag\n"
                 
                 print "Tag Value:", self._t.value
                 
                 print "subject:", subject
                 print "self._w:",self._w
                 """
                 if subject == self._w:
                     print "Widget"
                     if self._proprierty == "value":                       
                         print "self.Value:", subject.value,"\n"
                         self.value = subject.value
                         self._t.value =self.value
                         
                     elif self._proprierty == "text":
                         self.value = subject.text
                         self._t.setText(self.value)
                     else:
                         self.value = subject.value
                         self._t.value(self.value)
                         print "Sem Condição de propriedade, assume Value"
                    """
            elif self._direction =="t->t":
                 print u"\nDireção, Tag -> Tag"
                 if subject == self._t:
                     if self._proprierty == "value":
                         self.value = subject.value                        
                         print "self.Value:", subject.value,"\n"
                         
                         self._w.value = self.value                       
                     elif self._proprierty == "text":
                         self.value = subject.text
                         self._w.setText(self.value)
                     else:
                         self.value = subject.value
                         self._w.setValue(self.value)
                         print "Sem Condição de propriedade, assume Value"
                         
            elif (self._direction == "t<->w" or self._direction == "w<->t"):
                print u"\nDireção, Tag <-> Widget or Widget <-> Tag\n"
                if subject == self._t:
                     print "Sujeito é a Tag\n"
                     if self._proprierty == "value":
                         self.value = subject.value
                         self._w.setValue(self.value)
                         
                     elif self._proprierty == "text":
                         self.value = subject.text
                         self._w.setText(self.value)
                     else:
                         self.value = subject.value
                         self._w.setValue(self.value)
                         print "Sem Condição de propriedade, assume Value"
                elif subject == self._w:
                     print "Sujeito é o Widget\n"
                     if self._proprierty == "value":
                         self.value = subject.value
                         self._t.value(self.value)
                         
                     elif self._proprierty == "text":
                         self.value = subject.text
                         self._w.setText(self.value)
                     else:
                         self.value = subject.value
                         self._w.setValue(self.value)
                         print "Sem Condição de propriedade, assume Value"
                
            
        elif (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.nome)
            #dial.setValue(subject.valor)
        else:
            print u"Outro evento aleatório"
        
    @property
    def value(self):
        return self._v
        
    @value.setter    
    def value(self, value):
        self._v = value
        self.change()
        
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
        else:###############
            self._t._enable = False
    def conect(self):
        self._t.attach(self)
        

        
class AdapterBidirectional(Adapter):
    def __init__ (self, id=0, value=0, widget=None, tag=None):
        Adapter.__init__(self, id=0, value=0, widget=None, tag=None)
        self._id = id
        self._v = value
        self._w = widget
        self._t = tag
        self._nv = widget._state
        
    
    def value(self):
        return self._nv
    
    def change(self):
        pass
        
    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:
            self._t._enable = False

    
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            if (subject == self._w):
                self._t.value(self._w._state)
                print "\nEvento Veio do Widget!  Valor=", self._w._state, " | ValorTag=", self._t._v  
                self.verifyState(self._w._state)
                
                
            elif subject == self._t:
                self._w._state = self._t._v
                print "\nEvento Veio da TAG!   Valor=", self._t._v, " | ValorWidget=", self._w._state
                self.verifyState(self._t._enable)
                
            """
            self._v = subject._v
            self.change()
            print u"ADAPTER Bidirectional\n{0} mudou seu valor para {1}.".format(subject, self.value)        
            self._w.setValue(self.value())
            """
           
            
        elif (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.value)
            #dial.setValue(subject.valor)
        else:
            print u"Outro evento aleatório"
            
            
            
class AdapterScale2(Adapter):
    def __init__ (self, id=0, oldValue=0, oldMin=0, oldMax=0, newMin=0, newMax=0,  widget=None, tag=None):
        Adapter.__init__(self, id=0, oldValue=0, oldMin=0, oldMax=0, newMin=0, newMax=0,  widget=None, tag=None)
        self._id = id        
        self._oldValue = oldValue
        self._oldMin = oldMin
        self._oldMax = oldMax
        self._newMin =newMin
        self._newMax = newMax
        self._newValue = 0
        self._w = widget
        self._t = tag
        self.change()
        self.init()
        
    @property    
    def value(self):
        return self._newValue
        
    @value.setter    
    def value(self, value):
        self._newValue = value        
        self.change()
        
    def change(self):        
        OldRange = (self._oldMax - self._oldMin)    
        if (OldRange == 0): 
            self._newValue = self._newMin
        else:
            NewRange = (self._newMax - self._newMin)   
            self._newValue = (((self._oldValue - self._oldMin)*NewRange)/OldRange ) + self._newMin  
    
    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:
            self._t._enable = False    

            
        

                  
class AdapterBidirect(Adapter):
    def __init__ (self, id=0, widget=None, tag=None):
        Adapter.__init__(self, id=0,widget=None, tag=None)
        self._id = id        
        self._newValue = 0
        self._w = widget
        self._t = tag

        
    @property    
    def value(self):
        return self._newValue
        
    @value.setter    
    def value(self, value):
        self._newValue = value

    def verifyState(self, state):
        if state:
            self._t._enable = True
        else:
            self._t._enable = False    

    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            if subject == self._t:
                self.value = (subject.value)
                #self.change()
                #print u"ADAPTER111\n{0} mudou seu valor para {1}.".format(subject, self.value)           
                self._w.setValue(self.value)
                                           
            try:               
                if self._t._bidirectional :
                    if (subject == self._w):
                        self._t.value(self._w._state)
                        #print "\nEvento Veio do Widget!  Valor=", self._w._state, " | ValorTag=", self._t._v  
                        self.verifyState(self._w._state)
                        
                        
                    elif subject == self._t:
                        self._w._state = self._t._v
                        #print "\nEvento Veio da TAG!   Valor=", self._t._v, " | ValorWidget=", self._w._state
                        self.verifyState(self._t._enable)
            except AttributeError:
                    self._v = subject._v         
                    self._w.setValue(self.value)
        elif (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.nome)
            #dial.setValue(subject.valor)
        else:
            print u"Outro evento aleatório" 
            
            
            
class AdapterFloat(Adapter):
    def __init__ (self, id=0, value=0, widget=None):
        Adapter.__init__(self, id=0, value=0, widget=None)
        self._id = id
        self._v = value
        self._w = widget
        self.change()
   
    @property    
    def value(self):
        return self._nv
        
    def change(self):
        self._nv = float(self._v)
        #self.notify()
    
        
    """
    def notify(self):
        #tag.value > widget.value
        print "Notifica"
        self._w.setValue(self._nv)
    """
    
    
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            self._v = subject._v
            self.change()
            print u"ADAPTER\n{0} mudou seu valor para {1}.".format(subject, self.value)        
            self._w.setValue(self.value)
            
           
            
        elif (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.nome)
            #dial.setValue(subject.valor)
        else:
            print u"Outro evento aleatório"

class AdapterScale(Adapter):
    def __init__ (self, id=0, oldValue=0, oldMin=0, oldMax=0, newMin=0, newMax=0, widget=None):
        Adapter.__init__(self, id=0, oldValue=0, oldMin=0, oldMax=0, newMin=0, newMax=0, widget=None)
        self._id = id        
        self._oldValue = oldValue
        self._oldMin = oldMin
        self._oldMax = oldMax
        self._newMin =newMin
        self._newMax = newMax
        self._newValue = 0
        self._w = widget
        self.change()
        
    @property    
    def value(self):
        return self._newValue
        
    def change(self):           
        OldRange = (self._oldMax - self._oldMin)    
        if (OldRange == 0): 
            self._newValue = self._newMin
        else:
            NewRange = (self._newMax - self._newMin)   
            self._newValue = (((self._oldValue - self._oldMin)*NewRange)/OldRange ) + self._newMin  
        
    def process_event(self, event=None, subject=None):
        if (isinstance(event, EventChanged)):
            print "(subject.value)", subject._v
            self._v = subject._v
            print "self._v:", self._v
            self.change()
            print u"ADAPTER\n{0} mudou seu valor para {1}.".format(subject, self.value)           
            self._w.setValue(self.value)
           
        elif (isinstance(event, EventUpdated)):
            print u"{0} mudou seu nome para {1}.".format(subject, subject.nome)
            #dial.setValue(subject.valor)
        else:
            print u"Outro evento aleatório"      
"""
a = 10
b = AdapterFloat(1,a,).value()
print b
print type(b)
"""