# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:40:42 2015

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

from SalaLimpa import *
#from doisWidget_Widget import *

from comm import COMM
from provider import Provider
from modbusLink import ModbusLink
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    
    
    com2 = COMM(type="Modbus",port='/dev/ttyACM0', address=1)
    
    

    
    tagBotao = Tag()
    tagBotao._scan = 0.01
    tagBotao._adapter = AdapterRange(0,0, ui.onOffButton_3,"value", tagBotao, "value", "w<->t")
    a =  ModbusLink(name="Botao",board=com2, register=0, type="register")
    tagBotao.provider = a
    tagBotao.providerEnable = True
    
    """Adaptador que Cria uma Nova Faixa e Adiciona ao Widget LED"""
    
    adaptador2 = AdapterRange(0,0,ui.led_3,"value",tagBotao,"value","t->w")
    adaptador2.limits(minimum=0,average=1)
    adaptador2.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    adaptador3 = AdapterRange(0,0,ui.led_4,"value",tagBotao,"value","w<->t")
    adaptador3.limits(minimum=0,average=1)
    adaptador3.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    adaptador4 = AdapterRange(0,0,ui.led_5,"value",tagBotao,"value","w<->t")
    adaptador4.limits(minimum=0,average=1)
    adaptador4.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    AdapterContinuous(0,0, ui.onOffButton_4,"value", tagBotao, "value", "w<->t")
    AdapterContinuous(0,0, ui.onOffButton_5,"value", tagBotao, "value", "w<->t")
        

    
    scan = Scan(0.01)
    scan.add(tagBotao)
    
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()   
    
    MainWindow.show()
    sys.exit(app.exec_())