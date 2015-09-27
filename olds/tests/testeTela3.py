# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:55:36 2015

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:28:49 2015

@author: MarcosScholl
"""

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

from Tela3 import *
from XMLFactor import *
import copy
from multiprocessing import Process
import threading

from ScanWindow import *

class SCADA(threading.Thread):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    #lista = XMLFactor('Tela2.ui').create
    #Dial2 = eval("ui."+"dial_2Widget")
    #Dial2.value = 50
    #print "LISTA", lista
    """
    for widget in lista:
        try: 
            aux = eval("ui."+widget.getName())
            aux.__dict__ = widget.__dict__.copy()

        except AttributeError:
            print widget.getName(), " not valid"
        
    """    
    #ui.display.value = "Simulação Supervisório"
    #ui.displayLCD.value= 75
    
    
    tagGeradora = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.dial_2Widget,"value",tagGeradora,"value","t->w")
    tagGeradora._adapter = adaptador5
    tagGeradora.providerEnable = True
    tagGeradora._provider = SequenceGenerator(1,min=0,max=100,step=1)
    tagGeradora._scan = 0.3
    AdapterContinuous(0,0,ui.dial_3Widget,"value",tagGeradora,"value","t->w")
    AdapterContinuous(0,0,ui.thermo,"value",tagGeradora,"value","t->w")
    
    
    tagGeradora2 = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.dial_1Widget,"value",tagGeradora2,"value","t->w")
    tagGeradora2._adapter = adaptador5
    tagGeradora2.providerEnable = True
    tagGeradora2._provider = SequenceGenerator(1,min=0,max=100,step=5)
    tagGeradora2._scan = 0.5
    AdapterContinuous(0,0,ui.dial_Widget,"value",tagGeradora2,"value","t->w")
    AdapterContinuous(0,0,ui.thermometer,"value",tagGeradora2,"value","t->w")
   
    adaptador2 = AdapterRange(0,0,ui.led,"value",tagGeradora2,"value","t->w")
    adaptador2.limits(20,40,80,100)
    adaptador2.condition({"Cond1":"Blue","Cond2":"Normal","Cond3":"Warning","Cond4":u"Emergency"})

    tagGeradoraThermomether = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.thermo,"value",tagGeradoraThermomether,"value","t->w")
    tagGeradoraThermomether._adapter = adaptador5
    tagGeradoraThermomether.providerEnable = True
    tagGeradoraThermomether._provider = SequenceGenerator(1,min=0,max=100,step=10)
    tagGeradoraThermomether._scan = 0.01 
    AdapterContinuous(0,0,ui.slider,"value",tagGeradoraThermomether,"value","t->w")
    AdapterContinuous(0,0,ui.displayLCD,"value",tagGeradoraThermomether,"value","t->w")
    AdapterContinuous(0,0,ui.display_2,"value",tagGeradoraThermomether,"value","t->w")
    

    """
    tagGeradora3 = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.thermometer,"value",tagGeradora3,"value","t->w")
    tagGeradora3._adapter = adaptador5
    tagGeradora3.providerEnable = True
    tagGeradora3._provider = SequenceGenerator(1,min=0,max=100,step=10)
    tagGeradora3._scan = 0.5
    #AdapterContinuous(0,0,tagGeradora3,"value",tagGeradora,"value","t->t")
    """
    """
    adaptador2 = AdapterRange(0,0,ui.,"value",tagGeradora3,"value","t->w")
    adaptador2.limits(20,40,80,100)
    adaptador2.condition({"Cond1":"Blue","Cond2":"Normal","Cond3":"Warning","Cond4":u"Emergency"})
    """
    
    #Process(target=tagGeradora2).start()
    #Process(target=tagGeradoraThermomether).start()
    
    scan = Scan()
    scan.add(tagGeradora)
    scan.add(tagGeradora2)
    scan.add(tagGeradoraThermomether)
    #scan.add(tagGeradora3)
    
    
    import threading

    
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()
    
    scanWindow = ScanWindow()
    scanWindow.add(ui.widget)
    
    GeradorThreadWindow = threading.Thread(target=scanWindow.run, ) 
    GeradorThreadWindow.setDaemon(True)
    GeradorThreadWindow.start()
    
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