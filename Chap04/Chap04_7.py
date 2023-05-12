# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:37:14 2023

@author: zachp
"""

import cv2 as cv

img = cv.imread('messi.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)
grad_y = cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)
edge_strength = cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

scharrx = cv.Scharr(img, cv.CV_32F, 1, 0)
scharry = cv.Scharr(img, cv.CV_32F, 0, 1)
scharr_absx = cv.convertScaleAbs(scharrx)
scharr_absy = cv.convertScaleAbs(scharry)
scharr = cv.addWeighted(scharr_absx, 0.5, scharr_absy, 0.5, 0)

cv.imshow('Original',gray)
cv.imshow('sobel_x',sobel_x)
cv.imshow('sobel_y',sobel_y)
cv.imshow('edge_strength',edge_strength)
cv.imshow('scharr_absx',scharr_absx)
cv.imshow('scharr_absy',scharr_absy)
cv.imshow('scharr',scharr)

cv.waitKey()
cv.destroyAllWindows()