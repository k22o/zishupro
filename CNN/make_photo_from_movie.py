# -*- coding: UTF-8 -*-

'''
http://testpy.hatenablog.com/entry/2017/07/13/003000 より 一部変更
動画をフレームに分割して画像として指定したディレクトリに保存する操作 動画を読み込んで、フレームごとに存在を確認して、確認できれば画像として保存する
'''

import os
import cv2
import numpy as np
#Qimport hadairo

def video_2_frames(video_file, image_dir, image_file='img2_%s.png'):

    #ディレクトリがない場合は作る
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    i = 0
    cap = cv2.VideoCapture(video_file)

    while(cap.isOpened()):
        ret, frame = cap.read()#フレームごとの取得

        ##frame の処理をここでする###

        #saved_data = hadairo.hadairo_cap(frame)#肌色抽出
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#グレースケール化

        ######################

        if ret == False:
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(6), gray) # Save a frame
        print('Save', image_dir+image_file % str(i).zfill(6))
        i += 1

    cap.release()


if __name__ == '__main__':

    #全ての場合を順番に実行できないエラーあり。1つずつ実行。

    print("start to make pictures")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_0.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_0/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_45.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_45/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_90.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_90/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_135.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_135/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_180.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_180/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_225.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_225/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_270.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_270/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/deg_315.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/deg_315/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/paper.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/paper/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/stone.webm", "/home/mech-user/work/kikaib_enshu/zishupro/fingpictures/stone/")


    video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/face_movie/omura.mp4", "/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person0/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/face_movie/mori.webm", "/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person1/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/face_movie/yamada.mp4", "/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person2/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/stone.webm", "/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person3/")
    #video_2_frames("/home/mech-user/work/kikaib_enshu/zishupro/fing_movie/stone.webm", "/home/mech-user/work/kikaib_enshu/zishupro/facepictures/person4/")

    print("finish")
