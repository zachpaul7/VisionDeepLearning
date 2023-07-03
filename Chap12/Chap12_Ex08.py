import os
import trimesh
import tensorflow as tf
import matplotlib.pyplot as plt

classes = ['bathtub', 'bed', 'chair', 'desk', 'dresser', 'monitor', 'night_stand', 'sofa', 'table', 'toilet']

path = 'http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip'
data_dir = tf.keras.utils.get_file('modelnet.zip', path, extract=True)
data_dir = os.path.join(os.path.dirname(data_dir), 'ModelNet10')

fig = plt.figure(figsize=(50, 25))

num_points = [512, 1024, 2048, 4096, 8192]  # List of desired number of points

for j in range(len(num_points)):
    for i in range(len(classes)):
        mesh = trimesh.load(os.path.join(data_dir, classes[i] + '/train/' + classes[i] + '_0001.off'))

        points = mesh.sample(num_points[j])

        ax = fig.add_subplot(len(num_points), len(classes), j * len(classes) + i + 1, projection='3d')
        ax.set_title(classes[i], fontsize=30)
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1, c='g')

plt.show()
