# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:32:07 2015

@author: root
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150606-1800"
__status__ = "beta"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logger import *

objThread = None

alarmAlerts = 0
warningAlarm = LogAlarm(logger_name="ESSA_WarningAlarm", log_file="ESSA_WarningAlarm")
sound = None

fileConfigPath = None
pathInstall = None
pathLog = None