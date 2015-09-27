# -*- coding: utf-8 -*-
u"""
event.py - Definição de eventos
--------------------------------------------------------------------------------
Contém as classes Event, EventChanged, EventUpdated
"""

__author__ = "Carlos R. Rocha"
__email__ = "cticarlo@gmail.com"
__version__ = "20150321-1600"
__status__ = "beta"
__license__ = "GPL"


class Event(object):
    u"""
    Event - Classe base de eventos
    ----------------------------------------------------------------------------
    Event é uma mensagem que os Subjects podem enviar aos Listeners para
    notificar estes da ocorrência de um determinado evento, de forma que alguma
    ação seja tomada em resposta a este. Eventos também podem ser usados fora
    desse contexto, para troca de mensagens.
    Em geral, as classes derivadas de Event contém apenas a inicialização,
    o método __repr__ e a propriedade subject
    A ideia é que a própria classe identifique o tipo de ocorrência, ou seja,
    cada tipo de evento corresponderá a uma classe derivada específica.
    """
    def __init__(self, subject=None):
        u"""
        Inicializacao de Event. O único parametro é subject, uma referência
        ao objeto que disparou o evento
        """
        self._subject = subject

    def __repr__(self):
        u"""
        Retorna uma representação em string do evento
        """
        return u"Evento disparado por {0}".format(self._subject)

    @property
    def subject(self):
        u"""
        Retorna o subject que originou o evento,
        se este foi definido na inicialização
        """
        return self._subject


#-------------------------------------------------------------------------------
class EventChanged(Event):
    u"""
    EventChanged - Evento indicativo de que algo mudou de estado/valor
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar uma modificação de estado/valor
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Changed
        """
        return u"{0} foi modificado.".format(self._subject)


#-------------------------------------------------------------------------------
class EventUpdated(Event):
    u"""
    EventUpdated - Evento indicativo de que uma atualização foi realizada
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar que uma atualização foi feita
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)

class EventAlarm(Event):
    u"""
    EventAlarm - Evento indicativo de que um alarme foi ativado
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar que um alarme foi ativado
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)
        
class EventGui(Event):
    u"""
    EventGui - Evento indicativo de que uma janela foi ativada
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar que uma janela foi ativada
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)
        
class EventGuiClose(Event):
    u"""
    EventGuiClose - Evento indicativo de que uma janela foi desativada
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar que uma janela foi desativada
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)      
        
class EventComm(Event):
    u"""
    EventGuiClose - Evento indicativo de que uma comunicacao foi atualizada
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar que uma comunicacao foi atualizada
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)   

class EventWidget(Event):
    u"""
    EventGuiClose - Evento indicativo de que algo mudou de estado/valor
    ----------------------------------------------------------------------------
    Classe derivada de Event, para notificar um widget de que algo mudou de estado/valor
    """
    def __init__(self, subject=None):
        u"""
        Mesma inicialização de Event
        """
        Event.__init__(self, subject)

    def __repr__(self):
        u"""
        Representação string do evento Updated
        """
        return u"{0} foi atualizado".format(self._subject)   
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    print u"Event module"
    print u"Created by {0} ({1})".format(__author__, __email__)
    print u"Version {0} - {1}".format(__version__, __status__)
