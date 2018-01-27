# -*- coding: utf-8 -*-
#ラズパイ側で動かす

import sys,time,os,bluetooth
import cv2
import numpy as np
import chainer
from chainer import cuda
import chainer.functions as F
import chainer.links as L
from chainer import optimizers
from chainer import serializers
from chainer import Variable
import cnn

img_width = 80
img_height = 45
img_size = img_width * img_height
#出力サイズ
out_size = 3


#addr = "B8:27:EB:95:A6:C0"#ラズパイアドレス
addr = "E8:B1:FC:E8:92:2E"#PC
port2 = 2 #ポート
sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケット作成
#sock2.connect((addr, port2))#ソケットをつなげる
sock2.bind(("",port2))
sock2.listen(10)

def input_search(y):
    if y == 0:
        return "dyson"
    elif y == 1:
        return "mori"
    elif y == 2:
        return "yamataku"



if __name__=='__main__':

    sock2_client,addr2_client = sock2.accept()
    
    #cnnの設定
    model = cnn.cnn()
    optimizer = optimizers.Adam()
    optimizer.setup(model)#最適
    serializers.load_npz("face_CNN.npz",model)
 
    cap = cv2.VideoCapture(0)#キャプチャ設定
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX#文字のフォント

    while(1):
        ret,frame = cap.read()
        if ret==False:
            break

        #グレースケール画像を用いて顔の検出 
        #frame = cv2.flip(frame,1)#反転
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3,5)

        
        #顔が検出されたらする作業
        if len(faces) > 0 :
            for (x, y, w, h) in faces:

                
                #frame画像に四角を表示
                #cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
                #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            

                #顔を切り取ってCNN
                roi = gray[y:y+h,x:x+w]
                roi = np.array([cv2.resize(roi,(img_width,img_height))/255.0])
                y = cnn.exe_CNN(model,roi)
                name = input_search(y)
 
                #人の名前を送信する
                name_bin = name.encode('utf-8')#binに変換
                sock2_client.send(name_bin)
                #print("send name...{}".format(name))
                
                #名前を表示
                #引数は、書き出し位置,font,fintsize,color
                #cv2.putText(frame,name,(x,y),font,3,(255,255,255))

        else :
            name = "not find"
            name_bin = name.encode('utf-8')#binに変換
            sock2_client.send(name_bin)
            #print(name)
                
        #cv2.imshow("frame",frame)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    sock2.close()
    sock2_client.close()
    cap.release()
    cv2.destroyAllWindows()
 
