# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:18:48 2015

@author: root
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150610-1100"
__status__ = "stable"
__license__ = "GPL"

import minimalmodbus
import pyfirmata as pyfirmata


class Arduino():
     
    @classmethod
    def create(self, **kwargs):
        if 'port' in kwargs:
            self._port = kwargs['port']
        else:
            self._port = '/dev/ttyACM0'
        if 'baudrate' in kwargs:
            self._baudrate = kwargs['baudrate']
        else:
            self._baudrate = 9600
        self._board = pyfirmata.Arduino(self._port)
        self._iterator = pyfirmata.util.Iterator(self._board)
        self._iterator.start()
        print self._board
        return self._board


class Modbus():
    @classmethod
    def create(self, **kwargs):
        self._board = None
        if 'port' in kwargs:
            self._port = kwargs['port']
        else:
            self._port = '/dev/ttyACM0'
        if 'baudrate' in kwargs:
            self._baudrate = kwargs['baudrate']
        else:
            self._baudrate = 9600
        if 'address' in kwargs:
            self._address = kwargs['address']
        else:
            self._address = 1
        
        if 'bytesize' in kwargs:
            self._bytesize = kwargs['bytesize']
        else:
            self._bytesize = None
        
        if 'parity' in kwargs:
            self._parity = kwargs['parity']
        else:
            self._parity = None
        if 'stopbits' in kwargs:
            self._stopbits = kwargs['stopbits']
        else:
            self._stopbits = None
        if 'timeout' in kwargs:
            self._timeout = kwargs['timeout']
        else:
            self._timeout = None
        if 'mode' in kwargs:
            self._mode = kwargs['mode']
        else:
            self._mode = None
               

        
        self._board = minimalmodbus.Instrument(self._port,self._address)
        self._board.serial.baudrate = self._baudrate
        
        if self._parity is not None:
            print "Seta Paridade"
            self._board.serial.parity = self._parity
        if self._bytesize is not None:
            print "Seta _bytesize"
            self._board.serial.bytesize = self._bytesize
        if self._stopbits is not None:
            print "Seta _stopbits"
            self._board.serial.stopbits = self._stopbits
        if self._timeout is not None:
            print "Seta _timeout"
            self._board.serial.timeout = self._timeout
        if self._mode is not None:
            print "Seta _mode"
            if self._mode is "RTU":
                self._board.mode = minimalmodbus.MODE_RTU
            elif self._mode is "ASCII":
                self._board.mode = minimalmodbus.MODE_ASCII
        

        return self._board
        
        #return comm == 'Modbus'


def COMM(**kwargs):
    if 'type' in kwargs:
        _type = kwargs['type']
    else:
        _type = None
        
    
    if _type is "Arduino":
        print "Arduino"
        return Arduino().create(**kwargs)
    elif _type is "Modbus":
        return Modbus().create(**kwargs)

