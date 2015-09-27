# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:22:55 2015

@author: root
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from runtime import ESSA

essa = ESSA('/home/scholl/Dropbox/Spyder/essa/config/teste.xml')
essa.start()

def remap(x, oMin, oMax, nMin, nMax ):  
    #range check
    if oMin == oMax:
        print "Warning: Zero input range"
        return None

    if nMin == nMax:
        print "Warning: Zero output range"
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result
    
print remap(3,410,105,0,100)