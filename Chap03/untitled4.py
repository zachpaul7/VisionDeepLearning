# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:20:48 2023

@author: zachp
"""

import cv2 as cv

def draw_rectangle(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 3)
        patch = img[iy:y, ix:x, :]
        patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)
        cv.imshow('Resize nearest', patch1)
        cv.imshow('Resize bilinear', patch2)
        cv.imshow('Resize bicubic', patch3)

img = cv.imread('./Dani.jpg')
cv.namedWindow('image')
cv.setMouseCallback('image', draw_rectangle)

while True:
    cv.imshow('image', img)
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break

cv.destroyAllWindows()