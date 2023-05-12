# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:40:40 2023

@author: zachp
"""

import cv2 as cv
import numpy as np

img = cv.imread("messi.jpg")
img_show = np.copy(img)

mask = np.zeros((img.shape[0],img.shape[1]), np.uint8)
mask[:,:] = cv.GC_PR_BGD

BrushSize = 3
LColor, RColor = (255,0,0), (0,0,255)

def painting(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show,(x,y),BrushSize,LColor,-1)
        cv.circle(mask,(x,y),BrushSize,cv.GC_FGD,-1)
        
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show,(x,y),BrushSize,RColor,-1)
        cv.circle(mask,(x,y),BrushSize,cv.GC_BGD,-1)
        
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show,(x,y),BrushSize,LColor,-1)
        cv.circle(mask,(x,y),BrushSize,cv.GC_FGD,-1)
        
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show,(x,y),BrushSize,RColor,-1)
        cv.circle(mask,(x,y),BrushSize,cv.GC_BGD,-1)
        
    cv.imshow('Painting',img_show)
    
cv.namedWindow('Painting')
cv.setMouseCallback('Painting',painting)


background = np.zeros((1,65), np.float64)
foreground = np.zeros((1,65), np.float64)

def grabCutting():
    cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
    mask2 = np.where((mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')
    grab = img * mask2[:,:,np.newaxis]
    cv.imshow('Grab cut image', grab)

while True:
    cv.imshow('Painting',img_show)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        grabCutting()
        
cv.waitKey()
cv.destroyAllWindows()
