# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:07:48 2023

@author: zachp
"""

import cv2 as cv
import numpy as np

img = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]], dtype=np.float32)

k=0.04
a1 = 4
a2 = 5

def gaussian2d(x, y, sigma):
    return np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2)) / (2 * np.pi * sigma ** 2)

def get_gaussian_kernel(sigma,size):
    if size % 2 == 0:
        size += 1
    aran = np.arange(-1 * (size // 2), size // 2 + 1)
    XX, YY = np.meshgrid(aran, aran)
    ker = gaussian2d(XX, YY, sigma)
    ker = ker/np.sum(ker) # normalization
    return ker

mask = get_gaussian_kernel(1, 3)
dy = np.pad(img[1:],((0,1),(0,0))) - np.pad(img[:-1],((1,0),(0,0)))
dx = np.pad(img[...,1:],((0,0),(0,1))) - np.pad(img[...,:-1],((0,0),(1,0)))

A_01 = np.expand_dims(cv.filter2D(dx * dy, -1, mask), -1)
A_00 = np.expand_dims(cv.filter2D(dy * dy, -1, mask), -1)
A_11 = np.expand_dims(cv.filter2D(dx * dx, -1, mask), -1)
A = np.concatenate([np.concatenate([A_00, A_01], -1),
       np.concatenate([A_01, A_11], -1)], 2)

A_reshape = A.reshape(A.shape[0], A.shape[1], 2, 2)

print("행렬 : ", A_reshape[a1, a2])

# 고유값 계산
eigenvalues = np.linalg.eigvals(A_reshape[a1, a2])

print("고유값: ", eigenvalues)

# 특징 가능성 값 계산
print(eigenvalues[0] * eigenvalues[1])
print(eigenvalues[0] + eigenvalues[1])
C = (eigenvalues[0] * eigenvalues[1]) - (k * (eigenvalues[0] + eigenvalues[1])**2)

print("특징 가능성 값: ", C)



