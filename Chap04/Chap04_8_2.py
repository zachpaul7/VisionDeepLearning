# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:46:35 2023

@author: zachp
"""
import cv2 as cv

img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)

edges1 = cv.Canny(img, 50, 100, apertureSize=3)
edges2 = cv.Canny(img, 50, 100, apertureSize=5)
edges3 = cv.Canny(img, 50, 100, apertureSize=7)

cv.imshow('Original Image', img)
cv.imshow('Edges (apertureSize=3)', edges1)
cv.imshow('Edges (apertureSize=5)', edges2)
cv.imshow('Edges (apertureSize=7)', edges3)

cv.waitKey(0)
cv.destroyAllWindows()