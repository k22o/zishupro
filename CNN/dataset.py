# -*- coding: utf-8 -*-
#https://github.com/tommyfms2/face_prediction/blob/master/image2TrainAndTest.pyを参考に、一部改変

import numpy as np
from PIL import Image
import os
import cv2

#CNNデータセット作成用関数
#引数は、「パスとラベルのセット」「チャンネル数」「テストデータの数」
def img_cnn_TrainAndTest(pathsAndLabels, channels, test_num):

    allData = []

    #各ディレクトリに対して実行する(ディレクトリパス・ラベルのペア)
    for pathAndLabel in pathsAndLabels:
        path = pathAndLabel[0]
        label = pathAndLabel[1]
        imagelist = os.listdir(path)#ディレクトリ内の画像を取得
        for imgName in imagelist:
            real_path = os.path.join(path,imgName)
            allData.append([real_path, label])
    allData = np.random.permutation(allData)#シャッフル

    #白黒画像
    if channels == 1:
        imageData = []
        labelData = []

        for pathAndLabel in allData:
            img = Image.open(pathAndLabel[0])
            img = img.resize((80,45),Image.NEAREST)
            imgData = np.asarray([np.float32(img)/255.0])
            imageData.append(imgData)
            labelData.append(np.int32(pathAndLabel[1]))

        threshold = np.int32(len(imageData)/8*7)
        train_data = imageData[0:threshold]
        test_data  = imageData[threshold:]
        train_label = labelData[0:threshold]
        test_label  = labelData[threshold:]

    #RGB画像
    else:
        imageData = []
        labelData = []

        for pathAndLabel in allData:
            img = Image.open(pathAndLabel[0])
            img = img.resize((80,45),Image.NEAREST)#リサイズ

            #rgb配列の変更
            r,g,b = img.split()
            rImgData = np.asarray(np.float32(r)/255.0)
            gImgData = np.asarray(np.float32(g)/255.0)
            bImgData = np.asarray(np.float32(b)/255.0)
            imgData = np.asarray([rImgData, gImgData, bImgData])
            imageData.append(imgData)
            labelData.append(np.int32(pathAndLabel[1]))

        #訓練とテストデータの分離
        threshold = len(imageData) - test_num
        train_data = imageData[0:threshold]
        test_data  = imageData[threshold:]
        train_label = labelData[0:threshold]
        test_label  = labelData[threshold:]

    return train_data,test_data,train_label,test_label


#パスから作業をする
def getValueDataFromPath(imagePath):
    img = Image.open(imagePath)
    #img.show()
    r,g,b = img.split()
    rImgData = np.asarray(np.float32(r)/255.0)
    gImgData = np.asarray(np.float32(g)/255.0)
    bImgData = np.asarray(np.float32(b)/255.0)
    imgData = np.asarray([[[rImgData, gImgData, bImgData]]])
    return imgData


#画像データから作業をする
def getValueDataFromImg(img):
    #img.show()
    r,g,b = img.split()
    rImgData = np.asarray(np.float32(r)/255.0)
    gImgData = np.asarray(np.float32(g)/255.0)
    bImgData = np.asarray(np.float32(b)/255.0)
    imgData = np.asarray([[[rImgData, gImgData, bImgData]]])
    return imgData


if __name__=='__main__':
    pathsAndLabels = []

    '''
    #指画像の認識
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_0", 0]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_45", 1]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_90", 2]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_135", 3]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_180", 4]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_225", 5]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_270", 6]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_315", 7]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/paper", 8]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/stone", 9]))
    '''

    #顔画像の認識
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person0", 0]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person1", 1]))
    pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person2", 2]))
    #pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person3", 3]))
    #pathsAndLabels.append(np.asarray(["/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person4", 4]))

    #保存記録の設定
    #train_data,test_data,train_label,test_label = img_cnn_TrainAndTest(pathsAndLabels,3,10)
    train_data,test_data,train_label,test_label = img_cnn_TrainAndTest(pathsAndLabels,1,10)

    print("num of train ... {}".format(len(train_data)))
    print("num of test ... {}".format(len(test_data)))

    '''
    #指画像の保存
    np.save("fingpic_data_train.npy",train_data)
    np.save("fingpic_data_test.npy",test_data)
    np.save("fingpic_label_train.npy",train_label)
    np.save("fingpic_label_test.npy",test_label)
    print("all files were saved.")
    '''

    #画像の保存
    np.save("facepic_data_train.npy",train_data)
    np.save("facepic_data_test.npy",test_data)
    np.save("facepic_label_train.npy",train_label)
    np.save("facepic_label_test.npy",test_label)
    print("all files were saved.")
