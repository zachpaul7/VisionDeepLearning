# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:17:48 2023

@author: zachp
"""

import numpy as np 
import tensorflow as tf
import tensorflow.keras.datasets as ds
import matplotlib.pyplot as plt
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

learning = [0.1,0.01,0.001,0.0001,0.00001]
result = []
hists = []

for lr in range(5):
    mlp = Sequential()
    mlp.add(Dense(units=512,activation='tanh',input_shape=(784,)))
    mlp.add(Dense(units=10,activation='softmax'))

    mlp.compile(loss='MSE',optimizer=Adam(learning_rate=learning[lr]),metrics=['accuracy'])
    hists.append(mlp.fit(x_train,y_train,batch_size=128,epochs=100,validation_data=(x_test,y_test),verbose=2))
    res = mlp.evaluate(x_test,y_test,verbose=0)
    result.append(res[1]*100)
    

for i in range(5):
    print(learning[i],'의 정확률 = ',result[i])

plt.plot(hists[0].history['accuracy'],'r')
plt.plot(hists[1].history['accuracy'],'g')
plt.plot(hists[2].history['accuracy'],'b')
plt.plot(hists[3].history['accuracy'],'r--')
plt.plot(hists[4].history['accuracy'],'g--')
plt.title('graph')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(['0.1','0.01','0.001','0.0001','0.00001'])
plt.grid()
plt.show()
