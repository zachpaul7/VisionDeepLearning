import os
import glob
import trimesh
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score

classes = ['bathtub', 'bed', 'chair', 'desk', 'dresser', 'monitor', 'night_stand', 'sofa', 'table', 'toilet']

path = "http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip"
data_dir = tf.keras.utils.get_file('modelnet.zip', path, extract=True)
data_dir = os.path.join(os.path.dirname(data_dir), 'ModelNet10')

def parse_dataset(num_points=2048):
    train_points, train_labels = [], []
    test_points, test_labels = [], []

    for i in range(len(classes)):
        folder = os.path.join(data_dir, classes[i])
        print('데이터 읽기: 부류 {}'.format(os.path.basename(folder)))
        train_files = glob.glob(os.path.join(folder, 'train/*'))
        test_files = glob.glob(os.path.join(folder, 'test/*'))

        for f in train_files:
            train_points.append(trimesh.load(f).sample(num_points))
            train_labels.append(i)
        for f in test_files:
            test_points.append(trimesh.load(f).sample(num_points))
            test_labels.append(i)
    return (np.array(train_points), np.array(test_points), np.array(train_labels), np.array(test_labels))

NUM_POINTS = 2048  # Number of points in the sampled shape
NUM_CLASSES = 10  # Number of classes
batch_size = 32

x_train, x_test, y_train, y_test = parse_dataset(NUM_POINTS)

def conv_bn(x, filters):  # Convolutional layer followed by batch normalization
    x = layers.Conv1D(filters, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization(momentum=0.0)(x)
    return layers.Activation('relu')(x)

def dense_bn(x, filters):  # Fully connected layer followed by batch normalization
    x = layers.Dense(filters)(x)
    x = layers.BatchNormalization(momentum=0.0)(x)
    return layers.Activation('relu')(x)

class OrthogonalRegularizer(keras.regularizers.Regularizer):
    def __init__(self, num_features, l2reg=0.001):
        self.num_features = num_features
        self.l2reg = l2reg
        self.eye = tf.eye(num_features)

    def __call__(self, x):
        x = tf.reshape(x, (-1, self.num_features, self.num_features))
        xxt = tf.tensordot(x, x, axes=(2, 2))
        xxt = tf.reshape(xxt, (-1, self.num_features, self.num_features))
        return tf.reduce_sum(self.l2reg * tf.square(xxt - self.eye))

def tnet(inputs, num_features):  # T-Net
    bias = keras.initializers.Constant(np.eye(num_features).flatten())
    reg = OrthogonalRegularizer(num_features)

    x = conv_bn(inputs, 32)
    x = conv_bn(x, 64)
    x = conv_bn(x, 512)
    x = layers.GlobalMaxPooling1D()(x)
    x = dense_bn(x, 256)
    x = dense_bn(x, 128)
    x=layers.Dense(num_features*num_features,kernel_initializer='zeros',bias_initializer=bias,activity_regularizer=reg)(x)

    feat_T = layers.Reshape((num_features, num_features))(x)
    return layers.Dot(axes=(2, 1))([inputs, feat_T])  # Apply affine transformation (3x3 matrix) to feature map

inputs = keras.Input(shape=(NUM_POINTS, 3)) # Input to PointNet
x = tnet(inputs, 3) # Build PointNet (feature map reduced by half as mentioned in the paper)
x = conv_bn(x, 32)
x = conv_bn(x, 32)
x = tnet(x, 32)
x = conv_bn(x, 32)
x = conv_bn(x, 64)
x = conv_bn(x, 512)
x = layers.GlobalMaxPooling1D()(x)
x = dense_bn(x, 256)
x = layers.Dropout(0.3)(x)
x = dense_bn(x, 128)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(NUM_CLASSES, activation='softmax')(x) # PointNet output

model = keras.Model(inputs=inputs, outputs=outputs, name='pointnet')

model.compile(loss='sparse_categorical_crossentropy',
optimizer=keras.optimizers.Adam(learning_rate=0.001),
metrics=["sparse_categorical_accuracy"])
model.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test))

y_pred = model.predict(x_test)
y_pred = np.argmax(y_pred, axis=-1)

confusion_mtx = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("변환행렬 : ", confusion_mtx)
print("정확도 : ", accuracy)

chosen = np.random.randint(0, len(x_test), 8)
points = x_test[chosen] # Select 8 samples for prediction
labels = y_test[chosen]

preds = model.predict(points)
preds = np.argmax(preds, axis=-1) # Convert predictions to class indices

fig = plt.figure(figsize=(15, 4)) # Visualize the prediction results

for i in range(8):
    ax = fig.add_subplot(2, 4, i+1, projection='3d')
    ax.scatter(points[i, :, 0], points[i, :, 1], points[i, :, 2], s=1, c='g')
    ax.set_title('Pred: {:}, GT: {:}'.format(classes[preds[i]], classes[labels[i]]), fontsize=16)
    ax.set_axis_off()

plt.show()