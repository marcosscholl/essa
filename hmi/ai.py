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

from aware import *

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
        self.setPitch(pitch - 90)
        print "updatePitch:", pitch
        


    def updateRoll(self, roll):
        self.setRoll((roll / 10.0) - 180.0)
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
    
"""
if __name__ == "__main__":
    class Example(QtGui.QWidget):

        def __init__(self):
            super(Example, self).__init__()

            self.initUI()
            
        
        def initUI(self):

            vbox = QtGui.QVBoxLayout()
            
            
            self.wid = AttitudeIndicator()

            vbox.addWidget(self.wid)

            hbox = QtGui.QHBoxLayout()
            hbox.addLayout(vbox)

            


            self.setLayout(hbox)
            self.show()



    def main():

        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


    if __name__ == '__main__':
        main()
"""     
  
"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout()
    
    
    attitude = AttitudeIndicator()
    attitude.value = -1
    attitude.setLabel = -5
    #attitude.updatePitch(60)
    #print attitude.pitch
    layout.addWidget(attitude)
    
    
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
"""