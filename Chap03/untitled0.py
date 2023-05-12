# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:08:21 2023

@author: zachp
"""

import numpy as np
import matplotlib.pyplot as plt

# Read image
img = np.array([[0, 0, 1, 1, 3],
                [2, 3, 3, 3, 3],
                [3, 3, 4, 4, 4],
                [4, 3, 4, 5, 7],
                [4, 4, 4, 5, 7]])

hist, bins = np.histogram(img.flatten(), 8, [0, 8])

h_norm = hist / (img.shape[0] * img.shape[1])

cdf = np.cumsum(h_norm)

T = cdf * 7

print("명암 값:", np.unique(img))
print("히스토그램:", hist)
print("정규화된 히스토그램:", h_norm)
print("누적 분포 함수:", cdf)
print(T)




