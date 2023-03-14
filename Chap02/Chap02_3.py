# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv
import sys

img1 = cv.imread('C:\img\Kimi.jpg')
img2 = cv.imread('C:\img\Dani.jpg')

if img1 is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
if img2 is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('IMG DP1',img1)
cv.imshow('IMG DP2',img2)

cv.waitKey()
cv.destroyAllWindows()