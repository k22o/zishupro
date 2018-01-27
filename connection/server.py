# -*- coding:utf-8 -*-
import socket

host = "127.0.1.1" #サーバーのホスト名
port = 1111 #クライアントと同じPORT

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(('',port)) #IPとPORTを指定してバインド
serversock.listen(10) #接続の待ち受け（キューの最大数を指定）

print ('Waiting for connections...')
clientsock, client_address = serversock.accept() #接続されればデータを格納

while True:
    rcvmsg = clientsock.recv(1024)
    print ('Received -> %s' % (rcvmsg))
    if rcvmsg == '':
        break
    print ('Type message...')
    s_msg = raw_input()
    if s_msg == '':
        break
    print ('Wait...')
    
    clientsock.sendall(s_msg) #メッセージを返します
clientsock.close()
