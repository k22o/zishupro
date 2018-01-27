# -*- coding:utf-8 -*-

# python3!!
import socket
import time


addr = "B8:27:EB:95:A6:C0"#アドレス
port = 1#ポート

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)#ソケット作成
sock.connect((addr, port))#ソケットをつなげる

while(1):
    msg = input()
    msg_bin = msg.encode('utf-8')#binに変換
    sock.send(msg_bin)
    print("send msg...{}".format(msg))
        
sock.close()
