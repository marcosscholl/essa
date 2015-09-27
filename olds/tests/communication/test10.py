# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:08:06 2015

@author: root
"""

import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from aware import *
from data import *
from hmi import *
from communication import *
import threading

#from comm import COMM
#from provider import Provider
#from modbusLink import ModbusLink

com2 = COMM(type="Modbus",port='/dev/ttyACM0', address=1)



app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,255)
#dial.setScale(0,1.0,0.1)

slider = Slider()
slider.range(0,255)

botao = OnOffButton()
#botao.textTrue = "Ligado"
#botao.textFalse = "Desligado"
botao.textTrue = ""
botao.textFalse = ""
botao.setImageFalse('/home/scholl/Dropbox/Spyder/essa/images/closed-2.png')
botao.setImageTrue('/home/scholl/Dropbox/Spyder/essa/images/opened-2.png')
    
tagSlider = Tag(Identity(0,"TagSlider"), 0, True)
tagSlider._scan = 0.1
tagSlider.providerEnable = False
AdapterContinuous(0,0,slider,"value",tagSlider,"value",2)
tagSlider._script = ("if value >= 200: value=0")

tagLed = Tag()
tagLed._scan = 0.1
comm2 = ModbusLink(name="LedValor",board=com2, register=1, type="register")
tagLed.provider = comm2
tagLed.providerEnable = False
AdapterContinuous(1,0,tagLed,"value",tagSlider,"value",4)


tagPlot = Tag()
tagPlot._scan = 0.01
comm3 =  ModbusLink(name="LedValor",board=com2, register=1, type="register")
tagPlot.provider = comm3
tagPlot.providerEnable = True
AdapterContinuous(2,0,dial,"value",tagPlot,"value",1)


tagBotao = Tag()
tagBotao._scan = 0.01
a =  ModbusLink(name="Botao",board=com2, register=0, type="register")
tagBotao.provider = a
tagBotao.providerEnable = True
AdapterContinuous(3,0, botao,"value", tagBotao, "value", 3)

layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(slider)
layout.addWidget(botao)

scan = Scan(0.01)
scan.add(tagSlider)
scan.add(tagLed)
scan.add(tagPlot)
scan.add(tagBotao)

GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()



sys.exit(app.exec_()) 