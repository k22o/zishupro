#-*- coding: utf-8 -*-
#python2!!

import numpy as np
import bluetooth
import cv2
import socket,time,math
import hadairo as hd

####bluetooth通信の設定
#addr = "B8:27:EB:95:A6:C0"#アドレス
#port1 = 1 #ポート
#sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケット作成
#sock1.connect((addr, port))#ソケットをつなげる

thre5 = 200#y
thre6 = 360#y
thre7 = 250#x
thre8 = 410#x

####解析結果に応じた値の分類
def input_search(x,y,area):

    #処理内容
    if x > thre8 and y < thre6 and y>thre5:
        msg = "deg_0"
    elif x > thre8 and y < thre5:
        msg = "deg_45"
    elif x < thre8 and x > thre7 and y < thre5:
        msg = "deg_90"
    elif x < thre7 and y < thre5:
        msg = "deg_135"
    elif x < thre7 and y > thre5 and y < thre6:
        msg = "deg_180"
    elif x < thre7 and y > thre6:
        msg = "deg_225"
    elif x < thre8 and x > thre7 and y > thre6:
        msg = "deg_270"
    elif x > thre8 and y  > thre6:
        msg = "deg_315"
    else :
        msg = "stop"

    return msg


####肌色重心のはじめの位置決定
def init_center(frame):
    hadairo = hd.hadairo_cap(frame)#肌色検出
    mu = cv2.moments(hadairo, False)#重心検出
    area = cv2.countNonZero(hadairo)#肌色面積

    #座標の取得
    x= int(mu["m10"]/mu["m00"])
    y = int(mu["m01"]/mu["m00"])

    #重心を表す円の表示
    cv2.circle(hadairo, (x,y), 4, 100, 2, 4)#濃淡イメージに表示
    #cv2.circle(frame, (x,y), 4, 100, 2, 4)#カラーイメージに表示
    print ("init_x:{},init_y:{}".format(x,y))
    return x,y,area,hadairo


####肌色重心の算出
def center(frame):

    hadairo = hd.hadairo_cap(frame)#肌色検出
    mu = cv2.moments(hadairo, False)

    #座標の取得
    x= int(mu["m10"]/mu["m00"])
    y = int(mu["m01"]/mu["m00"])
    area = cv2.countNonZero(hadairo)



    #重心を表す円の表示
    cv2.circle(hadairo, (x,y), 5, 100, -1, 4)#濃淡イメージに表示
    #cv2.circle(frame, (x,y), 4, 100, 2, 4)#カラーイメージに表示
    print("x:{} y:{} area:{}".format(x,y,area))
    return x,y,area,hadairo


if __name__=='__main__':


    #startが入力されたら、開始する
    stop_cnt = 1
    msg0 = raw_input()


    if msg0 == "start":
        #msg0_bin = msg0.encode('utf-8')#binに変換
        #sock1.send(msg0_bin)
        print("send msg...{}".format(msg0))


    cap = cv2.VideoCapture(0)#capture開始

    #初期状態の設定
    ret,frame = cap.read()

    x ,y,area,hadairo = init_center(frame)

    time.sleep(1)

    while(1):

        ret,frame = cap.read()#フレームをキャプチャ
        if ret == False:
            break

        #反転/ 肌色処理 /重心算出
        frame = cv2.flip(frame, 1)
        x,y,area,hadairo = center(frame)
        hadairo = cv2.line(hadairo, (0,  thre5), (640,  thre5), (255, 0, 0), 5, 4)
        hadairo = cv2.line(hadairo, (0,  thre6), (640,  thre6), (255, 0, 0), 5, 4)
        hadairo = cv2.line(hadairo, (thre7,  0), (thre7,  640), (255, 0, 0), 5, 4)
        hadairo = cv2.line(hadairo, (thre8,  0), (thre8,  640), (255, 0, 0), 5, 4)


        cv2.imshow("frame",frame)
        cv2.imshow("hadairo",hadairo)



        #データ送信部分

        if stop_cnt==0:
            msg = input_search(x,y,area)
        elif stop_cnt==1:
            msg = "stop"
        #msg_bin = msg.encode('utf-8')#binに変換
        #sock1.send(msg_bin)

        print("send msg...{}".format(msg))


        time.sleep(0.1)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k== ord('s'):
            stop_cnt = 1
        elif k== ord('r'):
            stop_cnt = 0


    #sock1.close()
    cap.release()
    cv2.destroyAllWindows()
