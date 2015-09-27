# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:44:28 2015

@author: root
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main import *

essa = ESSA('/home/scholl/Dropbox/Spyder/essa/config/ESSA01.xml')
essa.start()


