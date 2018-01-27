# -*- coding:utf-8 -*-

# python2!!
import bluetooth
import time


addr = "B8:27:EB:95:A6:C0"#アドレス
port = 20000 #ポート

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケット作成
sock.connect((addr, port))#ソケットをつなげる


while(1):

    msg =input()# "  "で入力
    msg_bin = msg.encode('utf-8')#binに変換
    sock.send(msg_bin)
    print("send msg...{}".format(msg))

    data = sock_client.recv(1024)


sock.close()
