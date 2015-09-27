# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:57:59 2015

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 05 01:04:29 2015

@author: MarcosScholl
"""

import time
from threading import Thread
import threading
import datetime
"""
import threading 
from concurrent.futures import ThreadPoolExecutor

lock =  threading.Lock()
"""
class ScanWindow(Thread): 
    
    def __init__(self, scan=0.100):
        Thread.__init__(self)
        self._windows = []
        self._scan = scan;
        #global lock

           
    def add(self,window):
        self._windows.append(window)
        
    def run(self):
        i = 0
        while i < 2000:
            if self._windows is not None:
                for window in self._windows:
                    if window.isEnabled():
                        #print "Update"
                        window.update()
                        time.sleep(self._scan)
