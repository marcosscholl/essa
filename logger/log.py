# -*- coding: utf-8 -*-

__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150601-1000"
__status__ = "stable"
__license__ = "GPL"

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *

import logging
from logging.handlers import TimedRotatingFileHandler


#from aware import _globals

"""
second (s)
minute (m)
hour (h)
day (d)
w0-w6 (weekday, 0=Monday)
midnight
"""


#pathInstall, pathLog = ResolvePath('/home/scholl/Dropbox/Spyder/essa/config/Teste05.xml')
#pathInstall, pathLog = ResolvePath('C:\Users\MarcosScholl\Dropbox\Spyder\essa\config\Teste05.xml')
pathInstall = '/home/scholl/Dropbox/Spyder/'
#----------------------------------------------------------------------
def LogCreate(logger_name="ESSA_Logger", log_file=None, level=None, pathLog=None): 
    global pathInstall
    pathFile = None
    if log_file is None:
        log_file = "Essa_test"
    if level is None:
        level = "INFO"
        
    pathInstall = '/home/scholl/Dropbox/Spyder/'
        
    if pathLog is None: 
        if pathInstall is not None: pathFile = "{}essa/logs/{}.log".format(pathInstall,log_file)
    else: pathFile = "{}{}.log".format(pathLog,log_file)
    


    logger = logging.getLogger(logger_name)
    handler = TimedRotatingFileHandler(pathFile,
                                       when="m",
                                       interval=5,
                                       backupCount=5)
    formatter = logging.Formatter('%(asctime)s; %(name)-12s %(levelname)-8s; %(message)s;')
    handler.setFormatter(formatter)


    logger.addHandler(handler)

    if level is not None:
        if level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            logger.setLevel(logging.INFO)
        elif level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
            
    return logging.getLogger(logger_name)
    
def LogAlarm(logger_name="ESSA_ALARM", log_file=None, level=None, pathLog=None):    
    global pathInstall
    pathFile = None
    if log_file is None:
        log_file = "Essa_Alarm"
    if level is None:
        level = "WARNING"
        
    
    if pathLog is None: 
        if pathInstall is not None: pathFile = "{}essa/logs/{}.log".format(pathInstall,log_file)
    else: pathFile = "{}{}.log".format(pathLog,log_file)
    
        
    logger = logging.getLogger(logger_name)
    
    handler = TimedRotatingFileHandler(pathFile,
                                       when="d",
                                       interval=1,
                                       backupCount=5)
    formatter = logging.Formatter('%(asctime)s;%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if level is not None:
        if level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            logger.setLevel(logging.INFO)
        elif level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
            
    return logging.getLogger(logger_name)

def LogCSV(logger_name="ESSA_Logger", log_file=None, level=None, pathLog=None): 
    global pathInstall
    pathFile = None
    if log_file is None:
        log_file = "Essa_LOG"
    if level is None:
        level = "INFO"
        
    pathInstall = '/home/scholl/Dropbox/Spyder/'
        
    if pathLog is None: 
        if pathInstall is not None: pathFile = "{}essa/logs/{}.csv".format(pathInstall,log_file)
    else: pathFile = "{}{}.csv".format(pathLog,log_file)
    


    logger = logging.getLogger(logger_name)
    handler = TimedRotatingFileHandler(pathFile,
                                       when="m",
                                       interval=5,
                                       backupCount=5)
    formatter = logging.Formatter('%(message)s %(asctime)s ', datefmt='%d-%m-%y %H:%M')
    handler.setFormatter(formatter)


    logger.addHandler(handler)

    if level is not None:
        if level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            logger.setLevel(logging.INFO)
        elif level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
            
    return logging.getLogger(logger_name)