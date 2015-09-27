# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 01:04:18 2015

@author: root
"""

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
#from provider import Provider

comm = COMM(type="Arduino", port='/dev/ttyACM0')

app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,1)
dial.setScale(0,1.0,0.1)

tagGeradora = Tag()
tagGeradora._scan = 0.05
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value",1)
tagGeradora.provider = ArduinoLink(comm,"a:0:i")
tagGeradora.providerEnable = True


tagGeradora2 = Tag()
tagGeradora2._scan = 0.10
adaptador2 = AdapterContinuous(0,0,tagGeradora2,"value",tagGeradora,"value",4)
tagGeradora2.provider = ArduinoLink(comm,"d:9:p")
tagGeradora2.providerEnable = False

layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
#layout.addWidget(slider)

scan = Scan(0.1)
scan.add(tagGeradora)

scan.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()



sys.exit(app.exec_())  