# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:57:26 2023

@author: zachp
"""

import cv2 as cv

img = cv.imread('./mot1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()

# 2, 4, 8, 16, ..., 512개 생성 반복문
for num_kp in [2**n for n in range(10)]:
    kp, des = sift.detectAndCompute(gray, None)
    kp = kp[:num_kp]
    des = des[:num_kp]

    result = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.imshow(f'SIFT with {num_kp} keypoints', result)
    cv.waitKey(0)

cv.destroyAllWindows()

