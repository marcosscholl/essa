# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QwtCompass.ui'
#
# Created: Sat Feb 08 00:29:14 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import PyQt4.Qwt5 as Qwt

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
from PyQt4 import Qt, QtGui, QtCore

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass




def enumList(enum, sentinel):
    '''
    '''
    return [enum(i) for i in range(sentinel)]

colorGroupList = enumList(
    Qt.QPalette.ColorGroup, Qt.QPalette.NColorGroups)
colorRoleList = enumList(
    Qt.QPalette.ColorRole, Qt.QPalette.NColorRoles)
handList  = enumList(
    Qwt.QwtAnalogClock.Hand, Qwt.QwtAnalogClock.NHands)
    
    
class WidgetBussola(Widget, QtGui.QWidget):
    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self,parent)
              
        self.compass = Qwt.QwtCompass(self)
        
        palette = self.compass.palette()
        #Cor Interna Bussola
        palette.setColor(self.compass.backgroundRole(), Qt.Qt.darkCyan)
        self.compass.setPalette(palette)
        
        palette = Qt.QPalette()
        for colorRole in colorRoleList:
            palette.setColor(colorRole, Qt.QColor())
        palette.setColor(
            Qt.QPalette.Base,
            #Alterando uma pouco a cor, mais forte ou mais fraco, depende do valor
            self.compass.palette().color(self.compass.backgroundRole()).light(105))
        palette.setColor(
            #Cor de fundo do corculo da agulha
            Qt.QPalette.Foreground,
            palette.color(Qt.QPalette.Base))



        self.compass.setLineWidth(2)
        self.compass.setFrameShadow(Qwt.QwtCompass.Raised)
        self.compass.setScaleTicks(0, 0, 2)
       
        self.compass.setScaleOptions( Qwt.QwtDial.ScaleTicks |  Qwt.QwtDial.ScaleLabel | 
            Qwt.QwtDial.ScaleBackbone)
        self.compass.setLabelMap({0.0: "N",
                                 45.0: "ne",
                                 90.0: "E",
                                 135.0: "se",
                                 180.0: "S",
                                 225.0: "so",
                                 270.0: "O",
                                 315.0: "no"})
        self.compass.setScale(72,0, 0)
        
        self.compass.setNeedle(Qwt.QwtCompassMagnetNeedle(
        Qwt.QwtCompassMagnetNeedle.TriangleStyle,
            Qt.Qt.white,
            Qt.Qt.red))
        self.compass.setValue(35.0)
        
        

        newPalette = self.compass.palette()
    
        
        ##Criando Cor de fundo para Bussola
        
        for colorRole in colorRoleList:
            if palette.color(colorRole).isValid():
                for colorGroup in colorGroupList:
                    newPalette.setColor(
                        colorGroup, colorRole, palette.color(colorRole))
        
        self.compass.setPalette(newPalette)
        
        
        
        #Posicionamento do Widget
        #layout = Qt.QGridLayout(self)
        #layout.addWidget(self.compass)
        #layout.setColumnStretch(1,1) 
        layout = QtGui.QVBoxLayout(self)
    
        layout.addWidget(self.compass)
    
    @pyqtSlot(float)    
    def setValue(self, value):
        super(WidgetBussola, self).setValue(value)
        
    @property
    def value(self):
        self.compass.value()
    
    @value.setter
    def value(self, value):
        self.compass.setValue(float(value))
        
    def valueSetter(self,value):
        self.value = (float(value)) 
        
    def getValue(self):
        return self.compass.value()
      
    Value = QtCore.pyqtProperty(float,fget=getValue,fset=valueSetter) 
        
        


       
""" 
class WidgetBussola(Widget, QtGui.QWidget):
    def __init__(self, parent=None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self, parent=None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  
    
        palette = self.palette()
        #Cor Interna Bussola
        palette.setColor(self.backgroundRole(), Qt.Qt.darkCyan)
        self.setPalette(palette)
        
        #Posicionamento do Widget
        layout = Qt.QGridLayout(self)
        layout.addWidget(self.ui.setupUi(1),1,1)
        layout.setColumnStretch(1,1)
        
"""
"""
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
    #window.setAutoFillBackground(False)
    
    #window.setMinimumWidth(150)
    #window.setMinimumHeight(300)
    bussola = WidgetBussola()
    bussola.show()

    sys.exit(app.exec_())
"""


if __name__ == '__main__':
    import sys
    
    # BUSSOLA
    app = QtGui.QApplication(sys.argv)
    bussola = WidgetBussola()
    bussola.value = 50
    
   
    #bussola.setGeometry(1050, 100, 300, 300)  
    
    bussola.show()
    sys.exit(app.exec_())
