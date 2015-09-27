# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:00:41 2015

@author: MarcosScholl

"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150617-1000"
__status__ = "beta"
__license__ = "GPL"


import xml.etree.ElementTree as ET

from PyQt4 import Qt,QtGui, QtCore
import _globals




class ESSAParser:
    def __init__(self,arquive):
        self._arquive = arquive
        self._pathInstall = None
        self._pathLog = None
        self._comm = []
        self._tags = []
        self._adapters = []
        self._window = None
        self._alarms = []
        
        #print "g"
        #print "1",_globals.pathInstall
        #print "2",_globals.pathLog
        #def parseXML(self, arquive):
        
        tree = ET.parse(self._arquive)
        root = tree.getroot()
        for essa in root.iter('essa'):
            
            pathInstall = essa.find('install')
            if pathInstall.attrib['path'] is not None:
                try:
                    self._pathInstall = pathInstall.attrib['path']
                    if self._pathInstall[:1] != '/': self._pathInstall = "/"+self._pathInstall
                    if self._pathInstall[-1:] != "/": self._pathInstall = self._pathInstall+"/"
                    _globals.pathInstall = self._pathInstall
                except AttributeError:
                    pass
            
            
            window = essa.find('window')
            if window.attrib['name'] is not None:
                try:
                    self._window = window.attrib['name']
                except AttributeError:
                    pass
        
            pathLog = None
            pathLog = essa.find('logs')
            if pathLog.attrib['path'] is not None:
                try:
                    pathLog = pathLog.attrib['path']
                    self._pathLog = pathLog
                    if pathLog[:1] != '/': self._pathLog = "/"+pathLog
                    if pathLog[-1:] != "/": self._pathLog = pathLog+"/"
                    _globals.pathLog = self._pathLog
                except AttributeError:
                    pass
                
            scan = essa.find('scan')
            self._scan = scan.text    
            try:
                comms = essa.find('comunications').findall('comm')
            
                for comm in comms:
                    link = name = port = baudrate = address = bytesize = parity = stopbits = timeout = mode = None
                    if comm.attrib['type'] == 'Modbus':
                        try:
                            name = comm.find('name').text
                        except AttributeError:
                            pass
                        try:
                            port = comm.find('port').text
                        except AttributeError:
                            pass
                        try:
                            baudrate = comm.find('baudrate').text
                        except AttributeError:
                            pass
                        try:
                            address = comm.find('address').text
                        except AttributeError:
                            pass
                        try:
                            bytesize = comm.find('bytesize').text
                        except AttributeError:
                            pass
                        try:
                            parity = comm.find('parity').text
                        except AttributeError:
                            pass
                        try:
                            stopbits = comm.find('stopbits').text
                        except AttributeError:
                            pass
                        try:
                            timeout = comm.find('timeout').text
                        except AttributeError:
                            pass
                        try:
                            mode = comm.find('mode').text
                        except AttributeError:
                            pass
                        
                        if port is not None:
                            if link is None: link ="port='{}'".format(port)
                            else: link +=",port='{}'".format(port)
                        if baudrate is not None:
                            if link is None: link ="baudrate={}".format(baudrate)
                            else: link +=",baudrate={}".format(baudrate)
                        if address is not None:
                            if link is None: link ="address={}".format(address)
                            else: link +=",address={}".format(address)
                        if bytesize is not None:
                            if link is None: link ="bytesize={}".format(bytesize)
                            else: link +=",bytesize={}".format(bytesize)
                        if parity is not None:
                            if link is None: link ="parity={}".format(parity)
                            else: link +=",parity={}".format(parity)
                        if stopbits is not None:
                            if link is None: link ="stopbits={}".format(stopbits)
                            else: link +=",stopbits={}".format(stopbits)
                        if timeout is not None:
                            if link is None: link ="timeout={}".format(timeout)
                            else: link +=",timeout={}".format(timeout)
                        if mode is not None:
                            if link is None: link ="mode='{}'".format(mode)
                            else: link +=",mode='{}'".format(mode)
                        
                        adpt = "{}=COMM(type='Modbus',{})".format(name,link)
                        self._comm.append(adpt)
                    if comm.attrib['type'] == 'Arduino':
                        try:
                            name = comm.find('name').text
                        except AttributeError:
                            pass
                        try:
                            port = comm.find('port').text
                        except AttributeError:
                            pass
                        try:
                            baudrate = comm.find('baudrate').text
                        except AttributeError:
                            pass
                        
                        if port is not None:
                            if link is None: link ="port='{}'".format(port)
                            else: link +=u",port='{}'".format(port)
                        if baudrate is not None:
                            if link is None: link ="baudrate={}".format(baudrate)
                            else: link +=u",baudrate={}".format(baudrate)
                        
                        adpt = u"{}=COMM(type='Arduino',{})".format(name,link)
                        self._comm.append(adpt)
            except AttributeError:
                pass            
                        
            tags = essa.find('tags').findall('tag')
            for tag in tags:
                nome=None
                id=0
                startValue=0
                readOnly = True
                providerEnable = None
                provider = None
                script = None
                try:
                    nome = tag.attrib['name']
                    id = int(tag.attrib['id'])
                    startValue = int(tag.find('startValue').text)
                    readOnly = tag.find('readOnly').text
                    scan = float(tag.find('scan').text)
                    providerEnable = tag.find('providerEnable').text
                    try: provider = tag.find('provider').text
                    except: pass
                    
                    try: script = str(tag.find('script').text)
                    except: pass
                    adpt =u"{}=Tag(Identity({},'{}'),{},{},{},{},'{}')".format(nome,id,nome,startValue,readOnly,scan,providerEnable,script) 
                    self._tags.append(adpt)
                    if provider is not None:
                        adpt = "{}.provider = {}".format(nome,provider)
                        self._tags.append(adpt)
                except AttributeError:
                    print u"Problem in declaration of Tag"
            
            adapters = essa.find('adapters').findall('adapter')    
            for adapter in adapters:
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
                try:
                    name = adapter.attrib["type"]
                    nome = adapter.attrib['name']
                    id = int(adapter.attrib['id'])
                    startValue = int(adapter.find('startValue').text)
                    widget = adapter.find('widget').text
                    widgetProprierty = adapter.find('widgetProprierty').text
                    tag = adapter.find('tag').text
                    tagProprierty = adapter.find('tagProprierty').text
                    directionDataFlow = int(adapter.find('direction').text)
                except:
                    print u"Problem in data declaration of Adapter '{}'".format(nome)     
                    #pass
                if (name == "AdapterContinuous"):
                    try:
                        if adapter.find('scale') is not None:
                            adapterlimit = adapter.find('scale')   
                            try:       
                                minimum = float(adapterlimit.find('minimum').text)
                            except AttributeError:
                                pass
                            try:
                                maximum = float(adapterlimit.find('maximum').text)
                            except AttributeError:
                                pass
                            try:
                                newMin = float(adapterlimit.find('newMinimum').text)
                            except AttributeError:
                                pass
                            try:
                                newMax = float(adapterlimit.find('newMaximum').text)
                            except AttributeError:
                                pass                
                        
                        adpt =u"{}={}({},{},ui.{},'{}',{},'{}',{})".format(nome,name,id,startValue,widget,widgetProprierty,tag,tagProprierty,directionDataFlow)        
                        self._adapters.append(adpt)
                        if maximum is not None and newMin is not None: self._adapters.append(u"{}.scale({},{},{},{})".format(nome,minimum,maximum,newMin,newMax))
                    except AttributeError:
                        print u"Problem in declaration of AdapterContinuous"        
                
                if (name == "AdapterRange"):
                    try:
                        condition = adapter.find('condition').text
                        if adapter.find('limits') is not None:
                            try:
                                adapterlimit = adapter.find('limits')          
                            except AttributeError:
                                pass
                            try:
                                minimum = float(adapterlimit.find('minimum').text)
                            except AttributeError:
                                pass
                            try:
                                average = float(adapterlimit.find('average').text)
                            except AttributeError:
                                pass
                            try:
                                maximum = float(adapterlimit.find('maximum').text)
                            except AttributeError:
                                pass
                            try:
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
                        self._adapters.append(adpt)
                        if limits is not None: self._adapters.append(u"{}.limits({})".format(nome,limits))
                        if condition is not None: self._adapters.append(u"{}.condition({})".format(nome,condition))
                    except AttributeError:
                        print u"Problem in declaration of AdapterRange"
                           
                elif (name == "AdapterDiscret"):
                    try:
                        valueTrue = adapter.find('valueTrue').text
                        valueFalse = adapter.find('valueFalse').text
                        
                        adpt =u"{}={}({},{},ui.{},'{}',{},'{}',{},'{}','{}')".format(nome,name,id,startValue,widget,widgetProprierty,tag,tagProprierty,directionDataFlow,valueTrue,valueFalse)        
                        self._adapters.append(adpt)
                    except AttributeError:
                        print u"Problem in declaration of AdapterDiscret"                          
            try:    
                alarms = essa.find('alarms').findall('alarm')    
                for alarm in alarms:
                    try:
                        nome = alarm.find('name').text
                        id = int(alarm.find('id').text)
                        tags = alarm.find('tags').text
                        typE = alarm.find('type').text
                        value = float(alarm.find('value').text)
                        lifeGui = int(alarm.find('lifeGui').text)
                        adpt =u"Alarm(id={},name='{}',tags=[{}],{}={},lifeGui={})".format(id,nome,tags,typE,value,lifeGui)
                        self._alarms.append(adpt)
                    except AttributeError:
                        print u"Problem in declaration of AdapterDiscret"
            except AttributeError:
                pass
                

    
    @property
    def create(self):
        return self._window, self._scan, self._comm, self._tags, self._adapters, self._alarms

"""     
tags = ESSAParser("/home/scholl/Dropbox/Spyder/essa/config/Teste01.xml").create

for tag in tags:
    print tag    

print "Install=", _globals.pathInstall
print "Log=", _globals.pathLog
"""