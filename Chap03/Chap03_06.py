# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:51:33 2023

@author: zachp
"""

import numpy as np
import matplotlib.pyplot as plt

# 1차원 가우시안 필터 그래프

# x 범위 설정
x1 = np.arange(-6, 6, 0.01)

# 가우시안 함수
def gaussian1(x1, sigma):
    return (1/np.sqrt(2 * np.pi * sigma**2)) * np.exp(-(x1)**2 / (2 * sigma**2))

plt.plot(x1,gaussian1(x1,1))
plt.show()


# 2차원 가우시안 필터 그래프

# x,y 범위 설정
x = np.arange(-6, 6, 0.01)
y = np.arange(-6, 6, 0.01)

def gaussian2(x, y, sigma):
    return (1 / (2 * np.pi * sigma**2)) * np.exp(-((x)**2 + (y)**2) / (2 * sigma**2))

X, Y = np.meshgrid(x, y)

sigma = 1

Z = gaussian2(X, Y, sigma)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 2차원 가우시안 함수를 3차원에 그림
ax.plot_surface(X, Y, Z)
plt.show()








