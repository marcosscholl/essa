# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:09:01 2015

@author: scholl
"""


import sys
import os
from PyQt4 import Qt, QtCore, QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from aware import *
from data import *
from hmi import *
import threading

from doisWidget import *
#from doisWidget_Widget import *
#from sound import Music
import time
if __name__ == "__main__": 
    """
    import pyglet
    fileName = os.path.join('/home/scholl/Dropbox/Spyder/essa/sounds/', "alert2.wav") 
    source = pyglet.media.load(fileName, streaming=True) 
    player = pyglet.media.Player() 
    player.eos_action = pyglet.media.Player.EOS_LOOP # Loops the song 
    player.queue(source) 
    player.play()
    pyglet.app.run()
    time.sleep(3)
    pyglet.app.exit()
    """
    """
    fileName = os.path.join('/home/scholl/Dropbox/Spyder/essa/sounds/', "alert2.wav")
    a = Music(fileName)
    a.play()
    time.sleep(2)
    a.stop()
    """
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    pallet= MainWindow.palette()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

 
    
    tagGeradora = Tag(Identity(55, 'TagGeradora'))
    adaptador5 = AdapterContinuous(0,0,ui.dial_3Widget,"value",tagGeradora,"value",1)
    tagGeradora._adapter = adaptador5
    tagGeradora.providerEnable = True
    tagGeradora._provider = SequenceGenerator(1,min=0,max=13,step=1)
    tagGeradora._scan = 1

    #
    scan = Scan()
    scan.add(tagGeradora)
    
    tagGeradora2 = Tag(Identity(99, 'TagGeradora2'))
    adaptador6 = AdapterContinuous(0,0,ui.dial_3Widget_2,"value",tagGeradora2,"value",1)
    tagGeradora2._adapter = adaptador6
    tagGeradora2.providerEnable = True
    tagGeradora2._provider = SequenceGenerator(1,min=10,max=50,step=7)
    tagGeradora2._scan = 2
    scan.add(tagGeradora2)
    
    Alarm(id=0,name="Alarme1",tags=[tagGeradora],maxmax=2, lifeGui=10)
    
    scan.start()
    
    
    MainWindow.show()
    sys.exit(app.exec_())