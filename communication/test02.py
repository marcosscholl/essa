# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:21:40 2015

@author: root
"""


import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
from comm import *
from provider import Provider
import threading

app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,1)
dial.setScale(0,1.0,0.1)

botao = OnOffButton()
botao
comm = COMM(type="Arduino", port='/dev/ttyACM0')

tagGeradora = Tag()
tagGeradora._scan = 0.01
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value","t->w")
tagGeradora._adapter = adaptador
tagGeradora.providerEnable = True
#tagGeradora._provider =  SequenceGenerator(1,min=0,max=100,step=1)
tagGeradora.provider = Provider(comm.getComm,"a:0:i:")

layout = QtGui.QVBoxLayout()
layout.addWidget(dial)

scan = Scan()
scan.add(tagGeradora)


GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()


sys.exit(app.exec_())  