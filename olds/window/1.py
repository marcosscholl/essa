
import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *
import threading

from seisWidget2 import *
#from doisWidget_Widget import *


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    tagGeradora = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.dial_3Widget,"value",tagGeradora,"value",1)
    #adaptador5.scale(0,0,1000,0,100)
    
   
    tagGeradora.providerEnable = True
    tagGeradora._provider = SequenceGenerator(1,min=0,max=1000,step=1)
    tagGeradora._scan = 0.1
    AdapterContinuous(0,0,ui.dial_3Widget_2,"value",tagGeradora,"value",1)
    AdapterContinuous(0,0,ui.thermo,"value",tagGeradora,"value",1)
    AdapterContinuous(0,0,ui.thermometer,"value",tagGeradora,"value",1)
    AdapterContinuous(0,0,ui.displayLCD,"value",tagGeradora,"value",1)
    
    tagPlota = Tag()
    adaptador5 = AdapterContinuous(0,0,ui.plot,"value",tagPlota,"value",1)
    tagPlota._adapter = adaptador5
    tagPlota.providerEnable = True
    tagPlota._provider = SineGenerator(1,min=-1,max=1,step=10)
    tagPlota._scan = 0.1
    
    scan = Scan(0.01)
    scan.add(tagGeradora)
    scan.add(tagPlota)
    
    scan.start()
    
    #print ui.centralwidget.update()
    
    """
    import time
    def updateWidget():       
        #app.activeModalWidget
        while True:
            print "Update"
            time.sleep(5)
            
            for apps in app.allWidgets() :
                apps.update()
                print "Update"
                time.sleep(5)
            
        
               
    updateWidgetThread = threading.Thread(target=updateWidget,)
    updateWidgetThread.setDaemon(True)
    updateWidgetThread.start()
    """
    
    MainWindow.show()
    
    sys.exit(app.exec_())