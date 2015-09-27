# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:12:18 2015

@author: scholl
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:42:52 2015

@author: scholl
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:48:16 2015

@author: scholl
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *

from seisWidget import *

from XMLFactorTag import *
from XMLFactorAdapter import *

import threading

    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    

    scan = Scan()
    
    listaTags = XMLFactorTag('Tag1.xml').create
    listaAdapters = XMLFactorAdapter("Adapter02.xml").create
    
    tagsAdapter = []
    print listaTags
    print "\n", listaAdapters

    #Inicializa Adaptor e Tag
    for tags in listaTags:
        component = tags[:len(tags)-1].split(",")
        tag = (component[1]).replace(")","").replace("'","")
        exec(tag+"= Tag()")
        
        adapter = component[10]
        tagsAdapter.append(adapter)
        exec(adapter+"= None")
        
        
    #print "TENTA GERAR ADAPTERS"
    for adapter in listaAdapters:
        exec(adapter)      
        
    #print "TENTA GERAR TAGS"
    for tag in listaTags:     
        exec(tag)      
        
    #Adaptadores Sem Tag, conectando aos widgets
    for adapters in listaAdapters:
        adapter = adapters.replace(" ","").split("=")[0]
        if (adapter not in tagsAdapter):
            adpt = eval(adapter)
            adpt._t = eval(adapters.split(",")[4])
            adpt.connect()
        
    #add Tags em SCan
    for tag in listaTags:
        tag_ = tag[:len(tag)-1].split(",")
        tag = (tag_[1]).replace(")","").replace("'","")
        tag = eval(tag)
        for adapter in tagsAdapter:
            adpt = eval(adapter) 
            if adpt == tag._adapter:
                adpt._t = tag
                adpt.connect()
                scan.add(tag)
    
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()
    
    MainWindow.show()
    sys.exit(app.exec_())