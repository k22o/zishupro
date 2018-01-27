#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Python2

import RPi.GPIO as GPIO
#import socket
import time
#import bluetooth

#bluetooth通信の設定
#port1 = 1#port番号
#addr = "B8:27:EB:95:A6:C0"#アドレス   
#sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#for python2
#sock1.bind(("",port1))#バインドする
#sock1.listen(10)



#GPIOピン番号の設定
INPUT11  = 27#27#23#右タイヤ 前進
INPUT12  = 17#17#24#右タイヤ 後退
INPUT21  = 24#17#左タイヤ 前進
INPUT22  = 23#27#左タイヤ 後退


#GPIOの初期設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT11,GPIO.OUT)
GPIO.setup(INPUT12,GPIO.OUT)
GPIO.setup(INPUT21,GPIO.OUT)
GPIO.setup(INPUT22,GPIO.OUT)

#GPIOのPWMの初期設定
p11 = GPIO.PWM(INPUT11,200)
p12 = GPIO.PWM(INPUT12,200)
p21 = GPIO.PWM(INPUT12,200)
p22 = GPIO.PWM(INPUT22,200)

#閾値の設定
thre1 = 30
thre2 = 40
thre3 = 70

def deg_0():
    
    p11.ChangeDutyCycle(thre1)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(thre3)
    p22.ChangeDutyCycle(0)
    
    print("0 deg") 

    
def deg_45():

    p11.ChangeDutyCycle(thre2)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(thre3)
    p22.ChangeDutyCycle(0)    
    
    print("45 deg") 

    
def deg_90():

    p11.ChangeDutyCycle(thre3)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(thre3)
    p22.ChangeDutyCycle(0)        
    
    print("90 deg")

    
def deg_135():

    p11.ChangeDutyCycle(thre3)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(thre2)
    p22.ChangeDutyCycle(0)

    print("135 deg")

    
def deg_180():

    p11.ChangeDutyCycle(thre3)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(thre1)
    p22.ChangeDutyCycle(0)

    print("180 deg")

    
def deg_225():

    p11.ChangeDutyCycle(0)
    p12.ChangeDutyCycle(thre3)
    p21.ChangeDutyCycle(0)
    p22.ChangeDutyCycle(thre2)

    print("225 deg")

    
def deg_270():

    p11.ChangeDutyCycle(0)
    p12.ChangeDutyCycle(thre2)
    p21.ChangeDutyCycle(0)
    p22.ChangeDutyCycle(thre2)
    
    print("270 deg")

    
def deg_315():

    p11.ChangeDutyCycle(0)
    p12.ChangeDutyCycle(thre2)
    p21.ChangeDutyCycle(0)
    p22.ChangeDutyCycle(thre3)
    print("315 deg")


def stop():

    p11.ChangeDutyCycle(0)
    p12.ChangeDutyCycle(0)
    p21.ChangeDutyCycle(0)
    p22.ChangeDutyCycle(0)
    #GPIO.cleanup() 
    print("stop") 

    

if __name__ == '__main__':
        
    p11.start(0)
    p12.start(0)           
    p21.start(0)
    p22.start(0)           

    stop()
    time.sleep(1)
    deg_90()
    time.sleep(1)
    deg_270()
    time.sleep(1)
    stop()
    print("fin")
            

    
    
