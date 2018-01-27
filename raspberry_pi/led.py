#!/usr/bin/env python
# -*- coding:utf-8 -*-

#http://www.hiramine.com/physicalcomputing/raspberrypi/rpigpio_blink.html
###if use python3, you can use WEBIOPi

import RPi.GPIO as GPIO
import time

LEDPIN = 24

'''
GND(PIN3) 
|
LED (-)
|
LED(+)
|
R (200)
|
GPIO24
'''

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
'''
setmode .. . which mode do you use???
BCM ... the number is "GPIO 's  number"
BOARD ... the number is "pin number"
'''

GPIO.setup(LEDPIN,GPIO.OUT)
'''
LEDPIN is the pin you use
OUT means that is output
in means that is in
'''

while 1:
    GPIO.output(LEDPIN,True)
    '''
    same meaning    True  GPIO.HIGH    1
    same meaning    False  GPIO.LOW    0

    if you use input
    input_val = GPIO.input(channel)
    '''

    
    time.sleep(1.0)
    GPIO.output(LEDPIN,False)
    time.sleep(1.0)

    '''
    if you finish the operation...
    GPIO.cleanup()
    or
   GPIO.cleanup(channel)
    '''
    
