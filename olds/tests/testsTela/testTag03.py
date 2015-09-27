# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:07:27 2015

@author: root
"""

import xml.etree.ElementTree as ET

#from PyQt4 import Qt,QtGui, QtCore



arquive = "Tag03.xml"
componentes = []

tree = ET.parse(arquive)
root = tree.getroot()


for adapters in root.iter('tags'):
    for adapter in adapters.findall('tag'):
        name=None
        nome=None
        id=0
        startValue=0
        readOnly = True
        providerEnable = True
        provider = None
        
        try:
            nome = adapter.find('name').text
            id = int(adapter.find('id').text)
            startValue = int(adapter.find('startValue').text)
            readOnly = adapter.find('readOnly').text
            scan = float(adapter.find('scan').text)
            providerEnable = bool(adapter.find('name').text)
            provider = adapter.find('provider').text
            
            adpt =u"{}=Tag(Identity({},'{}'),{},{},{},{},{})".format(nome,id,nome,startValue,readOnly,scan,providerEnable,provider)        
            componentes.append(adpt)
        except AttributeError:
            print u"Problem in declaration of Tag" 
        
for component in componentes:
   print component            