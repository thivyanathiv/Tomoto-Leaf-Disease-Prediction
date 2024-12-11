from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Load model
filepath = r'C:\Users\DELL\OneDrive\Desktop\Tomoto Leaf Disease Prediction\model.h5'
model = load_model(filepath)
print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
    try:
        # Load and preprocess image
        test_image = load_img(tomato_plant, target_size=(128, 128))  # load image
        print("@@ Got Image for prediction")

        test_image = img_to_array(test_image) / 255  # convert image to np array and normalize
        test_image = np.expand_dims(test_image, axis=0)  # change dimension 3D to 4D

        # Predict using the model
        result = model.predict(test_image)  # predict diseased plant or not
        print('@@ Raw result = ', result)

        pred = np.argmax(result, axis=1)
        print(pred)
        
        # Disease classification and page redirection
        if pred == 0:
            return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
        elif pred == 1:
            return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'
        elif pred == 2:
            return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'
        elif pred == 3:
            return "Tomato - Late Blight Disease", 'Tomato - Late_blight.html'
        elif pred == 4:
            return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
        elif pred == 5:
            return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
        elif pred == 6:
            return "Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'
        elif pred == 7:
            return "Tomato - Tomato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
        elif pred == 8:
            return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
        elif pred == 9:
            return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error in prediction", 'error.html'


# Create flask instance
app = Flask(__name__)

# Render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# Get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Fetch input file
            file = request.files['image']
            filename = file.filename
            print("@@ Input posted = ", filename)

            # Ensure the 'upload' folder exists
            upload_folder = r'C:\Users\DELL\OneDrive\Desktop\Tomoto Leaf Disease Prediction/static/upload/'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            print("@@ Predicting class......")
            pred, output_page = pred_tomato_dieas(tomato_plant=file_path)

            return render_template(output_page, pred_output=pred, user_image=file_path)
        except Exception as e:
            print(f"Error during file upload or prediction: {e}")
            return render_template('error.html')

# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=True, port=8080)
