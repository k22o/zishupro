#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Python2

import RPi.GPIO as GPIO
#import socket
import time
import bluetooth

#bluetooth通信の設定
port1 = 1#port番号
sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#for python2
sock1.bind(("",port1))#バインドする
sock1.listen(10)



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

    try:
        sock1_client,addr1_client= sock1.accept()#情報を得る
        print ("success to connect!")

        bin_data = sock1_client.recv(1024)
        receive  = bin_data.decode('utf-8')

        if receive == 'start':

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
        GPIO.cleanup()
