# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150618-0100"
__status__ = "stable"
__license__ = "GPL"

import threading
import time

class Scan(threading.Thread):
    def __init__(self, scan=0.01):
        threading.Thread.__init__(self)
        self.iterations = 0
        self.daemon = True  # OK for main to exit even if instance is still running
        self.paused = True  # start out paused
        self.state = threading.Condition()
        self._scan = scan
        self._tags = []
        
    def add(self,tag):
        self._tags.append(tag)

    def run(self):
        self.resume() # unpause self
        while True:
            with self.state:
                if self.paused:
                    self.state.wait() # block until notified
                if self._tags is not None:
                    for tag in self._tags:
                        if tag._enable:
                            #if tag.name == "TAGLED":
                                #print tag.name
                                #print tag.id
                                #print tag.value
                            newUpdate = int(tag._timeUpdate + (tag._scan * 1000))
                            if (int(time.time() * 1000) > newUpdate):                         
                                if tag._providerEnable:
                                    tag.update()
                                elif not(tag._providerEnable):
                                    tag.update()
                    #self._stopevent.wait(self._sleepperiod)
                    #time.sleep(self._sleepperiod)
        time.sleep(self._scan)

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting

    def pause(self):
        #print "Pause"
        with self.state:
            self.paused = True  # make self block and wait
