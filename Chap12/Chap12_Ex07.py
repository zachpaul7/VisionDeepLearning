import os
import trimesh
import tensorflow as tf
import matplotlib.pyplot as plt

classes = ['bathtub', 'bed', 'chair', 'desk', 'dresser', 'monitor', 'night_stand', 'sofa', 'table', 'toilet']

path = 'http://3dvision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip'
data_dir = tf.keras.utils.get_file('modelnet.zip', path, extract=True)
data_dir = os.path.join(os.path.dirname(data_dir), 'ModelNet10')

fig = plt.figure(figsize=(50, 10))
for i in range(len(classes)):
    category_dir = os.path.join(data_dir, classes[i], 'train')
    sample_files = sorted(file for file in os.listdir(category_dir) if file != '.DS_Store')[:7]  # Exclude .DS_Store file

    for j, sample_file in enumerate(sample_files):
        mesh = trimesh.load(os.path.join(category_dir, sample_file))
        points = mesh.sample(1024)

        ax = fig.add_subplot(len(classes), 10, i * 10 + j + 1, projection='3d')  # Adjusting the subplot position
        ax.set_title(classes[i], fontsize=30)
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1, c='g')

plt.show()
