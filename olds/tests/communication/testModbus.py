# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:58:46 2015

@author: root
"""
"""
from comm import COMM
arduino = COMM(type="Modbus",port='/dev/ttyACM0', adress=1).create()
print arduino
print "#################\n"
print arduino.mode
#print arduino.read_register(0)
"""

import minimalmodbus
arduino = minimalmodbus.Instrument('/dev/ttyACM0', 1)
arduino.serial.baudrate = 9600

print arduino
print "#################\n"
print arduino.mode
                
msg = input("Intensidade do led(0-255): ")
while (0 <= msg <= 255):    
    
    ligado = arduino.read_register(0)
    intensidade = arduino.read_register(1)
    if ligado == 1:
        print u"O Led estava ligado com intensidade {}.".format(intensidade)
    else:
        print u"O Led estava desligado com intensidade {}.".format(intensidade)
    arduino.write_register(1,msg)
    intensidade = arduino.read_register(1)
    print u"A nova intensidade do Led é {}.".format(intensidade)

    msg = input("Intensidade do led(0-255): ")
    if msg is 1:
        arduino.write_register(0,1)
    elif msg is 200:
        arduino.write_register(0,0)






"""
#!usr/bin/env python
from math import pi,sqrt,acos

import subprocess
import time
import urllib
import httplib
import minimalmodbus
import time
import serial

instrument = minimalmodbus.Instrument('/dev/ttyACM0',1) 	# Nom du port et adresse modbus // port série de raspberry = ttyAMA0 // port usb = ttyUSB0
instrument2 = minimalmodbus.Instrument('/dev/ttyACM0',2) 	# Nom du port et adresse modbus // port série de raspberry = ttyAMA0 // port usb = ttyUSB0


instrument.serial.baudrate 					= 19200
instrument.serial.bytesize 					= 8
instrument.serial.parity 					= serial.PARITY_NONE
instrument.serial.stopbits 					= 1
instrument.serial.timeout 					= 1                		# secondes
instrument.mode								= minimalmodbus.MODE_RTU 	# rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument.debug 							= False
instrument.serial.xonxoff					= True
instrument.serial.rtscts					= False
instrument.serial.dsrdtr					= False
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL	= True


instrument2.serial.baudrate 				= 19200
instrument2.serial.bytesize 				= 8
instrument2.serial.parity 					= serial.PARITY_NONE
instrument2.serial.stopbits 				= 1
instrument2.serial.timeout 					= 1                		# secondes
instrument2.mode							= minimalmodbus.MODE_RTU 	# rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument2.debug 							= False
instrument2.serial.xonxoff					= True
instrument2.serial.rtscts					= False
instrument2.serial.dsrdtr					= False

usb1_on = True
usb2_on = True


if instrument.debug == True:
	print instrument

# Lecture d'un registre
while 1:
	if usb2_on == True :
		try:
	#		test_reg = instrument.read_register(1,0)		
	#		print test_reg
	#		test_reg = instrument.read_register(1,0)
	#		print test_reg
			print "Registres de l'ID 1 USB"
			test_reg = instrument2.read_registers(0,10,4)		# lecture plusieurs registres,( registre de départ, nb de registres à lire (max 10), décimales)
			print test_reg
	#		test_reg = instrument2.read_registers(0,2,3)
	#		print test_reg
			time.sleep (1)

			
		except:
			print ("error USB1 -----------------------")
			time.sleep (1)
		
		
	if usb1_on == True :
		try:
	#		test_reg = instrument.read_register(1,0)		
	#		print test_reg
	#		test_reg = instrument.read_register(1,0)
	#		print test_reg
			print "Registres de l'ID 2 USB"
			test_reg = instrument.read_registers(0,10,4)		# lecture plusieurs registres,( registre de départ, nb de registres à lire (max 10), décimales)
			print test_reg
	#		test_reg = instrument.read_registers(10,10,4)
	#		print test_reg
			time.sleep (1)
			
		except:
			print ("error usb 2 ------------------------------")
			time.sleep (8)
"""	