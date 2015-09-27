# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:33:44 2015

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
dial.text = "Volts"

botao = OnOffButton()
botao.textTrue = "Ligado"
botao.textFalse = "Desligado"

display = Display()

#comm = COMM(type="Arduino", port='/dev/ttyACM0')
comm = COMM(type="Arduino", port='/dev/ttyACM0', baudrate=9600)

tagGeradora = Tag()
tagGeradora._scan = 0.05
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value",1)
tagGeradora.provider = ArduinoLink(comm,"a:0:i")
tagGeradora.providerEnable = True

tagGeradora2 = Tag()
tagGeradora2._scan = 0.10
AdapterContinuous(99,0,tagGeradora,"value",tagGeradora2,"value",3)
tagGeradora2.provider = ArduinoLink(comm,"d:9:p")
tagGeradora2.providerEnable = False

#AdapterContinuous(0,0,display,"value",tagGeradora2,"value",1)

tagGeradora3 = Tag()
tagGeradora3._scan = 0.05
adaptador = AdapterContinuous(0,0,botao,"value",tagGeradora3,"value",2)
#tagGeradora3.provider = Provider(comm,"d:4:o")
tagGeradora3.providerEnable = False
#AdapterContinuous(0,0,display,"value",tagGeradora3,"value",1)
AdapterDiscret(0,0, display,"value", tagGeradora3, "value", 1,"Aberto","Fechado")

AdapterContinuous(0,1,tagGeradora2,"state",tagGeradora3, "value",1)


layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(botao)
layout.addWidget(display)

scan = Scan(0.3)
scan.add(tagGeradora)
scan.add(tagGeradora2)
scan.add(tagGeradora3)

GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()

sys.exit(app.exec_())  