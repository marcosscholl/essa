# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:16:12 2015

@author: root
"""

import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from aware import *
from data import *
from hmi import *
import threading

from communication import *
#from provider import Provider


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


comm = COMM(type="Arduino", port='/dev/ttyACM0')

tagGeradora = Tag()
tagGeradora._scan = 0.10
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value",1)
tagGeradora.providerEnable = True
tagGeradora.provider = Provider(comm,"a:0:i:")

tagGeradora2 = Tag()
tagGeradora2._scan = 0.05
adaptador2 = AdapterContinuous(0,0,dial2,"value",tagGeradora2,"value",1)
tagGeradora2.providerEnable = True
tagGeradora2.provider = Provider(comm,"a:1:i:")



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