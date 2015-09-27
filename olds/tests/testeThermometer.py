# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:20:21 2015

@author: MarcosScholl
"""
import sys
from PyQt4 import QtGui, uic
import os
from PyQt4 import Qt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)  
    window = QtGui.QWidget()
    window2 = QtGui.QWidget()
    window3 = QtGui.QWidget()
    
    
    thermometer = Thermometer()
    thermometer2 = Thermometer()
    thermometer3 = Thermometer()
    
    thermometer4 = Thermometer()
    thermometer5 = Thermometer()
    thermometer6 = Thermometer()
    
    thermometer7 = Thermometer()
    thermometer8 = Thermometer()
    thermometer9 = Thermometer()
    
    tagGeradora3 = Tag()
    adaptador5 = AdapterContinuous(0,0,thermometer,"value",tagGeradora3,"value","t->w")
    tagGeradora3._adapter = adaptador5
    tagGeradora3.providerEnable = True
    tagGeradora3._provider = SequenceGenerator(1,min=0,max=100,step=10)
    tagGeradora3._scan = 0.001
    AdapterContinuous(0,0,thermometer2,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer3,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer4,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer5,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer6,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer7,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer8,"value",tagGeradora3,"value","t->w")
    AdapterContinuous(0,0,thermometer9,"value",tagGeradora3,"value","t->w")
    

    scan = Scan()
    scan.add(tagGeradora3)
    
    layout = QtGui.QVBoxLayout()
    layout.addWidget(thermometer)
    layout.addWidget(thermometer2)
    layout.addWidget(thermometer3)
    
    
    
    layout2 = QtGui.QVBoxLayout()
    layout2.addWidget(thermometer4)
    layout2.addWidget(thermometer5)
    layout2.addWidget(thermometer6)
    
 
    layout3 = QtGui.QVBoxLayout()
    layout3.addWidget(thermometer7)
    layout3.addWidget(thermometer8)
    layout3.addWidget(thermometer9)
    
    import threading

    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()

    
    window.setLayout(layout)
    window.setGeometry(50,100,300,500)
    window.show()
    
    window2.setLayout(layout2)
    window2.setGeometry(350,100,300,500)
    window2.show()
    
    window3.setLayout(layout3)
    window3.setGeometry(650,100,300,500)
    window3.show()
    sys.exit(app.exec_())