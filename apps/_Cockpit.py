# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from runtime import ESSA

essa = ESSA('/home/scholl/Dropbox/Spyder/essa/config/cockpit.xml')
essa.start()

"""
palette = QtGui.QPalette()
palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("/home/scholl/GitHub/PythonProjectsAndCodes/CockpitNew/CockpitBackground.png")))
MainWindow.setPalette(palette)
"""