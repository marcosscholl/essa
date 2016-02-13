from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon

"""
@author: MarcosScholl
"""


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from aware import *

    
class Widget(Subject):
    def __init__ (self):
        Subject.__init__(self)
        pass

        
class Video(Widget, QtGui.QWidget):

    def __init__(self,parent = None):
        Widget.__init__(self)
        QtGui.QWidget.__init__(self,parent)
        self.media = Phonon.MediaObject(self)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(400, 400)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.video, 0)
        self.handleButton()

    def handleButton(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            path = "/home/scholl/Downloads/ROV-Exploration.mp4"
            if path:
                self.media.setCurrentSource(Phonon.MediaSource(path))
                self.media.play()

       
"""
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Video()
    window.media.play()
    window.show()
    sys.exit(app.exec_())
"""