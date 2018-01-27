# -*- coding:utf-8 -*-

##python3で実行すること！

import socket
import time

port = 1#ポート名
addr = " "#アドレス

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)#ソケットを作る

sock.bind((addr,port))#バインドする
sock.listen(1)

try: 
    sock_client,addr_client= sock.accept()#情報を得る

    while(1):

        data = sock_client.recv(1024)
        data_read = data.decode('utf-8')
        print ("get data ...{}".format(data_read))

except:
    print ("close")
    sock_client.close()
    sock.close()
