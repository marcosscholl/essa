# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from runtime import ESSA

scada = ESSA('/home/scholl/Dropbox/Spyder/essa/config/Teste04.xml')
scada.start()