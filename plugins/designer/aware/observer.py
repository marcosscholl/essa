# -*- coding: utf-8 -*-
u"""
observer.py - Implementação do padrão de projeto Observer
--------------------------------------------------------------------------------
Contém as classes Subject, Listener, ObserverError
"""

__author__ = "Carlos R. Rocha"
__email__ = "cticarlo@gmail.com"
__version__ = "20150321-1000"
__status__ = "beta"
__license__ = "GPL"


class ObserverError(Exception):
    u"""
    ObserverError - Exceção geral para as classes Subject e Listener
    ----------------------------------------------------------------------------
    Esta exceção é disparada quando alguma anormalidade com ocorre nos métodos
    relacionados a Listeners e Subjects.
    """
    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value

    def __str__(self):
        return u"Erro no padrão Observer: {0}".format(self.value)


#-------------------------------------------------------------------------------
class Listener(object):
    u"""
    Listener - Classe base para componentes data-aware
    ----------------------------------------------------------------------------
    Listeners são entidades que são notificadas por instâncias de classes
    derivadas de Subject quando algum evento ocorre. Eles devem implementar o
    método processEvent() para processar os eventos que recebem.
    """
    def __init__(self):
        u"""
        Deve ser implementado pelas classes derivadas.
        Em um Listener puro, não há nada para fazer.
        """
        pass

    def process_event(self, event=None, subject=None):
        u"""
        Esse método deve ser sobrecarregado com o processamento de notificações
        enviadas por subjects. O evento que motivou a notificação pode ser
        enviado através de event. O subject que disparou a notificação pode ser
        passado através de subject.
        """
        raise NotImplementedError(u"Método abstrato")


#-------------------------------------------------------------------------------
class Subject(object):
    u"""
    Subject - Classe base de elementos observáveis
    ----------------------------------------------------------------------------
    Subjects são entidades observáveis que em determinadas operações podem
    afetar o comportamento de outras entidades. Nesse caso, elas podem notificar
    as interessadas através do envio de Events com o metodo notify().
    Os observadores (Listeners) devem se vincular aos Subjects através do método
    attach(). Se não quiser mais receber notificações, pode se desvincular do
    Subject atraves do método detach().
    """
    def __init__(self):
        u"""
        Cria uma lista vazia de listeners
        """
        self._listeners = [] # lista de listeners a serem notificados

    def attach(self, *listeners):
        u"""
        Vincula listeners a um subject, se eles já não estiverem vinculados.
        Qualquer número de listeners podem ser passados como parametros no
        formato s.attach(l1, l2, l3, ....)
        """
        for listener in listeners:
            if not listener in self._listeners:
                self._listeners.append(listener)

    def detach(self, *listeners):
        u"""
        Desvincula listeners de um subject, se estiverem vinculados
        Qualquer número de listeners podem ser passados como parametros no
        formato s.detach(l1, l2, l3, ....)
        """
        lista = []
        try:
            for listener in listeners:
                try:
                    self._listeners.remove(listener)
                except ValueError:
                    lista.append(listener)
        finally:
            if len(lista) > 0:
                raise ObserverError(u"Listeners não registrados", lista)

    def notify(self, event=None):
        u"""
        Para cada listener da lista, executa seu método processEvent. O método
        pode passar um evento, opcionalmente
        """
        for listener in self._listeners:
            listener.process_event(event=event, subject=self)


#-------------------------------------------------------------------------------
if __name__ == "__main__":
    print u"Observer module"
    print u"Created by {0} ({1})".format(__author__, __email__)
    print u"Version {0} - {1}".format(__version__, __status__)
    