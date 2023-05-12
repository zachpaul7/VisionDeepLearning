# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:57:03 2023

@author: zachp
"""

import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# 데이터셋 로드
(x_train, y_train), (x_test, y_test) = ds.cifar100.load_data()

# 데이터 전처리
x_train = x_train.reshape(50000, 3072)
x_test = x_test.reshape(10000, 3072)
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 100)
y_test = tf.keras.utils.to_categorical(y_test, 100)

# 초경량 모델 탐색
best_acc = 0
best_model = None
for i in range(10):
    units = np.random.randint(128, 1024)
    dropout_rate = np.random.uniform(0.1, 0.5)
    dmlp = Sequential()
    dmlp.add(Dense(units=units, activation='relu', input_shape=(3072,)))
    dmlp.add(Dropout(dropout_rate))
    dmlp.add(Dense(units=units, activation='relu'))
    dmlp.add(Dropout(dropout_rate))
    dmlp.add(Dense(units=100, activation='softmax'))
    dmlp.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001), metrics=['accuracy'])
    hist = dmlp.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=0)
    acc = dmlp.evaluate(x_test, y_test, verbose=0)[1] * 100
    if acc > best_acc:
        best_acc = acc
        best_model = dmlp
    print(f"Units: {units}, Dropout rate: {dropout_rate:.2f}, Accuracy: {acc:.2f}%")

# 최적의 모델 저장
best_model.save('dmlp_trained_cifar100.h5')

# 정확도와 손실 그래프 출력
import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy Graph')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'])
plt.grid()
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss Graph')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['Train', 'Test'])
plt.grid()
plt.show()

print(f"Best Accuracy: {best_acc:.2f}%")
