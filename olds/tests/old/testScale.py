# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:26:43 2015

@author: root
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:31:33 2015

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:39:24 2015

@author: MarcosScholl
"""
import sys, os, threading
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *

from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()


dial2 = Dial()
dial2.setRange(0,100)
dial2.setScale(0,3.0,5.0)

dial3 = Dial()
dial3.setRange(0,1000)


tagDial2 = Tag(Identity(0, "TagDial2"),0,True)
adaptador2 = AdapterContinuous(1,0, dial2, "value",tagDial2, "value","t->w")
adaptador2.scale(0,10,0,1)
tagDial2._adapter = adaptador2
tagDial2._provider = SequenceGenerator(1,min=0,max=10,step=1)
tagDial2._providerEnable = True
tagDial2._scan = 1

AdapterContinuous(3,0,dial3,"value",tagDial2,"value","t->w")


layout = QtGui.QVBoxLayout()
layout.addWidget(dial2)
layout.addWidget(dial3)

scan = Scan()
scan.add(tagDial2)

GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(10,10,400,600)
window.show()

adaptador2.process_event(Event())

sys.exit(app.exec_())  