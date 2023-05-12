# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:50:30 2023

@author: zachp
"""

import cv2 as cv

img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)

edges1 = cv.Canny(img, 50, 100)
edges2 = cv.Canny(img, 100, 200)
edges3 = cv.Canny(img, 150, 300)

cv.imshow('Original Image', img)
cv.imshow('Edges (threshold1=50, threshold2=100)', edges1)
cv.imshow('Edges (threshold1=100, threshold2=200)', edges2)
cv.imshow('Edges (threshold1=150, threshold2=300)', edges3)

cv.waitKey(0)
cv.destroyAllWindows()