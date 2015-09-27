# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:33:35 2015

@author: scholl
"""

import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
import threading

app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,100)
dial.setScale(0,1.0,5.0)


dial2 = Dial()
dial2.setRange(0,100)
dial2.setScale(0,1.0,10.0)

tagGeradora = Tag()
tagGeradora._scan = 0.1
adaptador = AdapterContinuous(0,0,dial,"value",tagGeradora,"value","t->w")
tagGeradora._adapter = adaptador
tagGeradora.providerEnable = True
tagGeradora._provider =  SequenceGenerator(1,min=0,max=100,step=1)
AdapterContinuous(0,0,dial2,"value",tagGeradora,"value","t->w")


layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(dial2)

scan = Scan()
scan.add(tagGeradora)


GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()


sys.exit(app.exec_())  