# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doisWidget_Widget.ui'
#
# Created: Mon Jun  1 11:01:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys, os
from PyQt4 import QtGui, QtCore

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(269, 526)
        self.dial_3Widget_2 = Dial_3(Form)
        self.dial_3Widget_2.setGeometry(QtCore.QRect(20, 250, 234, 234))
        self.dial_3Widget_2.setMaxValue(1000)
        self.dial_3Widget_2.setProperty("StepScale", 50)
        self.dial_3Widget_2.setObjectName(_fromUtf8("dial_3Widget_2"))
        self.dial_3Widget = Dial_3(Form)
        self.dial_3Widget.setGeometry(QtCore.QRect(20, 10, 234, 234))
        self.dial_3Widget.setMaxValue(1000)
        self.dial_3Widget.setProperty("StepScale", 50)
        self.dial_3Widget.setObjectName(_fromUtf8("dial_3Widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.dial_3Widget_2.setToolTip(_translate("Form", "Dial Widget 3", None))
        self.dial_3Widget_2.setWhatsThis(_translate("Form", "SCADA Dial 3", None))
        self.dial_3Widget.setToolTip(_translate("Form", "Dial Widget 3", None))
        self.dial_3Widget.setWhatsThis(_translate("Form", "SCADA Dial 3", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

