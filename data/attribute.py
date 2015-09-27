# -*- coding: utf-8 -*-
"""
attribute.py - Classes que representam dados e metodos auxiliares
--------------------------------------------------------------------------------
Contem as classes Attribute, Attributes, AttributeList, Identity
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *
#from data import KastError, KastListError

__author__  = "Carlos R. Rocha"
__email__   = "cticarlo@gmail.com"
__version__ = "20110411-1200"
__status__ = "stable"
__license__ = "GPL"

#-------------------------------------------------------------------------------


class Identity(Subject):
    """
    Identity - Define uma identidade para um objeto
    Descende de Subject para ser data-aware
    
    Os atributos essenciais de uma instancia de Identity sao:
      - id          : inteiro unico para referenciar a entidade
      - name        : nome da entidade
      - description : descricao mais detalhada da entidade
    """
    changed = EventChanged()
    obrigatorios = ('id', 'name', 'description')
    
    def __init__(self, id = None, name = None, description = None, 
                 readonly=False, **other):
        """
        Inicializador - Define os atributos da identidade e se eles sao
            somente leitura. O valor default eh um dicionario vazio.
        A instancia aceita modificacoes por default
        id - inteiro que referencia a entidade. Default eh None
        name - nome da entidade. Default eh None
        description - descricao detalhada da entidade. Default eh None
        readonly - define se a identidade eh somente leitura. Default eh False
        other - dicionario de outros identificadores opcionais
        """
        self._id = dict(id=id, name=name, description=description, **other)
        self._ro = readonly
        Subject.__init__(self)

    @property
    def readonly(self):
        """
        Retorna verdadeiro se a instancia for somente leitura
        """
        return self._ro
        
    @readonly.setter
    def readonly(self, status):
        """
        Define se a instancia eh somente leitura (True)
        """
        self._ro = status

    def __repr__(self):
        """
        Retorna atributo name da identidade
        """
        return self._id['name']

    def __getitem__(self, key):
        """
        Retorna o valor do elemento key do dicionario se existir
        """
        try:
            return self._id[key]
        except:
            raise (u"{0} não é identificador".format(key))

    def __setitem__(self, key, value=0.0):
        """
        Modifica o valor armazenado no elemento key do dicionario
        Se nao existir, o adiciona, se a instancia nao for somente leitura
        """
        if (self._ro):
            raise (u"Identidade é somente leitura.")
        else:
            self._id[key] = value
            self.notify(Identity.changed)

    def __delitem__(self, key):
        """
        Remove o elemento key do dicionario
        se a instancia nao for somente leitura ou key nao for obrigatorio
        """
        if self._ro:
            raise (u"Identidade é somente leitura.")
        elif key in Identity.obrigatorios:
            raise (u"Atributo obrigatório.")
        else:
            try:
                del self._id[key]
                self.notify(Identity.changed)
            except:
                raise (u"{0} não é identificador".format(key))

    def __contains__(self, key):
        """
        Verifica se a chave key esta contida no dicionario
        """
        return key in self._id

    def __len__(self):
        """
        Retorna o tamanho do dicionario
        """
        return len(self._id)
        
    def setdefault(self, key, value=None):
        """
        Define o valor default de um atributo, se ele nao existir no dicionario
        """
        if key not in self._id:
            self._id[key] = value
            self.notify(Identity.changed)
        return self._id[key]

    @property
    def id(self):
        """
        Retorna o identificador numerico
        """
        return self._id['id']
        
    @id.setter    
    def id(self, value):
        """
        Modifica o id se a instancia nao for somente leitura
        """
        if (self._ro):
            raise (u"Identidade é somente leitura.")
        else:
            self._id['id'] = value
            self.notify(Identity.changed)

    @property
    def name(self):
        """
        Retorna o nome
        """
        return self._id['name']
        
    @name.setter    
    def name(self, value):
        """
        Modifica o nome se a instancia nao for somente leitura
        """
        if (self._ro):
            raise (u"Identidade é somente leitura.")
        else:
            self._id['name'] = value
            self.notify(Identity.changed)
            self.notify(EventUpdated(self))

    @property
    def description(self):
        """
        Retorna a descricao
        """
        return self._id['description']
        
    @description.setter    
    def description(self, value):
        """
        Modifica a descricao se a instancia nao for somente leitura
        """
        if (self._ro):
            raise KastError(u"Identidade é somente leitura.")
        else:
            self._id['description'] = value
            self.notify(Identity.changed)

    def __iter__(self):
        """
        Necessario para definir a classe como generator
        """
        return self._id.iteritems()

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    print u"Módulo attribute"
    print u"Criado por {0} ({1})".format(__author__, __email__)
    print u"Versão {0} - {1}".format(__version__, __status__)
