# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:21:21 2023

@author: zachp
"""

import cv2 as cv
import sys
from math import sqrt, pow

img = cv.imread('./Kimi.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
def draw(event, x, y, flags, param):
    global ix, iy, jx, jy
    
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix,iy), (x, y), (0, 0, 255), 2)
        
    elif event == cv.EVENT_RBUTTONDOWN:
        jx, jy = x, y
        
    elif event == cv.EVENT_RBUTTONUP:
        radius = int(sqrt(pow(x-jx,2)+pow(y-jy,2)))
        cv.circle(img, (jx,jy),radius,(0,0,255))
        
        
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break