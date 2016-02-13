# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from runtime import ESSA

essa = ESSA('/home/scholl/Dropbox/Spyder/essa/config/MPCT_Simulation.xml')
essa.start()
