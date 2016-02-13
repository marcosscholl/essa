# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:04:06 2015

@author: scholl
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 00:33:43 2015

@author: scholl
"""

"""
Attitude indicator widget.
"""

import sys
import os
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4 import Qt,QtGui, QtCore
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time, serial, string
import PyQt4.Qwt5 as Qwt
from aware import *

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
    
    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass
       
        
class AttitudeIndicator(Widget, QtGui.QWidget):
    """Widget for showing attitude"""
    def __init__(self, parent=None):
        #super(AttitudeIndicator, self).__init__()
        Widget.__init__(self)
        QtGui.QWidget.__init__(self,parent)        

        self.roll = 0
        self.pitch = 0
        self.hover = False
        self.hoverASL = 0.0
        self.hoverTargetASL = 0.0

        self.setMinimumSize(100, 100)
        # self.setMaximumSize(240,240)
        
        #layout = QtGui.QVBoxLayout(self)
        #layout.setMargin(0)
        #layout.setSpacing(0)
        #layout.addWidget(self)
            
        
        


    def setRoll(self, roll):
        self.roll = roll
        self.update()

    def setPitch(self, pitch):
        self.pitch = pitch
        self.update()
        
    def setHover(self, target):        
        self.hoverTargetASL = target
        self.hover = target>0
        self.update()
        
    def setBaro(self, asl):
        self.hoverASL = asl;
        self.update()

    def setRollPitch(self, roll, pitch):
        self.roll = roll
        self.pitch = pitch
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        size = self.size()
        w = size.width()
        h = size.height()
        #qp.drawEllipse(100,100,100,100)
        qp.translate(w / 2, h / 2)
        qp.rotate(self.roll)
        qp.translate(0, (self.pitch * h) / 50)
        qp.translate(-w / 2, -h / 2)
        qp.setRenderHint(qp.Antialiasing)

        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        # Draw the blue
        qp.setPen(QtGui.QColor(0, 61, 144))
        qp.setBrush(QtGui.QColor(0, 61, 144))
        qp.drawRect(-w, h / 2, 3 * w, -3 * h)

        # Draw the marron
        qp.setPen(QtGui.QColor(59, 41, 39))
        qp.setBrush(QtGui.QColor(59, 41, 39))
        qp.drawRect(-w, h / 2, 3 * w, 3 * h)

        pen = QtGui.QPen(QtGui.QColor(255, 255, 255), 1.5,
            QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(-w, h / 2, 3 * w, h / 2)

        # Drawing pitch lines
        for ofset in [-180, 0, 180]:
            for i in range(-900, 900, 25):
                pos = (((i / 10.0) + 25 + ofset) * h / 50.0)
                if i % 100 == 0:
                    length = 0.35 * w
                    if i != 0:
                        if ofset == 0:
                            qp.drawText((w / 2) + (length / 2) + (w * 0.06),
                                        pos, "{}".format(-i / 10))
                            qp.drawText((w / 2) - (length / 2) - (w * 0.08),
                                        pos, "{}".format(-i / 10))
                        else:
                            qp.drawText((w / 2) + (length / 2) + (w * 0.06),
                                        pos, "{}".format(i / 10))
                            qp.drawText((w / 2) - (length / 2) - (w * 0.08),
                                        pos, "{}".format(i / 10))
                elif i % 50 == 0:
                    length = 0.2 * w
                else:
                    length = 0.1 * w

                qp.drawLine((w / 2) - (length / 2), pos,
                            (w / 2) + (length / 2), pos)

        qp.setWorldMatrixEnabled(False)

        pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 2,
            QtCore.Qt.SolidLine)
        qp.setBrush(QtGui.QColor(0, 0, 0))
        qp.setPen(pen)
        qp.drawLine(0, h / 2, w, h / 2)
        
        
        
        # Draw Hover vs Target
        
        qp.setWorldMatrixEnabled(False)
        
        pen = QtGui.QPen(QtGui.QColor(255, 255, 255), 2,
                         QtCore.Qt.SolidLine)
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.setPen(pen)
        fh = max(7,h/50)
        font = QtGui.QFont('Sans', fh, QtGui.QFont.Light)
        qp.setFont(font)
        qp.resetTransform()
      
        

        
        qp.translate(0,h/2) 
        if not self.hover:  
            qp.drawText(w-fh*10, fh/2, str(round(self.hoverASL,2)))  # asl
               
        
        if self.hover:
            qp.drawText(w-fh*10, fh/2, str(round(self.hoverTargetASL,2)))  # target asl (center)    
            diff = round(self.hoverASL-self.hoverTargetASL,2)
            pos_y = -h/6*diff
            
            # cap to +- 2.8m
            if diff<-2.8:
                pos_y = -h/6*-2.8
            elif diff>2.8:
                pos_y= -h/6*2.8
            else:
                pos_y = -h/6*diff
            qp.drawText(w-fh*3.8, pos_y+fh/2, str(diff)) # difference from target (moves up and down +- 2.8m)        
            qp.drawLine(w-fh*4.5,0,w-fh*4.5,pos_y) # vertical line     
            qp.drawLine(w-fh*4.7,0,w-fh*4.5,0) # left horizontal line
            qp.drawLine(w-fh*4.2,pos_y,w-fh*4.5,pos_y) #right horizontal line
            
    def updatePitch(self, pitch):
        #self.wid.setPitch(pitch - 90)
        self.setPitch(pitch)
        print "updatePitch:", pitch

    def updateRoll(self, roll):
        #self.wid.setRoll((roll / 10.0) - 180.0)
        self.setRoll(roll )
        print "updateRoll:", (roll / 10.0) - 180.0
    
    def updateTarget(self, target):
        self.setHover(500+target/10.)
        print "updateTarget"
    def updateBaro(self, asl):
        self.setBaro(500+asl/10.) 
        print "updateBaro"
    
    def changeValue(self, value):

        self.c.updateBW.emit(value)
        self.update()

        
    @pyqtSlot(float)    
    def setValue(self, value):
        super(AttitudeIndicator, self).updateRoll(float(value))
        
    @property
    def value(self):
        pass
    
    @value.setter
    def value(self, value):
        if type(value) is str:
            self.setPitch(float(value))
        else:
            self.setRoll(float(value))
        
    def valueSetter(self,value):
        self.value = (float(value)) 
        
    def getValue(self):
        return 0
      
    Value = QtCore.pyqtProperty(float,fget=getValue,fset=valueSetter) 
    
    @value.setter
    def setLabel(self, text):
        self.pitch = text
        self.setPitch(text)
    @property    
    def getLabel(self):
        return self.__label
    label = QtCore.pyqtProperty(str, getLabel, setLabel)







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





class Instruments(Widget, QtGui.QWidget):
    def __init__(self,parent = None):
         Widget.__init__(self)
         QtGui.QWidget.__init__(self,parent)
         self.ai = AttitudeIndicator()
         self.compass = WidgetBussola()
         
         layout = QtGui.QVBoxLayout(self)
         #layout.setMargin(0)
         #layout.setSpacing(0)
         layout.addWidget(self.compass)
         layout.addWidget(self.ai)
         
         print "Descomentar"
         self.ptoSerial = None
         self.timer = QtCore.QTimer()       
         self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.timerEvent)
         self.timer.start(1)
         """
         self.ptoSerial = serial.Serial('/dev/ttyACM1',  115200,  timeout = 1)
         
         """





    def decodeData(self):
        data = self.ptoSerial.readline()
        words = None
        print "Data:", data
        if data.find("!ANG:") != -1:          # filter out incomplete (invalid) lines
            line = data.replace("!ANG:","")   # Delete "!ANG:"
            print line                    # Write to the output log file
            words = string.split(line,",")    # Fields split
            if len(words) > 2:
                try:
                    roll = float(words[0])*grad2rad
                    pitch = float(words[1])*grad2rad
                    yaw = float(words[2])
                except:
                    print "Invalid line"
        
        return float(words[0]), float(words[1]),float(words[2])

    def timerEvent(self):
        angX, gradY, yaw = self.decodeData() 
        self.ai.updateRoll(angX)
        self.ai.updatePitch(gradY) 
        self.compass.value = yaw
        
        
    
           

  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    attitude = Instruments()
    #attitude.updatePitch(60)
    #print attitude.pitch
    layout.addWidget(attitude)
    
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
