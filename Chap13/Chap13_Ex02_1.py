import numpy as np
from tensorflow.keras.datasets import mnist
from sklearn.mixture import GaussianMixture

(x_train, y_train), (x_test, y_test) = mnist.load_data()
X = x_train.reshape((x_train.shape[0], 28*28))

k = 8  # set the number k of Gaussians in equation (13.4) to 8

gm = GaussianMixture(n_components=k).fit(X)

gen = gm.sample(n_samples=1)

import matplotlib.pyplot as plt

plt.figure(figsize=(20, 4))  # Figure the average of the trained Gaussians for each class
for c in range(10):
    X_class = X[y_train == c]
    gm_class = GaussianMixture(n_components=k).fit(X_class)
    for i in range(k):
        plt.subplot(10, 10, c*10 + i + 1)
        plt.imshow(gm_class.means_[i].reshape((28, 28)), cmap='gray')
        plt.xticks([])
        plt.yticks([])
plt.show()

plt.figure(figsize=(20, 4))  # Draw 10 generated samples for each class
for c in range(10):
    X_class = X[y_train == c]
    gm_class = GaussianMixture(n_components=k).fit(X_class)
    gen_class = gm_class.sample(n_samples=10)
    for i in range(10):
        plt.subplot(10, 10, c*10 + i + 1)
        plt.imshow(gen_class[0][i].reshape((28, 28)), cmap='gray')
        plt.xticks([])
        plt.yticks([])

plt.show()

