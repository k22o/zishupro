# -*- coding:utf-8 -*-

# python2!!
import bluetooth
import time

addr = "B8:27:EB:95:A6:C0"#ラズパイアドレス
port2 = 2 #ポート

sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケット作成
sock2.connect((addr, port2))#つなぐ
print("success connection")

while(1):

    data = sock2.recv(1024)#データ受信(バイナリ列)
    data_read = data.decode('utf-8')#string型に治す
    print ("get data ...{}".format(data_read))

    #msg_bin = msg.encode('utf-8')#binに変換
    #sock.send(msg_bin)
    #print("send msg...{}".format(msg))


sock2.close()
