# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:46:12 2023

@author: zachp
"""

import cv2

img = cv2.imread('./messi.jpg')

gaussians = []
for i in range(6):
    ksize = (5 + i*4, 5 + i*4)  # 들여쓰기 변경
    sigma = 1 + i*0.5
    gaussians.append(cv2.GaussianBlur(img, ksize, sigma))


dogs = []
for i in range(5):
    dogs.append(gaussians[i+1] - gaussians[i])

for i in range(6):
    cv2.namedWindow(f'Gaussian {i+1}', cv2.WINDOW_NORMAL)
    cv2.imshow(f'Gaussian {i+1}', gaussians[i])

for i in range(5):
    cv2.namedWindow(f'DOG {i+1}', cv2.WINDOW_NORMAL)
    cv2.imshow(f'DOG {i+1}', dogs[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
