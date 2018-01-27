# -*- coding: utf-8 -*-

import sys,time,os,cv2
import numpy as np
import chainer
#GPUを利用した高速計算を可能にする
##本環境ではうまく使えなかった
from chainer import cuda

#Functionクラス…フォワード・バックワードなどの計算に関するクラス
import chainer.functions as F
#Linkクラス…重みやバイアスなどのパラメータを持つクラス。Functionクラスの関数使える
import chainer.links as L
#誤差逆伝搬法など、最適化のためのクラス
from chainer import optimizers
from chainer import serializers
from chainer import Variable

import matplotlib.pyplot as plt

#取り込む画像の画素数
img_width = 80
img_height = 45
img_size = img_width * img_height

#出力サイズ
#out_size = 10
out_size = 3

#パスの設定
#dataset.pyを用いて作成したファイルを読み込む
'''
data_train=np.load("fingpic_data_train.npy")
data_test=np.load("fingpic_data_test.npy")
label_train=np.load("fingpic_label_train.npy")
label_test=np.load("fingpic_label_test.npy")
'''
data_train=np.load("facepic_data_train.npy")
data_test=np.load("facepic_data_test.npy")
label_train=np.load("facepic_label_train.npy")
label_test=np.load("facepic_label_test.npy")

n_epoch = 4#繰り返し回数
batch_size = 10#バッチサイズ
N = data_train.shape[0]#訓練データの数
N_test = data_test.shape[0]#テストデータの数


'''
#GPUを用いるときには記述する
gpu_flag = 0
if gpu_flag >= 0:
    cuda.check_cuda_available()
xp = cuda.cupy if gpu_flag >= 0 else np
'''


#Chainクラス…ニューラルネットワークの各要素をつなぐためのクラス。Linkの子クラス
#class CNN にて、ニューラルネット内を規定する
#https://qiita.com/icoxfog417/items/96ecaff323434c8d677b

class cnn(chainer.Chain):

    #各層の条件などを定める
    def __init__(self):
        super(cnn,self).__init__(
            conv1 = L.Convolution2D(1,20,5),
            conv2 = L.Convolution2D(20,50,5),
            conv3 = L.Convolution2D(50,70,5),
            link1 = L.Linear(1470,1000),
            link2 = L.Linear(1000,3),

        )
        '''
        link ... 各層間の全結合層についての規定
        conv ... 畳み込み層についての規定
        Convolution2D ... (入力チャンネル,出力チャンネル,フィルタサイズ,stride=,pad=,)として、畳込み層における計算をしてくれるLinkクラスの関数。
        stride = ストライド幅。（小さいほうが良い。入力画像サイズとの兼ね合いか？）
        pad = パディング幅。（ H/2H/2 の少数切り捨てにすることが多い）
        linear ... (入力,出力) 全結合。重みおよびバイアスが関連する
        '''

    #フォワード計算・プーリングの処理を行う.
    def forward(self,data):
        h = F.max_pooling_2d(F.relu(self.conv1(data)),2)
        h = F.max_pooling_2d(F.relu(self.conv2(h)),2)
        h = F.max_pooling_2d(F.relu(self.conv3(h)),2)
        h = F.relu(self.link1(h))
        h = F.softmax(self.link2(h))
        return h


###訓練データ
def train_CNN(data_train,label_train,optimizer):

    print("start trainig")

    for epoch in range(n_epoch):

        perm = np.random.permutation(N)#初期値
        sum_acc = 0
        sum_loss = 0

        for i in range(0,N,batch_size):

            '''
            GPU使用時にはこっちらしい
            x = Variable(xp.asarray(data_train[perm[i:i+batch_size]]))
            t = Variable(xp.asarray(label_train[perm[i:i+batch_size]]))
            '''

            x = Variable(np.array(data_train[perm[i:i+batch_size]]))
            t = Variable(np.array(label_train[perm[i:i+batch_size]]))
            y = model.forward(x)#フォワード計算をする

            model.zerograds()  #勾配を初期化
            loss = F.softmax_cross_entropy(y,t) #クロスエントロピーの算出
            acc = F.accuracy(y,t)#正答率の算出
            loss.backward()#勾配の計算
            optimizer.update()#パラメータの更新
            sum_loss += loss.data*batch_size
            sum_acc += acc.data*batch_size

        print("epoch:{}, loss:{}, acc:{}".format(epoch,sum_loss/N,sum_acc/N))


###テスト用
def test_CNN(data_train,label_train,data_test,label_test,optimizer):

    print ("start test")
    train_CNN(data_train,label_train,optimizer)

    cnt = 0
    for i in range(len(data_test)):

        #GPU使用時にはこっちらしい
        #x = Variable(xp.asarray([label_test[i]], dtype=np.float32))

        x = Variable(np.array([data_test[i]], dtype=np.float32))
        t = label_test[i]
        y = model.forward(x)
        y = np.argmax(y.data[0])#最も大きい値のindexを返す
        if t == y:
            cnt += 1

    print("accuracy: {}".format(100*cnt/N_test))


###他のプログラムにて、この重みを使って解析するとき
def exe_CNN(model,input_data):

    #GPU使用時
    #x = Variable(xp.asarray([inputdata], dtype=np.float32))

    x = Variable(np.array([input_data], dtype=np.float32))
    y = model.forward(x)
    y = np.argmax(y.data[0])
    return y


if __name__=='__main__':

    #モデルの設定
    model = cnn()
    '''
    #GPU使用時
    if gpu_flag >= 0:
        cuda.get_device(gpu_flag).use()
        model.to_gpu()
    '''

    #最適化設定
    optimizer = optimizers.Adam()
    optimizer.setup(model)#最適化

    #テストの実行
    test_CNN(data_train,label_train,data_test,label_test,optimizer)

    #if you save
    #serializers.save_npz("finger_CNN.npz",model)
    serializers.save_npz("face_CNN.npz",model)
    print("model is saved")
