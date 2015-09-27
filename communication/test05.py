# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:33:44 2015

@author: root
"""

import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
import threading

from comm import COMM
from provider import Provider


app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,1)
dial.setScale(0,1.0,0.1)

botao = OnOffButton()
botao.textTrue = "Ligado"
botao.textFalse = "Desligado"


#comm = COMM(type="Arduino", port='/dev/ttyACM0')
comm = COMM(type="Arduino", port='/dev/ttyACM0', baudrate=9600).create()

tagGeradora = Tag()
tagGeradora._scan = 0.10
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value","t->w")
tagGeradora._adapter = adaptador
tagGeradora.providerEnable = True
tagGeradora.provider =Provider(comm,"a:0:i:")

tagGeradora2 =  Tag(Identity(0,),True,True)
tagGeradora2._scan = 0.03
adaptador2 = AdapterContinuous(0,True,botao,"value",tagGeradora2,"value","w->t")
tagGeradora2._adapter = adaptador2
tagGeradora2.providerEnable = False
tagGeradora2.provider = Provider(comm,"d:13:o")



layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(botao)

scan = Scan(0.1)
scan.add(tagGeradora)
scan.add(tagGeradora2)

GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()

sys.exit(app.exec_())  