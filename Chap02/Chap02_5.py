# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:58:28 2023

@author: zachp
"""

import cv2 as cv
import sys

frames=[]

cap = cv.VideoCapture(0, cv.CAP_DSHOW) # 카메라와 연결 시도
gray = False
if not cap.isOpened():
    sys.exit('카메라 연결 실패.')

while True:
   ret, frame = cap.read() # 비디오를 구성하는 프레임 흭득
   if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
   if gray :
       frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   cv.imshow('Video display',frame)
   key=cv.waitKey(1) # 1밀리초 동안 키보드 입력 기다림
   if key==ord('q'): # 'q' 키 입력시 루프를 빠져나감
      break
   elif key == ord('g'): # 'g' 키 입력시 명암
       gray = True
   elif key == ord('c'): # 'c' 키 입력시 컬러
       gray = False

cap.release() #카메라 연결 끊음
cv.destroyAllWindows()