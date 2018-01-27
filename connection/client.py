# -*- coding: utf-8 -*-
#https://qiita.com/nadechin/items/28fc8970d93dbf16e81b

import socket
import time

#hostの確認の仕方…hostname -i
host = "127.0.1.1"
port = 1111 #適当なポード番号

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #objectの作成

#socket.AF_INETにおいては、connect(address)として、address=(host,port)が利用される
client.connect((host, port))
'''
sendでメッセージを送る
python2から3の変更によって、str型とbytes型の区別を明確化しなければならなくった。これはpython2で可能
'''
msg = "abcde"
client.send(msg) #適当なデータを送信

response = client.recv(4096) #レシーブは適当な2進数にします（大きすぎるとダメ）

print(response)
