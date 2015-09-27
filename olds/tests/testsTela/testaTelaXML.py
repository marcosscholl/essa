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

import copy
import threading
import types

    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    scan = Scan()
    
    listaTags = XMLFactorTag('Tag1.xml').create
    listaAdapters = XMLFactorAdapter("Adapter01.xml").create
    
    tagAdapter = None

    #print listaTags
    #print "\n",listaAdapters, "\n"
    #exec("tagGeradora = Tag()")

    #Cria Atributor de Adapter


    """    
    for tags in listaTags:
        tag_ = tags
        tag_ = tag_[:len(tag_)-1]
        tag_ = tag_.split(",")
        
        #Inicializa TAG
        tag = (tag_[1]).replace(")","").replace("'","")
        ##############################3
        #exec(tag+"= Tag()")
        exec('globals()['+tag+'] = Tag()')
        ##############################
        print tag
        print "\nTag Objeto", eval(tag)
        
        #Inicializa Adapter
        adapter = tag_[10]
        print adapter
        exec(adapter+"= None")
        print "\nAdapter Objeto", eval(adapter)
      
    """
    
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
        tagAdapter = adapter
        print "adapter:", adapter
        exec(adapter+"= None")
        exec('globals()['+adapter+'] = '+adapter)
        
        
    #print "TENTA GERAR ADAPTERS"
    for adapter in listaAdapters:
        #print adapter
        exec(adapter)
        print "\nAdapterGerado: ", adapter01
        
    #print "TENTA GERAR TAGS"
    for tag in listaTags:
        
        exec(tag)
        print "\nGeraTAG: ", tagGeradora,"\n"
        
        
    #add Tags em SCan
    for tag in listaTags:
        tag_ = tag
        tag_ = tag_[:len(tag_)-1]
        tag_ = tag_.split(",")
        
        #Inicializa TAG
        tag = (tag_[1]).replace(")","").replace("'","")
        tag = globals()[tag]
        print "tag:",tag
        scan.add(tag)
        print "TAGSS:", tag
        eval(tagAdapter)._t = tag
        eval(tagAdapter).conect()
        
        print "\n \n"
        print "tagGeradora._adapter =", eval("tagGeradora._adapter")
        print "adapter01._t =", eval("adapter01._t")
        print "\n\n"
        
        
    """        
    #print "\n\n TAG TAG \n"
    for tag in listaTags:
        tag = tag.replace(" ","").replace("[","").replace("'","")
        tag = tag.split("=")
        scan.add(eval(tag[0]))
    """
    """
    g = dict ( globals ())
    # Loop sobre pares.
    for item in g.items():
        print(item[0], "=", item[1]) , "\n"
    """
    #scan.add(tagGeradora)
    
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()
    
    MainWindow.show()
    sys.exit(app.exec_())