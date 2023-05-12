# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:30:31 2023

@author: zachp
"""

import cv2 as cv

img = cv.imread('./mot1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp,des = sift.detectAndCompute(gray,None)

gray = cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift',gray)

k = cv.waitKey()
cv.destroyAllWindows()
