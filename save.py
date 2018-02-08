
import os

import cv2

global b

def a(s=[0]):
    s[0] += 1
    return s[0]

for i in range(1,4):
        jpg = cv2.imread('./data0/%d.jpg' %i)
        cv2.namedWindow('jpg', cv2.WINDOW_NORMAL)
        cv2.imshow('jpg', jpg)
        cv2.imwrite('./data/img_%d.png' %i ,jpg)
        print i