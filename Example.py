import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Path to the trained model file
filepath = r'C:\Users\DELL\OneDrive\Desktop\Tomoto Leaf Disease Prediction\model.h5'

# Load the trained model
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

# Path to the image file
image_path = r'C:\Users\DELL\OneDrive\Desktop\Tomoto Leaf Disease Prediction\Dataset\test\image.JPG'

# Print the image path for debugging
print(f"Loading image from: {image_path}")

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: The image file does not exist at the given path: {image_path}")
else:
    # Load the image
    tomato_plant = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if tomato_plant is None:
        print("Error: Unable to load image. The file might be corrupted or not readable by OpenCV.")
    else:
        print("Image loaded successfully")

        # Resize the image to match the model's expected input size
        test_image = cv2.resize(tomato_plant, (128, 128))

        # Convert image to numpy array and normalize pixel values
        test_image = img_to_array(test_image) / 255.0

        # Expand dimensions to make the image batch-like (1, 128, 128, 3)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict the class of the image
        result = model.predict(test_image)

        # Get the class with the highest probability
        pred = np.argmax(result, axis=1)

        # Print the result based on the predicted class
        if pred == 0:
            print("Tomato - Bacteria Spot Disease")
        elif pred == 1:
            print("Tomato - Early Blight Disease")
        elif pred == 2:
            print("Tomato - Healthy and Fresh")
        elif pred == 3:
            print("Tomato - Late Blight Disease")
        elif pred == 4:
            print("Tomato - Leaf Mold Disease")
        elif pred == 5:
            print("Tomato - Septoria Leaf Spot Disease")
        elif pred == 6:
            print("Tomato - Target Spot Disease")
        elif pred == 7:
            print("Tomato - Tomato Yellow Leaf Curl Virus Disease")
        elif pred == 8:
            print("Tomato - Tomato Mosaic Virus Disease")
        elif pred == 9:
            print("Tomato - Two Spotted Spider Mite Disease")
        else:
            print("Unknown Disease")
