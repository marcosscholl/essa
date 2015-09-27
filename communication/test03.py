# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:58:13 2015

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

dial2 = Dial()
dial2.setRange(0,1)
dial2.setScale(0,1.0,0.1)

botao = OnOffButton()
botao.textTrue = "Ligado"
botao.textFalse = "Desligado"


#tagGeradora.attach(comm)
#AdapterContinuous(0,0,dial2,"value",tagGeradora,"value","t->w")
#comm = COMM('/dev/ttyACM0',"a:0:i:")
comm = COMM(type="Arduino", port='/dev/ttyACM0')

tagGeradora2 = Tag()
tagGeradora2._scan = 0.05
adaptador2 = AdapterContinuous(0,0,dial2,"value",tagGeradora2,"value","t->w")
tagGeradora2._adapter = adaptador2
tagGeradora2.providerEnable = True
tagGeradora2.provider = Provider(comm.getComm,"a:0:i:")
#tagGeradora2.attach(comm2)

tagGeradora = Tag()
tagGeradora._scan = 1
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value","t->w")
tagGeradora._adapter = adaptador
tagGeradora.providerEnable = True
#tagGeradora._provider =  SequenceGenerator(1,min=0,max=100,step=1)
tagGeradora.provider = Provider(comm.getComm,"a:1:i:")


layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(dial2)

scan = Scan()
scan.add(tagGeradora)
scan.add(tagGeradora2)


GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()


sys.exit(app.exec_())  