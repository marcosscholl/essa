# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150525-1000"
__status__ = "beta"
__license__ = "GPL"

import sys, os
from easygui import buttonbox, codebox

import threading
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from aware import *
from alarm import *
from sound import Music
#from aware.resolvePath import ResolvePath
from aware import _globals


lock =  threading.RLock()
alarmLog = None


#pathInstall, pathLog = ResolvePath('/home/scholl/Dropbox/Spyder/essa/config/ESSA01.xml')
#pathInstall, pathLog = ResolvePath('C:\Users\MarcosScholl\Dropbox\Spyder\essa\config\Teste06.xml')
    
class PopUp(Listener): 
    def __init__(self):
        Listener.__init__(self)
        global lock
        global alarmLog, pathInstall, pathLog
        self._val = None
        self._lifeGui = 10
        sound_file = os.path.join("{}essa/alarm/sounds/".format(_globals.pathInstall), "alert3.wav") 
        self.som = Music(sound_file)        
        
        
    def threaded(fn):
        def wrapper(*args, **kwargs):    
            threading.Thread(target=fn, args=args, kwargs=kwargs).start()
        return wrapper
    
    @threaded    
    def AlarmGui(self, msg="Alert", title="Alert", choices=("Button[1]", "Button[2]", "Button[3]"), type="alert", sound=None):
        try:
            if type == "alert":
                img = "alert.png"
            elif type == "error":
                img = "error.png"
                
            image = "{}essa/alarm/images/{}".format(_globals.pathInstall,img)
            self._val = buttonbox(msg=msg, title=title, image=image, choices=choices, default_choice="Sim",lifeGui=self._lifeGui, sounds=sound)
            self.analiza(sound)
        except:
             pass
            
    @threaded    
    def analiza(self, sound):
        while self._val is None:
            time.sleep(0.5)
        if self._val == "Ciente":
            _globals.alarmAlerts -= 1
            alarmLog.warning("Alarm Warning STOPPED - User Action;")
            sound.stop()
        else:
            alarmLog.warning("Alarm Warning STOPPED AUTOMATICALLY - USER AWAY;")
            _globals.warningAlarm.warning("Alarm Warning STOPPED AUTOMATICALLY - USER AWAY;")
            sound.stop()
            #sound.play()
            #_globals.sound = sound
            
            
            
            
    @threaded 
    def LogGui(self, title="Alert", msg="Alert", arq="Essa_test.log"):
        filename = os.path.normcase("{}{}".format(_globals.pathLog,arq))
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        return codebox(msg=msg + filename, title=title, text=text)


    def process_event(self, event=None, subject=None):
        global alarmLog
        if (isinstance(event, EventGui)):
            try:
                lock.acquire()
                #print "Subject", subject
                subject.alarmGui.AlarmGui(title="Alert for "+str(subject._subjectAlarm), msg="            Notice for "+str(subject._subjectAlarm)+" !\nYour "+str(subject._alarmEvent)+" value has been reached. \n                Action required!", choices=["Ciente"],sound=self.som)                            
                alarmLog = subject._alarmLog  
                self._lifeGui = subject._lifeGui
                self.som.play()
            finally:
                lock.release()
        elif (isinstance(event,EventGuiClose)):
            try:
                lock.acquire()
                subject.alarmGui = None
                subject.alarmGui = PopUp()
                self.som.stop()
                
            finally:
                lock.release()
        else:
            print "OUTRO EVENTO"
