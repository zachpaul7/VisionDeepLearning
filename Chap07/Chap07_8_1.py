# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:31:05 2023

@author: zachp
"""

import numpy as np 
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

(x_train,y_train),(x_test,y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000,784)
x_train = x_train.astype(np.float32)/255.0
x_test = x_test.astype(np.float32)/255.0
y_train = tf.keras.utils.to_categorical(y_train,10)
y_test = tf.keras.utils.to_categorical(y_test,10)

# 학습률을 다양하게 설정하기 위해 리스트로 저장합니다.
learning_rates = [0.1, 0.01, 0.001, 0.0001, 0.00001]

# 각 학습률에 대한 정확률을 저장할 빈 리스트를 만듭니다.
accuracies = []

# 각 학습률에 대해 모델을 생성하고 학습시킵니다.
for lr in learning_rates:
    # 모델을 생성합니다.
    mlp = Sequential()
    mlp.add(Dense(units=512,activation='tanh',input_shape=(784,)))
    mlp.add(Dense(units=10,activation='softmax'))

    # 모델을 컴파일합니다. Adam 옵티마이저의 학습률을 lr로 설정합니다.
    mlp.compile(loss='categorical_crossentropy',optimizer=Adam(learning_rate=lr),metrics=['accuracy'])
    
    # 모델을 학습시킵니다. 세대 수는 100으로 설정합니다.
    mlp.fit(x_train,y_train,batch_size=128,epochs=100,validation_data=(x_test,y_test),verbose=2)

    # 모델의 정확률을 평가하고 accuracies 리스트에 추가합니다.
    res = mlp.evaluate(x_test,y_test,verbose=0)
    accuracies.append(res[1]*100)

import matplotlib.pyplot as plt

# 학습률과 정확률의 관계를 그래프
plt.plot(learning_rates, accuracies)
plt.xlabel('Learning rate')
plt.ylabel('Accuracy')
plt.xscale('log')
plt.show()