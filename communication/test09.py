# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:40:41 2015

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
from modbusLink import ModbusLink

com2 = COMM(type="Modbus",port='/dev/ttyACM0', address=1)



app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,255)
#dial.setScale(0,1.0,0.1)

slider = Slider()
slider.range(0,255)

botao = OnOffButton()
botao.textTrue = "Ligado"
botao.textFalse = "Desligado"

tagSlider = Tag(Identity(0,"TagSlider"), 0, True)
adaptador = AdapterContinuous(0,0,slider,"value",tagSlider,"value","w->t")
tagSlider._adapter = adaptador
tagSlider._scan = 0.1
tagSlider.providerEnable = False


tagGeradora2 = Tag()
tagGeradora2._scan = 0.1
adaptador2 = AdapterContinuous(0,0,tagGeradora2,"value",tagSlider,"value","t->t")
tagGeradora2._adapter = adaptador2
comm2 = ModbusLink(name="LinkLed",board=com2, register=1,type="register")
tagGeradora2.provider = comm2
#tagGeradora2.attach(comm2)
tagGeradora2.providerEnable = False


tagGeradora3 = Tag()
tagGeradora3._scan = 0.01
adaptador3 = AdapterContinuous(0,0,dial,"value",tagGeradora3,"value","t->w")
tagGeradora3._adapter = adaptador3
comm3 = ModbusLink(name="LinkLed",board=com2, register=1,type="register")
tagGeradora3.provider = comm3
#agGeradora3.attach(comm3)
tagGeradora3.providerEnable = True


tagBotao = Tag()
tagBotao._scan = 0.01
tagBotao._adapter = AdapterContinuous(0,0, botao,"value", tagBotao, "value", "w<->t")
a = ModbusLink(name="LinkBotao",board=com2, register=0, type="register")
tagBotao.provider = a
tagBotao.providerEnable = True

layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(slider)
layout.addWidget(botao)

scan = Scan(0.01)
scan.add(tagSlider)
scan.add(tagGeradora2)
scan.add(tagGeradora3)
scan.add(tagBotao)

GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()



sys.exit(app.exec_()) 