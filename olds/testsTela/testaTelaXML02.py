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

from doisWidget import *

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
    listaAdapters = XMLFactorAdapter("Adapter01.xml").create
    
    tagsAdapter = []

    
    for tags in listaTags:
        tag_ = tags
        tag_ = tag_[:len(tag_)-1]
        tag_ = tag_.split(",")
        
        #Inicializa TAG
        tag = (tag_[1]).replace(")","").replace("'","")
        ##############################3
        exec(tag+"= Tag()")
        
        #exec('globals()['+tag+'] = Tag()')
        ##############################
        adapter = tag_[10]
        tagsAdapter.append(adapter)
        #print "adapter:", adapter
        exec(adapter+"= None")
        #exec('globals()['+adapter+'] = '+adapter)
        
        
    #print "TENTA GERAR ADAPTERS"
    for adapter in listaAdapters:
        exec(adapter)
        
    #print "TENTA GERAR TAGS"
    for tag in listaTags:     
        exec(tag)
        
        
    #add Tags em SCan
    aux = 0;
    for tag in listaTags:
        tag_ = tag
        tag_ = tag_[:len(tag_)-1]
        tag_ = tag_.split(",")
        tag = (tag_[1]).replace(")","").replace("'","")
        #print "9=", tag
        #print tagsAdapter
        for adapter in tagsAdapter:
            if eval(adapter) == eval(tag)._adapter:
                #print "adapter:",adapter
                #print "tag:",tag                
                #print "É IGUAL"
                eval(adapter)._t = eval(tag)
                eval(adapter).conect()
                scan.add(eval(tag))
        

    """  
    g = dict ( globals ())
    # Loop sobre pares.
    for item in g.items():
        print(item[0], "=", item[1]) , "\n"
     
    print "\n \n"
    print "1-tagGeradora =", eval("tagGeradora")
    print "1-adapter01._t =", eval("adapter01._t")
    print "1-adapter01 =", eval("adapter01")
    print "1-tagGeradora._adapter =", eval("tagGeradora._adapter")
    print "\n"
    print "2-tagGeradora2 =", eval("tagGeradora2")
    print "2-adapter02._t =", eval("adapter02._t")
    print "2-adapter02 =", eval("adapter02")
    print "2-tagGeradora2._adapter =", eval("tagGeradora2._adapter")
    print "\n\n"
    """
    """
    ('tagGeradora', '=', <data.tag02.Tag object at 0x7ff1f15620d0>) 
    ('adapter01', '=', <data.adapter03.AdapterContinuous object at 0x7ff1f1554f90>) 

    ('tagGeradora2', '=', <data.tag02.Tag object at 0x7ff1f1562190>) 
    ('adapter02', '=', <data.adapter03.AdapterContinuous object at 0x7ff1f1554fd0>) 
    """

    #scan.add(tagGeradora)
    
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()
    
    MainWindow.show()
    sys.exit(app.exec_())