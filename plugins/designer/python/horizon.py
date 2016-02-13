# -*- coding: utf-8 -*-
"""
Created on Mon Feb 03 20:24:26 2014

@author: MarcosScholl
"""

if 0:
    import sip
    sip.settracemask(0x3f)

import math
import random
import sys
from PyQt4 import Qt, QtGui
import PyQt4.Qwt5 as Qwt


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


class AttitudeIndicatorNeedle(Qwt.QwtDialNeedle):

    def __init__(self, color):
        Qwt.QwtDialNeedle.__init__(self)
        palette = Qt.QPalette()
        for colourGroup in colorGroupList:
            ## Cor dos Indicadores QtGui.QColor(255, 0, 0)
            palette.setColor(colourGroup, Qt.QPalette.Text, QtGui.QColor(255, 255, 255))
        self.setPalette(palette)

    # __init__()

    def draw(self, painter, center, length, direction, cg):
        direction *= math.pi / 180.0
        triangleSize = int(round(length * 0.1))

        painter.save()

        p0 = Qt.QPoint(center.x() + 1, center.y() + 1)
        p1 = Qwt.qwtPolar2Pos(p0, length - 2 * triangleSize - 2, direction)

        pa = Qt.QPolygon([
            Qwt.qwtPolar2Pos(p1, 2 * triangleSize, direction),
            Qwt.qwtPolar2Pos(p1, triangleSize, direction + math.pi/2),
            Qwt.qwtPolar2Pos(p1, triangleSize, direction - math.pi/2),
            ])

        color = self.palette().color(cg, Qt.QPalette.Text)
        painter.setBrush(color)
        painter.drawPolygon(pa)

        painter.setPen(Qt.QPen(color, 3))
        painter.drawLine(
            Qwt.qwtPolar2Pos(p0, length - 2, direction + math.pi/2),
            Qwt.qwtPolar2Pos(p0, length - 2, direction - math.pi/2))

        painter.restore()

    # draw()

# class AttitudeIndicatorNeedle


class AttitudeIndicator(Qwt.QwtDial):

    def __init__(self, *args):
        Qwt.QwtDial.__init__(self, *args)
        self.__gradient = 0.0
        self.setMode(Qwt.QwtDial.RotateScale)
        self.setWrapping(True)
        self.setOrigin(270.0)
        self.setScaleOptions(Qwt.QwtDial.ScaleTicks)
        self.setScale(0, 0, 30.0)
        self.setNeedle(AttitudeIndicatorNeedle(
            self.palette().color(Qt.QPalette.Text)))
            

    # __init__()

    def angle(self):
        return self.value()

    # angle()
    
    def setAngle(self, angle):
        self.setValue(angle)

    # setAngle()

    def gradient(self):
        return self.__gradient

    # gradient()

    def setGradient(self, gradient):
        self.__gradient = gradient

    # setGradient()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Plus:
            self.setGradient(self.gradient() + 0.05)
        elif event.key() == Qt.Qt.Key_Minus:
            self.setGradient(self.gradient() - 0.05)
        else:
            Qwt.QwtDial.keyPressEvent(self, event)

    # keyPressEvent()
    # Faz a Escala de Angulação  acompanhar a rotação do horizonte
    def drawScale(self, painter, center, radius, origin, minArc, maxArc):
        dir = (360.0 - origin) * math.pi / 180.0
        offset = 4
        p0 = Qwt.qwtPolar2Pos(center, offset, dir + math.pi)

        w = self.contentsRect().width()

        # clip region to swallow 180 - 360 degrees
        pa = []
        pa.append(Qwt.qwtPolar2Pos(p0, w, dir - math.pi/2))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], 2 * w, dir + math.pi/2))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], w, dir))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], 2 * w, dir - math.pi/2))

        painter.save()
        painter.setClipRegion(Qt.QRegion(Qt.QPolygon(pa)))
        
        Qwt.QwtDial.drawScale(
            self, painter, center, radius, origin, minArc, maxArc)
        painter.restore()
    
    # drawScale()
    # Cria o Horizonte.
    def drawScaleContents(self, painter, center, radius):
        # Cria a escala azul
        ############################################################
        dir = 360 - int(round(self.origin() - self.value()))
        arc = 90 + int(round(self.gradient() * 90))
        skyColor = Qt.QColor(38, 151, 221)
        painter.save()
        painter.setBrush(skyColor)
        
        painter.drawChord(
            self.scaleContentsRect(), (dir - arc)*16, 2*arc*16)
        # Cria a escala marrom, abaixo da escala azul
        ############################################################
        dir2 = 180 - int(round(self.origin() - self.value()))
        arc2 = 90 + int(round(self.gradient() * 90))
        skyColor2 = Qt.QColor(170, 85, 0)
        #painter.save()
        painter.setBrush(skyColor2)
        
        painter.drawChord(
            self.scaleContentsRect(), (dir2 - arc2 )*16, 2*arc2*16)
        ############################################################
        
        painter.restore()

    # drawScaleContents()
    
# class AttitudeIndicator


class HorizonArtifictialWidget(Qt.QFrame):
    
    def __init__(self, *args):
        Qt.QFrame.__init__(self, *args)
        
        
        self.setPalette(
            self.__colorTheme(Qt.QColor(Qt.Qt.darkGray).dark(150)))
        
       
        
        layout = Qt.QGridLayout(self)
        
       
        layout.addWidget(self.__createDial(),0,1)
        
        #self.__speed_offset = 0.8
        self.__angle_offset = 0.05
        #self.__gradient_offset = 0.005
        
            
    # __init__()
    
    def __colorTheme(self, base):
        background = base.dark(150)
        foreground = base.dark(200)
        
        mid = base.dark(110)
        dark = base.dark(170)
        light = base.light(170)
        text = foreground.light(800)

        palette = Qt.QPalette()
        for colorGroup in colorGroupList:
            # Cor do Corpo do Widget
            palette.setColor(colorGroup, Qt.QPalette.Base, dark)
            palette.setColor(colorGroup, Qt.QPalette.Background, background)
            # Deixa a borda de uma cor mais escura
            palette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            # Deixa Cor uniforme das bordas do widget
            palette.setColor(colorGroup, Qt.QPalette.Light, light)
            #palette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            # Cor dos indicadores
            palette.setColor(colorGroup, Qt.QPalette.Text, text)
            palette.setColor(colorGroup, Qt.QPalette.Foreground, foreground)
        
        return palette
    
    # __colorTheme()

    def __createDial(self):
        dial = None
        self.__ai = AttitudeIndicator(self)
        gradientTimer = Qt.QTimer(self.__ai)
        """
        gradientTimer.connect(gradientTimer,
                              Qt.SIGNAL('timeout()'),
                                    self.changeGradient)
        """
        #gradientTimer.start(100)
        
        angleTimer = Qt.QTimer(self.__ai)
        angleTimer.connect(
        angleTimer, Qt.SIGNAL('timeout()'), self.changeAngle)
        angleTimer.start(1)
        dial = self.__ai
        dial.setToolTip("Horizonte Artificial")
        
        if dial:
            #dial.setReadOnly(True)
            dial.scaleDraw().setPenWidth(3)
            dial.setLineWidth(3)
            #dial.setFrameShadow(Qwt.QwtDial.Sunken)

        return dial
    
    
    # __createDial()

    
    def changeAngle(self):
        angle = self.__ai.angle()
        if angle > 180.0:
            angle -= 360.0

        if ((angle < -35.0 and self.__angle_offset < 0.0 )
            or (angle > 35.0 and self.__angle_offset > 0.0)):
            self.__angle_offset = -self.__angle_offset
            
        self.__ai.setAngle(angle + self.__angle_offset)
    

if __name__ == '__main__':
    import sys
    
    # BUSSOLA
    app = QtGui.QApplication(sys.argv)
    bussola = HorizonArtifictialWidget()
    
   
    #bussola.setGeometry(1050, 100, 300, 300)  
    

    bussola.show()
    sys.exit(app.exec_())
 