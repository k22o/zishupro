#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Python2

import RPi.GPIO as GPIO
#import socket
import time
import bluetooth

#bluetooth通信の設定
port1 = 1#port番号
#addr = "B8:27:EB:95:A6:C0"#アドレス   
sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#for python2
sock1.bind(("",port1))#バインドする
sock1.listen(10)



#GPIOピン番号の設定
INPUT11  = 27#23#右タイヤ 前進
INPUT12  = 17#24#右タイヤ 後退
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
p11 = GPIO.PWM(INPUT11,50)
p12 = GPIO.PWM(INPUT12,50)
p21 = GPIO.PWM(INPUT12,50)
p22 = GPIO.PWM(INPUT22,50)

#閾値の設定
thre1 = 10
thre2 = 20
thre3 = 30

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
        
    try:
        sock1_client,addr1_client= sock1.accept()#情報を得る
        print ("success to connect!")

        bin_data = sock1_client.recv(1024)
        receive  = bin_data.decode('utf-8')

        if receive == 'start':
        
            p11.start(0)
            p12.start(0)           
            p21.start(0)
            p22.start(0)           
        
            while(1):
            
                bin_data = sock1_client.recv(1024)
                receive  = bin_data.decode('utf-8')
                print ("msg...{}".format(receive))
                
                #receive を受信データとして、その値に応じて実行関数を変える
                if receive == "deg_0":
                    deg_0()
                elif receive == "deg_45":
                    deg_45()
                elif receive == "deg_90":
                    deg_90()
                elif receive == "deg_135":
                    deg_135()
                elif receive == "deg_180":
                    deg_180()
                elif receive == "deg_225":
                    deg_225()
                elif receive == "deg_270":
                    deg_270()
                elif receive == "deg_315":
                    deg_315()
                elif receive == "stop":
                    stop()
                else:
                    print ("no match")

                #print ("get data ...{}".format(receive))
                
    except:
        print ("error")
        #sock1_client.close()
        sock1.close()


                    

 


    
    
    
