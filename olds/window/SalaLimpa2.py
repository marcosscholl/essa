# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalaLimpa2.ui'
#
# Created: Mon Jun 22 13:37:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(836, 506)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.onOffButton_3 = OnOffButton(self.centralwidget)
        self.onOffButton_3.setGeometry(QtCore.QRect(20, 60, 253, 300))
        self.onOffButton_3.setTextTrue(_fromUtf8(""))
        self.onOffButton_3.setTextFalse(_fromUtf8(""))
        self.onOffButton_3.setObjectName(_fromUtf8("onOffButton_3"))
        self.display = Display(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(240, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setObjectName(_fromUtf8("display"))
        self.led_3 = Led(self.centralwidget)
        self.led_3.setGeometry(QtCore.QRect(101, 370, 91, 88))
        self.led_3.setObjectName(_fromUtf8("led_3"))
        self.onOffButton_4 = OnOffButton(self.centralwidget)
        self.onOffButton_4.setGeometry(QtCore.QRect(289, 60, 253, 300))
        self.onOffButton_4.setTextTrue(_fromUtf8(""))
        self.onOffButton_4.setTextFalse(_fromUtf8(""))
        self.onOffButton_4.setObjectName(_fromUtf8("onOffButton_4"))
        self.led_4 = Led(self.centralwidget)
        self.led_4.setGeometry(QtCore.QRect(370, 370, 91, 88))
        self.led_4.setObjectName(_fromUtf8("led_4"))
        self.onOffButton_5 = OnOffButton(self.centralwidget)
        self.onOffButton_5.setGeometry(QtCore.QRect(559, 60, 253, 300))
        self.onOffButton_5.setTextTrue(_fromUtf8(""))
        self.onOffButton_5.setTextFalse(_fromUtf8(""))
        self.onOffButton_5.setObjectName(_fromUtf8("onOffButton_5"))
        self.led_5 = Led(self.centralwidget)
        self.led_5.setGeometry(QtCore.QRect(640, 370, 91, 88))
        self.led_5.setObjectName(_fromUtf8("led_5"))
        self.onOffButton = OnOffButton(self.centralwidget)
        self.onOffButton.setGeometry(QtCore.QRect(510, 10, 75, 29))
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.onOffButton_3.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton_3.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.onOffButton_3.setProperty("PathImageTrue", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/opened-2.png", None))
        self.onOffButton_3.setProperty("PathImageFalse", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/closed-2.png", None))
        self.display.setToolTip(_translate("MainWindow", "Display Widget", None))
        self.display.setWhatsThis(_translate("MainWindow", "Display SCADA", None))
        self.display.setText(_translate("MainWindow", "Sala Limpa", None))
        self.led_3.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led_3.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.onOffButton_4.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton_4.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.onOffButton_4.setProperty("PathImageTrue", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/opened-2.png", None))
        self.onOffButton_4.setProperty("PathImageFalse", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/closed-2.png", None))
        self.led_4.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led_4.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.onOffButton_5.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton_5.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))
        self.onOffButton_5.setProperty("PathImageTrue", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/opened-2.png", None))
        self.onOffButton_5.setProperty("PathImageFalse", _translate("MainWindow", "/home/scholl/Dropbox/Spyder/essa/images/closed-2.png", None))
        self.led_5.setToolTip(_translate("MainWindow", "Led Widget", None))
        self.led_5.setWhatsThis(_translate("MainWindow", "Led SCADA", None))
        self.onOffButton.setToolTip(_translate("MainWindow", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("MainWindow", "SCADA OnOffButton", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

