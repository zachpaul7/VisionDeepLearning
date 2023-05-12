# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:03:51 2023

@author: zachp
"""

import cv2 as cv
import numpy as np
import time

def my_EqualizeHist(img):
    gray = np.zeros([img.shape[0],img.shape[1]])
    gray = 0.114*img[:,:,0]+0.587*img[:,:,1]+0.299*img[:,:,2]
    
    # 이미지의 픽셀 값 범위를 [0, 255]로 변경합니다.
    min_value = np.min(gray)  # 이미지의 최솟값을 구합니다.
    max_value = np.max(gray)  # 이미지의 최댓값을 구합니다.
    normalized_image = (gray - min_value) / (max_value - min_value) * 255  # 픽셀 값 범위를 [0, 255]로 조정합니다.
    normalized_image = normalized_image.astype(np.uint8)  # 픽셀 값을 8비트 자연수형으로 변환합니다.

    # 히스토그램을 계산합니다.
    hist, bins = np.histogram(normalized_image.flatten(), 256, [0, 256])  # 0~255 범위를 갖는 히스토그램을 계산합니다.
    cdf = hist.cumsum()  # 누적 분포 함수(Cumulative Distribution Function)를 계산합니다.

    # 히스토그램 평활화를 수행합니다.
    cdf_normalized = cdf * float(255) / cdf[-1]  # 누적 분포 함수를 정규화합니다.
    equalized_image = np.interp(normalized_image.flatten(), bins[:-1], cdf_normalized)  # 정규화된 누적 분포 함수를 이용하여 평활화를 수행합니다.
    equalized_image = equalized_image.reshape(normalized_image.shape)  # 결과 이미지의 형태를 입력 이미지와 동일하게 조정합니다.
    
    # 최종 결과를 반환합니다.
    return np.uint8(equalized_image)

def cv_EqualizeHist(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    equal = cv.equalizeHist(gray)
    
    color = cv.cvtColor(equal, cv.COLOR_GRAY2BGR)

    return np.uint8(color)

img = cv.imread('./Dani.jpg')

start = time.time()
my_equalized_img = my_EqualizeHist(img)
print('My time : ',time.time()-start)

start = time.time()
cv_equalized_img = cv_EqualizeHist(img)
print('CV time : ',time.time()-start)   

cv.imshow('Original Image', img)
cv.imshow('My Equalized Image', my_equalized_img)
cv.imshow('CV Equalized Image', cv_equalized_img)

cv.waitKey()
cv.destroyAllWindows()