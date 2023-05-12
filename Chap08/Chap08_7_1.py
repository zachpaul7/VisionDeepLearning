import numpy as np 
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout,Input
from tensorflow.keras.optimizers import Adam

(x_train,y_train),(x_test,y_test) = ds.cifar10.load_data()
x_train = x_train.astype(np.float32)/255.0
x_test = x_test.astype(np.float32)/255.0
y_train = tf.keras.utils.to_categorical(y_train,10)
y_test = tf.keras.utils.to_categorical(y_test,10)

input_layer = Input(shape=(32, 32, 3))
conv_layer1 = Conv2D(32, (3,3), activation='relu')(input_layer)
conv_layer2 = Conv2D(32, (3,3), activation='relu')(conv_layer1)
pooling_layer1 = MaxPooling2D(pool_size=(2,2))(conv_layer2)
dropout_layer1 = Dropout(0.25)(pooling_layer1)
conv_layer3 = Conv2D(64, (3,3), activation='relu')(dropout_layer1)
conv_layer4 = Conv2D(64, (3,3), activation='relu')(conv_layer3)
pooling_layer2 = MaxPooling2D(pool_size=(2,2))(conv_layer4)
dropout_layer2 = Dropout(0.25)(pooling_layer2)
flatten_layer = Flatten()(dropout_layer2)
dense_layer1 = Dense(units=512, activation='relu')(flatten_layer)
dropout_layer3 = Dropout(0.5)(dense_layer1)
output_layer = Dense(units=10, activation='softmax')(dropout_layer3)

cnn = Model(inputs=input_layer, outputs=output_layer)

cnn.compile(loss='categorical_crossentropy',optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
hist=cnn.fit(x_train,y_train,batch_size=128,epochs=30,validation_data=(x_test,y_test),verbose=2)

res=cnn.evaluate(x_test,y_test,verbose=0)
print('정확률 = ',res[1]*100)

import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy graph')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train','Validation'])
plt.grid()
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss graph')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train','Validation'])
plt.grid()
plt.show()