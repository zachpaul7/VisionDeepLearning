# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 00:56:17 2023

@author: zachp
"""

import cv2 as cv
import sys

img = cv.imread('./Dani.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img, (330,260), (500,530), (0,0,255), 2)
cv.putText(img, 'laugh', (300,200), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
cv.arrowedLine(img,(320,205),(335,255),(255,255,255),2)


cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()    