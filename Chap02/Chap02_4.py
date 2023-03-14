# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 00:26:48 2023

@author: zachp
"""

import cv2 as cv
import sys

img = cv.imread('./Kimi.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_s1 = cv.resize(gray, dsize=(0,0), fx=0.1, fy=0.1)
gray_s2 = cv.resize(gray, dsize=(0,0), fx=0.2, fy=0.2)
gray_s3 = cv.resize(gray, dsize=(0,0), fx=0.3, fy=0.3)
gray_s4 = cv.resize(gray, dsize=(0,0), fx=0.4, fy=0.4)
gray_s5 = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)
gray_s6 = cv.resize(gray, dsize=(0,0), fx=0.6, fy=0.6)
gray_s7 = cv.resize(gray, dsize=(0,0), fx=0.7, fy=0.7)
gray_s8 = cv.resize(gray, dsize=(0,0), fx=0.8, fy=0.8)
gray_s9 = cv.resize(gray, dsize=(0,0), fx=0.9, fy=0.9)
gray_s10 = cv.resize(gray, dsize=(0,0), fx=1.0, fy=1.0)

cv.imwrite('./gray_s1.jpg', gray_s1)
cv.imwrite('./gray_s2.jpg', gray_s2)
cv.imwrite('./gray_s3.jpg', gray_s3)
cv.imwrite('./gray_s4.jpg', gray_s4)
cv.imwrite('./gray_s5.jpg', gray_s5)
cv.imwrite('./gray_s6.jpg', gray_s6)
cv.imwrite('./gray_s7.jpg', gray_s7)
cv.imwrite('./gray_s8.jpg', gray_s8)
cv.imwrite('./gray_s9.jpg', gray_s9)
cv.imwrite('./gray_s10.jpg', gray_s10)

cv.imshow('Gray Image S1', gray_s1)
cv.imshow('Gray Image S2', gray_s2)
cv.imshow('Gray Image S3', gray_s3)
cv.imshow('Gray Image S4', gray_s4)
cv.imshow('Gray Image S5', gray_s5)
cv.imshow('Gray Image S6', gray_s6)
cv.imshow('Gray Image S7', gray_s7)
cv.imshow('Gray Image S8', gray_s8)
cv.imshow('Gray Image S9', gray_s9)
cv.imshow('Gray Image S10', gray_s10)

cv.waitKey()
cv.destroyAllWindows()    