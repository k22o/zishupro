# -*- coding: utf-8 -*-
#ラズパイ側で動かす

import sys,time,os
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
out_size = 10

def input_search(y):

    if y == 0:
        return "omura"
    elif y == 1:
        return "mori"
    elif y == 2:
        return "yamada"


if __name__=='__main__':

    #モデルの設定
    model = cnn.cnn()

    #最適化設定
    optimizer = optimizers.Adam()
    optimizer.setup(model)#最適化

    cap = cv2.VideoCapture(0)#キャプチャ設定
    serializers.load_npz("face_CNN.npz",model)

    while(1):

        ret,frame = cap.read()
        if ret==False:
            break

        frame = cv2.flip(frame,1)#反転
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray,(80,45))
        roi  = np.array([gray/255.0])
        
        y = cnn.exe_CNN(model,roi)
        name = input_search(y)
        print ("{}".format(name))

        cv2.imshow("gray",frame)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
