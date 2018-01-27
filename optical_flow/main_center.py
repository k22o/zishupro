#-*- coding: utf-8 -*-
#python2!!

import numpy as np
import bluetooth
import cv2
import socket,time,math
import hadairo as hd

####bluetooth通信の設定
addr = "B8:27:EB:95:A6:C0"#アドレス
addr_pc = "127.0.1.1"
port1 = 1  #ポート pc→pi
#sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)#ソケット作成

####解析結果に応じた値の分類
def input_search(dif_x,dif_y,dif_area,msg_pre,msg_pre2,msg_pre3):

    #絶対値設定
    abs_x = math.fabs(dif_x)
    abs_y = math.fabs(dif_y)

    #閾値設定
    thre = 20
    thre2 = 20
    thre3 = 100
    thre4 = 5000

    #処理内容
    if dif_x > thre and abs_y < thre:
        msg = "deg_0"
    elif dif_x > thre2 and dif_y < -1*thre2:
        msg = "deg_45"
    elif abs_x < thre and dif_y < -1*thre:
        msg = "deg_90"
    elif dif_x < -1*thre2 and dif_y < -1*thre2:
        msg = "deg_135"
    elif dif_x < -1*thre and abs_y < thre:
        msg = "deg_180"
    elif dif_x < -1*thre2 and dif_y > thre2:
        msg = "deg_225"
    elif abs_x < thre and dif_y > thre:
        msg = "deg_270"
    elif dif_x > thre2 and dif_y  > thre2:
        msg = "deg_315"
    elif msg_pre != msg_pre2 and msg_pre2 != msg_pre3:
        msg = "stop"
    else:
        msg = msg_pre

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
    print ("init_x:{},init_y:{}".format(x,y))
    return x,y,area,hadairo


####肌色重心の算出
def center(frame,prev_x,prev_y,prev_area):

    hadairo = hd.hadairo_cap(frame)#肌色検出
    mu = cv2.moments(hadairo, False)

    #座標の取得
    x= int(mu["m10"]/mu["m00"])
    y = int(mu["m01"]/mu["m00"])
    area = cv2.countNonZero(hadairo)


    #前との誤差の取得
    dif_x = x - prev_x
    dif_y = y - prev_y
    dif_area = area - prev_area

    #重心を表す円の表示
    cv2.circle(hadairo, (x,y), 4, 100, 2, 4)#濃淡イメージに表示
    print("dif_x:{} dif_y:{} dif_area:{}".format(dif_x,dif_y,dif_area))
    return prev_x,prev_y,prev_area,x,y,area,dif_x,dif_y,dif_area,hadairo


if __name__=='__main__':

    #startが入力されたら、開始する
    stop_cnt = 0
    msg0 = raw_input()

    if msg0 == "start":

        #sock1.connect((addr, port1))#ソケットをつなげる
        print("success connection!")

        #pc→piの接続をする
        msg0_bin = msg0.encode('utf-8')#binに変換
        #sock1.send(msg0_bin)
        print("send msg...{}".format(msg0))


    cap = cv2.VideoCapture(0)#capture開始

    #初期状態の設定
    ret,frame = cap.read()
    prev_x ,prev_y,prev_area,hadairo = init_center(frame)
    msg_pre = "deg_90"
    msg_pre2 = "deg_180"
    msg_pre3 = "deg_270"

    time.sleep(1)

    while(1):

        ret,frame = cap.read()#フレームをキャプチャ
        if ret == False:
            break

        #反転/ 肌色処理 /重心算出
        frame = cv2.flip(frame, 1)
        prev_x,prev_y,prev_area,x,y,area,dif_x,dif_y,dif_area,hadairo = center(frame,prev_x,prev_y,prev_area)

        #cv2.imshow("frame",frame)
        cv2.imshow("hadairo",hadairo)

        #値の更新
        prev_x = x
        prev_y = y
        prev_area = area

        #messageの作成
        if stop_cnt==0:
            msg = input_search(dif_x,dif_y,dif_area,msg_pre,msg_pre2,msg_pre3)

        elif stop_cnt==1:
            msg = "stop"

        print("send msg...{}".format(msg))

        #データ送信部分
        msg_bin = msg.encode('utf-8')#binに変換
        #sock1.send(msg_bin)

        msg_pre3 = msg_pre2
        msg_pre2 = msg_pre
        msg_pre = msg


        time.sleep(0.2)

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
