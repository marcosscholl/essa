# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:42:35 2015

@author: root
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import xml.etree.ElementTree as ET

def ResolvePath(essaXML):
    tree = ET.parse(essaXML)
    root = tree.getroot()
    for essa in root.iter('essa'):
       
        pathLog = None
        pathInstall = None
        pathLog = essa.find('logs')
        if pathLog.attrib['path'] is not None:
            try:
                pathLog = pathLog.attrib['path']
            except AttributeError:
                pass
            
        pathInstall = essa.find('install')
        if pathInstall.attrib['path'] is not None:
            try:
                pathInstall = pathInstall.attrib['path']
            except AttributeError:
                pass
    if pathLog[:1] != '/': pathLog = "/"+pathLog
    if pathLog[-1:] != "/": pathLog = pathLog+"/"
    
    if pathInstall[:1] != '/': pathInstall = "/"+pathInstall
    if pathInstall[-1:] != "/": pathInstall = pathInstall+"/"
    
    return pathInstall, pathLog

#print ResolvePath('C:\Users\MarcosScholl\Dropbox\Spyder\essa\config\Teste06-w.xml')