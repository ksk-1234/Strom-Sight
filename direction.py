import os
import zipfile
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

# Download the dataset using Kaggle API

file_path = 'insat3d-infrared-raw-cyclone-images-20132021.zip'
output_folder = '/extracted_folder'  # Change this to your desired extraction path

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Unzipping the file
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(output_folder)

# Path to the extracted dataset
data_folder = output_folder

# Preprocessing function for images
def preprocess_images(image_paths, labels, desired_width, desired_height):
    images = []
    for path in image_paths:
        img = Image.open(path)
        img = img.resize((desired_width, desired_height))  # Resize images to a consistent size
        img = np.array(img)  # Convert PIL image to NumPy array
        images.append(img)
    return np.array(images), np.array(labels)

# Load and preprocess images
image_paths = []
labels = []

for direction in os.listdir(data_folder):
    direction_path = os.path.join(data_folder, direction)
    if os.path.isdir(direction_path):
        for image_file in os.listdir(direction_path):
            if image_file.endswith('.jpg'):  # Assuming images are in JPG format
                image_paths.append(os.path.join(direction_path, image_file))
                labels.append(direction)  # Store label based on folder name

# Split the data into training and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(image_paths, labels, test_size=0.2, random_state=42)

# Define desired width and height for the images
desired_width = 100
desired_height = 100

# Preprocess training and testing images
train_images_processed, train_labels_processed = preprocess_images(train_images, train_labels, desired_width, desired_height)
test_images_processed, test_labels_processed = preprocess_images(test_images, test_labels, desired_width, desired_height)

# Now you have preprocessed training and testing images and labels ready for model training
# Proceed with building and training your model using train_images_processed, train_labels_processed, etc.
