# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:27:39 2015

@author: root
"""

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

from SalaLimpa2 import *
#from doisWidget_Widget import *

from communication import *
#from provider import Provider
#from modbusLink import ModbusLink
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    
    
    com2 = COMM(type="Modbus",port='/dev/ttyACM0', address=1)
    
    

    
    tagBotao = Tag()
    tagBotao._scan = 0.1
    AdapterContinuous(0,0, ui.onOffButton_3,"value", tagBotao, "value", 3)
    a =  ModbusLink(name="Botao",board=com2, register=0, type="register")
    tagBotao.provider = a
    tagBotao.providerEnable = True
    
    """Adaptador que Cria uma Nova Faixa e Adiciona ao Widget LED"""
    
    adaptador2 = AdapterRange(0,0,ui.led_3,"value",tagBotao,"value",1)
    adaptador2.limits(minimum=0,average=1)
    adaptador2.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    adaptador3 = AdapterRange(0,0,ui.led_4,"value",tagBotao,"value",1)
    adaptador3.limits(minimum=0,average=1)
    adaptador3.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    adaptador4 = AdapterRange(0,0,ui.led_5,"value",tagBotao,"value",1)
    adaptador4.limits(minimum=0,average=1)
    adaptador4.condition({"Cond1":"Emergency","Cond2":"Normal"})
    
    AdapterContinuous(0,0, ui.onOffButton_4,"value", tagBotao, "value", 1)
    AdapterContinuous(0,0, ui.onOffButton_5,"value", tagBotao, "value", 1)
    
    tagBotao2 = Tag()
    tagBotao2._scan = 0.1
    AdapterContinuous(0,0, ui.onOffButton,"value", tagBotao2, "value", 2)
    tagBotao2.providerEnable = False
    
    AdapterContinuous(0,0,tagBotao,"state",tagBotao2,"value",4)  

    
    AdapterDiscret(0,0, ui.display,"value", tagBotao2, "value", 1,"Aberto","Fechado")

        

    
    scan = Scan(0.01)
    scan.add(tagBotao)
    scan.add(tagBotao2)
    
    scan.start()   
    
    MainWindow.show()
    sys.exit(app.exec_())