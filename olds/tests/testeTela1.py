# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:42:20 2015

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

from Tela1 import *
from XMLFactor import *
import copy

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    """
    teste = ui.dial_2Widget
    teste.value = 53
    teste.setMaxValue(77)
    ui.dial_2Widget = copy.copy(teste)
    teste.value = 99
    print "TESTE:", teste
    print "UI.DIAL:", ui.dial_2Widget
    """
    #DialWidget2 = ui.dial_2Widget
    #DialWidget2.setGeometry(QtCore.QRect(40, 90, 196, 196))
    #DialWidget2.setObjectName("DialWidget2")
    #DialWidget2.setValue(50)
    
    #lista = XMLFactor('Tela1.ui').create
    #Dial2 = eval("ui."+"dial_2Widget")
    #Dial2.value = 50
    #print "LISTA", lista
    """
    for widget in lista:
        aux = eval("ui."+widget.getName())
        if aux.getName == "display_2":
            widget.value = "99"
        #aux.__dict__ = widget.__dict__.copy()
        
        
    ui.display.value = "Simulação Supervisório"
    ui.displayLCD.value= 75
    """
    tagGeradora = Tag()
    adaptador5 = eval("AdapterContinuous(0,0,ui.dial_2Widget,'value',tagGeradora,'value','t->w')")
    #adaptador5 = AdapterContinuous(0,0,ui.displayLCD,"value",tagGeradora,"value","t->w")
    tagGeradora._adapter = adaptador5
    tagGeradora.providerEnable = True
    tagGeradora._provider = SequenceGenerator(1,min=0,max=100,step=1.22)
    tagGeradora._scan = 0.5
    #AdapterContinuous(0,0,ui.dial_3Widget,"value",tagGeradora,"value","t->w")
    #AdapterContinuous(0,0,ui.thermo,"value",tagGeradora,"value","t->w")
    
    
    scan = Scan()
    scan.add(tagGeradora)
    
    import threading

    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()

    
    MainWindow.show()
    sys.exit(app.exec_())



"""
class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('Tela1.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
"""