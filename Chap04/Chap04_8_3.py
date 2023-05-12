# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:51:45 2023

@author: zachp
"""

import cv2 as cv

img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)

edges1 = cv.Canny(img, 50, 100, L2gradient=False)
edges2 = cv.Canny(img, 50, 100, L2gradient=True)

cv.imshow('Original Image', img)
cv.imshow('Edges (L2gradient=False)', edges1)
cv.imshow('Edges (L2gradient=True)', edges2)

cv.waitKey(0)
cv.destroyAllWindows()