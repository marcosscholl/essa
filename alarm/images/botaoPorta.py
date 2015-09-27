# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'botaoPorta.ui'
#
# Created: Mon Jun 15 14:10:20 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data import *
from aware import *
from hmi import *
from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(614, 486)
        self.onOffButton = OnOffButton(Form)
        self.onOffButton.setGeometry(QtCore.QRect(70, 100, 321, 351))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/scholl/Dropbox/Spyder/essa/images/closed.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("/home/scholl/Dropbox/Spyder/essa/images/opened.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.onOffButton.setIcon(icon)
        self.onOffButton.setIconSize(QtCore.QSize(350, 350))
        self.onOffButton.setAutoDefault(False)
        self.onOffButton.setDefault(False)
        self.onOffButton.setFlat(False)
        self.onOffButton.setObjectName(_fromUtf8("onOffButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.onOffButton.setToolTip(_translate("Form", "OnOffButton Widget", None))
        self.onOffButton.setWhatsThis(_translate("Form", "SCADA OnOffButton", None))

#import door_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

