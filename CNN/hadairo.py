# -*- coding: UTF-8 -*-

import cv2
import numpy as np

#肌色を検出して、maskを返す関数
def hadairo_cap(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowcolor = np.array([0,58,58])
    upcolor = np.array([25,173,229])
    #肌色検出

    mask = cv2.inRange(hsv, lowcolor, upcolor)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    return mask


if __name__ == '__main__':

    capture = cv2.VideoCapture(0)

    while(True):
        # 動画ストリームからフレームを取得
        ret, frame = capture.read()
        if ret == False:
            break

        mask = hadairo_cap(frame)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
