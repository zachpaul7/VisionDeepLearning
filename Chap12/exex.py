import cv2
import numpy as np
import tensorflow as tf

# Load the depth estimation model
try:
    depth_model = tf.keras.models.load_model('depth_estimation_model.h5')  # Replace with your model path
except OSError:
    print("Unable to load the depth estimation model. Please check the file path.")

# Preprocessing function for depth estimation
def preprocess_image(image):
    # Resize the image to the required input shape
    image = cv2.resize(image, (224, 224))
    # Normalize the image
    image = image / 255.0
    # Add an extra dimension to match the model's input shape
    image = np.expand_dims(image, axis=0)
    return image

# Preprocessing function for displaying the depth map
def preprocess_depth_map(depth_map):
    # Normalize the depth map values
    depth_map = (depth_map - np.min(depth_map)) / (np.max(depth_map) - np.min(depth_map))
    # Convert the depth map to a color image for visualization
    depth_map = cv2.applyColorMap((depth_map * 255).astype(np.uint8), cv2.COLORMAP_JET)
    return depth_map

# Load and preprocess the input image
image_path = 'messi.jpg'  # Replace with your image path
image = cv2.imread(image_path)
if image is None:
    print("Unable to load the input image. Please check the file path.")
preprocessed_image = preprocess_image(image)

# Estimate the depth of the image
depth_map = depth_model.predict(preprocessed_image)[0, :, :, 0]

# Preprocess the depth map for visualization
preprocessed_depth_map = preprocess_depth_map(depth_map)

# Display the preprocessed depth map
cv2.imshow('Preprocessed Depth Map', preprocessed_depth_map)
cv2.waitKey(0)
cv2.destroyAllWindows()


