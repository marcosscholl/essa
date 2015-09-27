# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:20:28 2015

@author: scholl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:12:18 2015

@author: scholl
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:42:52 2015

@author: scholl
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:48:16 2015

@author: scholl
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *

from seisWidget import *

import threading
import time

from pyqt_nonblock import pyqtapplication
        
if __name__ == "__main__":
    import sys
    #app = pyqtapplication()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    
    scan = Scan(1)
    
    
    listaTags = TagParser('Tag1.xml').create
    listaAdapters = AdapterParser("Adapter02.xml").create
       
    for tag in listaTags:     
        exec(tag)  
        tag_ = tag[:len(tag)-1].split(",")
        tag_ = (tag_[1]).replace(")","").replace("'","")
        scan.add(eval(tag_))
    
    for adapter in listaAdapters:
        exec(adapter)           
    
        
    Alarm(id=0,name="Alarme1",tags=[tagGeradora],maxmax=750, lifeGui=15)
    GeradorThread = threading.Thread(target=scan.run, ) 
    GeradorThread.setDaemon(True)
    GeradorThread.start()
    
    
    MainWindow.show()
  
        
    sys.exit(app.exec_())
    
