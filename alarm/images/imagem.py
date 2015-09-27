# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagem.ui'
#
# Created: Mon Jun 15 11:59:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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
        Form.resize(307, 296)
        self.kpixmapregionselectorwidget = KPixmapRegionSelectorWidget(Form)
        self.kpixmapregionselectorwidget.setGeometry(QtCore.QRect(0, 10, 281, 281))
        self.kpixmapregionselectorwidget.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/alert.png")))
        self.kpixmapregionselectorwidget.setObjectName(_fromUtf8("kpixmapregionselectorwidget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

from kpixmapregionselectorwidget import KPixmapRegionSelectorWidget
import imagem_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

