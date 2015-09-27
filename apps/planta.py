# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:49:37 2015

@author: root
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from runtime import ESSA

essa = ESSA('/home/scholl/Dropbox/Spyder/essa/config/planta.xml')
essa.start()