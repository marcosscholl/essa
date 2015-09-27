# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:15:06 2015

@author: root
"""

import xml.etree.ElementTree as ET

#from PyQt4 import Qt,QtGui, QtCore



arquive = "Adapter03.xml"
componentes = []

tree = ET.parse(arquive)
root = tree.getroot()

 
for adapters in root.iter('adapters'):
    for adapter in adapters.findall('adapter'):
        name=None
        nome=None
        id=0
        startValue=0
        widget=None
        widgetProprierty=None
        tag=None
        tagProprierty=None
        directionDataFlow=None
        minimum = None
        average = None
        maximum = None
        limit = None
        condition = None
        limits = None
        valueTrue = None
        valueFalse = None
        if (adapter.attrib["type"] == "AdapterContinuous"):
            try:
                name = adapter.attrib["type"]
                nome = adapter.find('name').text
                id = int(adapter.find('id').text)
                startValue = int(adapter.find('startValue').text)
                widget = adapter.find('widget').text
                widgetProprierty = adapter.find('widgetProprierty').text
                tag = adapter.find('tag').text
                tagProprierty = adapter.find('tagProprierty').text
                directionDataFlow = int(adapter.find('direction').text)
                
                if adapter.find('scale') is not None:
                    try:
                        adapterlimit = adapter.find('scale')          
                        minimum = float(adapterlimit.find('minimum').text)
                        maximum = float(adapterlimit.find('maximum').text)
                        newMin = float(adapterlimit.find('newMinimum').text)
                        newMax = float(adapterlimit.find('newMaximum').text)
                    except AttributeError:
                        pass                
                adpt =u"{}={}({},{},ui.{},'{}',{},'{}',{})".format(nome,name,id,startValue,widget,widgetProprierty,tag,tagProprierty,directionDataFlow)        
                componentes.append(adpt)
                if maximum is not None and newMin is not None: componentes.append(u"{}.scale({},{},{},{})".format(nome,minimum,maximum,newMin,newMax))
            except AttributeError:
                print u"Problem in declaration of AdapterContinuous"        
        
        if (adapter.attrib["type"] == "AdapterRange"):
            try:
                name = adapter.attrib["type"]
                nome = adapter.find('name').text
                id = int(adapter.find('id').text)
                startValue = int(adapter.find('startValue').text)
                widget = adapter.find('widget').text
                widgetProprierty = adapter.find('widgetProprierty').text
                tag = adapter.find('tag').text
                tagProprierty = adapter.find('tagProprierty').text
                directionDataFlow = int(adapter.find('direction').text)
                condition = adapter.find('condition').text
                if adapter.find('limits') is not None:
                    try:
                        adapterlimit = adapter.find('limits')          
                        minimum = float(adapterlimit.find('minimum').text)
                        average = float(adapterlimit.find('average').text)
                        maximum = float(adapterlimit.find('maximum').text)
                        limit = float(adapterlimit.find('limit').text)
                    except AttributeError:
                        pass
                    
                if minimum is not None:
                    if limits is None: limits ="minimum={}".format(minimum)
                    else: limits +=",minimum={}".format(minimum)
                if average is not None: 
                    if limits is None: limits =u"average={}".format(average)
                    else: limits +=u",average={}".format(average)
                if maximum is not None: 
                    if limits is None: limits =u"maximum={}".format(maximum)
                    else: limits +=u",maximum={}".format(maximum)
                if limit is not None: 
                    if limits is None: limits =u"limit={}".format(limit)
                    else: limits +=u",limit={}".format(limit)   
        
                adpt =u"{}={}({},{},ui.{},'{}',{},'{}',{})".format(nome,name,id,startValue,widget,widgetProprierty,tag,tagProprierty,directionDataFlow)        
                componentes.append(adpt)
                if limits is not None: componentes.append(u"{}.limits({})".format(nome,limits))
                if condition is not None: componentes.append(u"{}.condition({})".format(nome,condition))
            except AttributeError:
                print u"Problem in declaration of AdapterRange"
                
            
        elif (adapter.attrib["type"] == "AdapterDiscret"):
            try:
                name = adapter.attrib["type"]
                nome = adapter.find('name').text
                id = int(adapter.find('id').text)
                startValue = int(adapter.find('startValue').text)
                widget = adapter.find('widget').text
                widgetProprierty = adapter.find('widgetProprierty').text
                tag = adapter.find('tag').text
                tagProprierty = adapter.find('tagProprierty').text
                directionDataFlow = int(adapter.find('direction').text)
                valueTrue = adapter.find('valueTrue').text
                valueFalse = adapter.find('valueFalse').text
                
                adpt =u"{}={}({},{},ui.{},'{}',{},'{}',{},'{}','{}')".format(nome,name,id,startValue,widget,widgetProprierty,tag,tagProprierty,directionDataFlow,valueTrue,valueFalse)        
                componentes.append(adpt)
            except AttributeError:
                print u"Problem in declaration of AdapterDiscret"

"""
print name
print nome
print id
print startValue
print widget
print widgetProprierty
print tag
print tagProprierty
print directionDataFlow
print minimum
print average
print maximum 
print limit 
"""
for component in componentes:
    print component