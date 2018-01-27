# -*- coding:utf-8 -*-

##python2で実行すること！

import bluetooth
import time
port = 20000

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケットを作る
sock.bind(("",port))#バインドする
sock.listen(10)

try:
    sock_client,addr_client= sock.accept()#情報を得る
    print("success connection!")

    while(1):

        data = sock_client.recv(1024)
        data_read = data.decode('utf-8')
        print ("get data ...{}".format(data_read))

except:
    print ("close")
    sock_client.close()
    sock.close()
