"""
    Potenciometro -> Slide
    Boton -> Led
    Rueda -> Servo
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pyfirmata import Arduino, util, SERVO


class Form(QDialog):

    def __init__(self, app, parent=None):
        super(Form, self).__init__(parent)

        # Pyfirmata code
        self.potPin = 0
        self.servoPin = 9
        self.ledPin = 13
        self.board = Arduino('/dev/ttyACM0')

        iterator = util.Iterator(self.board)
        iterator.start()

        self.board.analog[self.potPin].enable_reporting()
        #self.board.digital[self.servoPin].mode = SERVO
        
        # PyQT Code
        servoLabel = QLabel("Servo")
        self.servoDial = QDial()
        self.servoDial.setMinimum(0)
        self.servoDial.setMaximum(180)
        self.servoPosition = 0

        potLabel = QLabel("Potenciometro")
        self.potSlider = QSlider()
        self.potSlider.setMinimum(0)
        self.potSlider.setMaximum(1000)

        ledLabel = QLabel("Led 13")
        self.ledButton = QPushButton('Light')

        grid = QGridLayout()
        grid.addWidget(servoLabel, 0, 0)
        grid.addWidget(potLabel, 0, 1)
        grid.addWidget(ledLabel, 0, 2)
        grid.addWidget(self.servoDial, 1, 0)
        grid.addWidget(self.potSlider, 1, 1)
        grid.addWidget(self.ledButton, 1, 2)
        self.setLayout(grid)

        self.connect(self.ledButton,
                SIGNAL("pressed()"), self.ledOn)
        self.connect(self.ledButton,
                SIGNAL("released()"), self.ledOff)

        #self.connect(self.servoDial,
                #SIGNAL("valueChanged(int)"), self.moveServo)

        self.connect(app,
                SIGNAL("lastWindowClosed()"), self.cleanup)

        self.timer = QTimer()
        self.timer.setInterval(500)

        self.connect(self.timer, SIGNAL("timeout()"), self.readPot)

        self.setWindowTitle("Arduino")

        self.timer.start()


    def ledOn(self):
        print "Led on"
        self.board.digital[self.ledPin].write(1)

    def ledOff(self):
        print "Led off"
        self.board.digital[self.ledPin].write(0)
    """
    def moveServo(self):
        position = self.servoDial.value()
        if abs(position - self.servoPosition) > 10:
            self.servoPosition = position
            print "Servo at position: %s" % position
            self.board.digital[self.servoPin].write(position)
    """
    def cleanup(self):
        print "cleanup"
        self.board.exit()

    def readPot(self):
        value = self.board.analog[self.potPin].read()
        if value is not None:
            position = value * 1000
            print "Read Pot: %s" % position
            self.potSlider.setValue(position)

app = QApplication(sys.argv)
form = Form(app)
form.show()
app.exec_()