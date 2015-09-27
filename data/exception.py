# -*- coding: utf-8 -*-
"""
exception.py - Classes de excecoes do framework Kast
--------------------------------------------------------------------------------
Contem a classe KastError
--------------------------------------------------------------------------------
Outros eventos builtin usados sao o NotImplementedError
"""

__author__  = "Carlos R. Rocha"
__email__   = "cticarlo@gmail.com"
__version__ = "20110411-0900"
__status__  = "stable"
__license__ = "GPL"

class KastError(Exception):
    """
    KastError - Excecao geral de erros do framework Kast
    ----------------------------------------------------------------------------
    Esta eh uma excecao que deve ser disparada quando algum erro especifico do
    uso do framework Kast ocorre.
    """
    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value
        
    def __str__(self):
        return "Erro em Kast: {0}".format(self.value)

class KastListError(Exception):
    """
    KastListError - Excecao causada por manipulacao de listas ou tuplas
    ----------------------------------------------------------------------------
    Excecao que deve ocorrer quando uma lista ou tupla eh processada e
    seus elementos disparam excecoes individuais, capturadas pelo metodo e
    relacionando os elementos em uma lista que deve ser passada para a excecao.
    Assim, permite tomar alguma acao com os elementos que geraram o problema.
    """
    def __init__(self, value, list):
        Exception.__init__(self, value)
        self.value = value
        self.list = list 
        
    def __str__(self):
        return "Erro em Kast - {0}: {1}".format(self.value, self.list)

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    print u"Módulo exception"
    print u"Criado por {0} ({1})".format(__author__, __email__)
    print u"Versão {0} - {1}".format(__version__, __status__)
