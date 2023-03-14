# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 00:41:32 2023

@author: zachp
"""

import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    key = cv.waitKey(1)
    
    if key == ord('g'):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Video Display Gray', gray)
        
    elif key == ord('c'):
        cv.imshow('Video Display Color', frame)
    
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()