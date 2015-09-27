# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:23:35 2015

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


app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,1)
dial.setScale(0,1.0,0.1)

comm = COMM(type="Arduino", port='/dev/ttyACM0')


tagGeradora = Tag()
tagGeradora._scan = 0.05
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value",1)
#tagGeradora._adapter = adaptador
tagGeradora.provider = ArduinoLink(comm,"a:0:i")
tagGeradora.providerEnable = True

tagGeradora2 = Tag()
tagGeradora2._scan = 0.10
AdapterContinuous(99,0,tagGeradora,"value",tagGeradora2,"value",4)
#tagGeradora2._adapter = adaptador2
tagGeradora2.provider = ArduinoLink(comm,"d:9:p")
tagGeradora2.providerEnable = False


layout = QtGui.QVBoxLayout()
layout.addWidget(dial)

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