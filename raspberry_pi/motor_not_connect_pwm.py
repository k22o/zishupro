#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Python2

import RPi.GPIO as GPIO
#import socket
import time


#GPIOピン番号の設定
p11  = 27#23#右タイヤ 前進
p12  = 17#24#右タイヤ 後退
p21  = 24#17#左タイヤ 前進
p22  = 23#27#左タイヤ 後退


#GPIOの初期設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p11,GPIO.OUT)
GPIO.setup(p12,GPIO.OUT)
GPIO.setup(p21,GPIO.OUT)
GPIO.setup(p22,GPIO.OUT)


def deg_0():
    
    GPIO.output(p11,0)
    GPIO.output(p12,0)
    GPIO.output(p21,1)
    GPIO.output(p22,0)    
    
    print("0 deg") 

    
def deg_45():

    GPIO.output(p11,0)
    GPIO.output(p12,0)
    GPIO.output(p21,1)
    GPIO.output(p22,0)    
    
    print("45 deg") 

    
def deg_90():

    GPIO.output(p11,1)
    GPIO.output(p12,0)
    GPIO.output(p21,1)
    GPIO.output(p22,0)    
    
    print("90 deg")

    
def deg_135():

    GPIO.output(p11,1)
    GPIO.output(p12,0)
    GPIO.output(p21,0)
    GPIO.output(p22,0)    

    print("135 deg")

    
def deg_180():

    GPIO.output(p11,1)
    GPIO.output(p12,0)
    GPIO.output(p21,0)
    GPIO.output(p22,0)    

    print("180 deg")

    
def deg_225():

    GPIO.output(p11,0)
    GPIO.output(p12,1)
    GPIO.output(p21,0)
    GPIO.output(p22,0)    

    print("225 deg")

    
def deg_270():

    GPIO.output(p11,0)
    GPIO.output(p12,1)
    GPIO.output(p21,0)
    GPIO.output(p22,1)    
    
    print("270 deg")

    
def deg_315():

    GPIO.output(p11,0)
    GPIO.output(p12,0)
    GPIO.output(p21,0)
    GPIO.output(p22,1)    

    print("315 deg")


def stop():

    GPIO.output(p11,0)
    GPIO.output(p12,0)
    GPIO.output(p21,0)
    GPIO.output(p22,0)    
    #GPIO.cleanup() 
    print("stop") 

    

if __name__ == '__main__':

    time.sleep(1)
    deg_90()
    time.sleep(1)
    deg_270()
    time.sleep(1)
    stop()
    
    GPIO.cleanup()

                    

 


    
    
    
