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

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
import threading

from comm import COMM
from provider import Provider

comm = COMM(type="Arduino", port='/dev/ttyACM0')

app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()

dial = Dial()
dial.setRange(0,1)
dial.setScale(0,1.0,0.1)

slider = Slider()
slider.range(0,1)


tagSlider = Tag(Identity(0,"TagSlider"), 0, True)
adaptador = AdapterContinuous(0,0,slider,"value",tagSlider,"value","w->t")
tagSlider._adapter = adaptador
tagSlider._scan = 0.1
tagSlider.providerEnable = False

tagDial = Tag()
adaptador2 = AdapterContinuous(0,0,dial,"value",tagSlider,"value","t->w")
tagDial._adapter = adaptador2
tagDial._scan = 0.10
tagDial.providerEnable = False


tagGeradora2 = Tag()
tagGeradora2._scan = 0.10
adaptador2 = AdapterContinuous(0,0,tagGeradora2,"value",tagSlider,"value","t->t")
tagGeradora2._adapter = adaptador2
comm3 = Provider(comm,"d:9:p")
tagGeradora2.provider = comm3
tagGeradora2.providerEnable = False

layout = QtGui.QVBoxLayout()
layout.addWidget(dial)
layout.addWidget(slider)

scan = Scan(0.1)
scan.add(tagSlider)
scan.add(tagGeradora2)


GeradorThread = threading.Thread(target=scan.run, ) 
GeradorThread.setDaemon(True)
GeradorThread.start()

window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()



sys.exit(app.exec_())  