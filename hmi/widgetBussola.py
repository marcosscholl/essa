# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QwtCompass.ui'
#
# Created: Sat Feb 08 00:29:14 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


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
    

class Ui_Form(Qt.QFrame):
    
    def setupUi(self, Form ):
        
        
        compass = Qwt.QwtCompass()
        
        palette = compass.palette()
        #Cor Interna Bussola
        palette.setColor(compass.backgroundRole(), Qt.Qt.darkCyan)
        compass.setPalette(palette)
        
        palette = Qt.QPalette()
        for colorRole in colorRoleList:
            palette.setColor(colorRole, Qt.QColor())
        palette.setColor(
            Qt.QPalette.Base,
            #Alterando uma pouco a cor, mais forte ou mais fraco, depende do valor
            compass.palette().color(compass.backgroundRole()).light(105))
        palette.setColor(
            #Cor de fundo do corculo da agulha
            Qt.QPalette.Foreground,
            palette.color(Qt.QPalette.Base))


        #Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(400, 300)
        #compass.setGeometry(QtCore.QRect(100, 40, 200, 200))
        """
        compass.setGeometry(QtCore.QRect(100, 40, 200, 200))
        compass.setLineWidth(4)
        compass.setObjectName(_fromUtf8("Compass"))
        """
        compass.setLineWidth(2)
        compass.setFrameShadow(Qwt.QwtCompass.Raised)
        compass.setScaleTicks(0, 0, 2)
       
        compass.setScaleOptions( Qwt.QwtDial.ScaleTicks |  Qwt.QwtDial.ScaleLabel | 
            Qwt.QwtDial.ScaleBackbone)
        compass.setLabelMap({0.0: "N",
                                 45.0: "ne",
                                 90.0: "E",
                                 135.0: "se",
                                 180.0: "S",
                                 225.0: "so",
                                 270.0: "O",
                                 315.0: "no"})
        compass.setScale(72,0, 0)
        
        compass.setNeedle(Qwt.QwtCompassMagnetNeedle(
        Qwt.QwtCompassMagnetNeedle.TriangleStyle,
            Qt.Qt.white,
            Qt.Qt.red))
        compass.setValue(35.0)
        
        

        newPalette = compass.palette()
    
        
        ##Criando Cor de fundo para Bussola
        
        for colorRole in colorRoleList:
            if palette.color(colorRole).isValid():
                for colorGroup in colorGroupList:
                    newPalette.setColor(
                        colorGroup, colorRole, palette.color(colorRole))
        
        compass.setPalette(newPalette)
        
        return compass
    
        
        
                
                
        
        #QtCore.QMetaObject.connectSlotsByName(Form)
        
        


class WidgetBussola(QtGui.QWidget):
    def __init__(self, parent=None):
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

if __name__ == '__main__':
    import sys
    
    # BUSSOLA
    app = QtGui.QApplication(sys.argv)
    bussola = WidgetBussola()
    
   
    #bussola.setGeometry(1050, 100, 300, 300)  
    
    bussola.show()
    sys.exit(app.exec_())
