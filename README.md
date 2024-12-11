# Tomoto-Leaf-Disease-Prediction
This project is a machine learning-based application that predicts diseases on tomato leaves based on the uploaded image. 
The prediction is done using a pre-trained model, which is deployed using Python and Flask for the backend. 
The frontend is designed using HTML and CSS, which allows users to upload an image of a tomato leaf for prediction.

### Key Features:
- **Image Upload**: Users can upload a tomato leaf image.
- **Prediction**: The application will predict if the leaf is healthy or affected by a particular disease.
- **Treatment Suggestions**: Based on the prediction, the application provides treatment suggestions for the disease.

## Technology Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning Model**: Pre-trained deep learning model for image classification.

## Prerequisites
Before running the application, ensure that you have the following installed:

1. **Python 3.12**
2. **Flask**: A micro web framework for Python.
3. **TensorFlow/Keras or PyTorch**: For loading and running the machine learning model.
4. **Other Python Libraries**:
   - `numpy`
   - `opencv-python`
   - `Pillow`
   - `flask`
   - `tensorflow` 

You can install these dependencies using `pip`. Here's the list of necessary packages:
pip install flask tensorflow numpy opencv-python Pillow


## Setup Instructions
## 1. Train or Download the Model

- **Option 1: If you have a pre-trained model**, place the model file (e.g., `model.h5`) in the project directory.
- **Option 2: If you want to train your own model**, you can train it using a dataset of tomato leaf images and save it in a format like `.h5`.

Ensure that the model is capable of classifying images of tomato leaves into healthy or diseased categories.

### 3. Running the Flask App

In the project directory, open a terminal and run the following command to start the Flask server:

```bash
python leaf.py
```

The server will start, and you should see the following output:

```bash
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

### 4. Accessing the Frontend

Once the Flask server is running, open your browser and navigate to `http://127.0.0.1:8080/`. You should see the web interface,
where you can upload an image of a tomato leaf for prediction.

---

## Frontend Details
The frontend of this project is designed using **HTML and CSS**. The interface allows users to upload an image file of a tomato leaf.
Upon submission, the image is sent to the backend for processing and prediction. The result is displayed along with treatment suggestions for the predicted disease.

## Running the Application

1. Start the Flask server by running the following command:

    ```bash
    python leaf.py
    ```

2. Open your browser and go to `http://127.0.0.1:8080`.

3. Upload an image of a tomato leaf and click on the "Predict" button. The model will predict the disease and show treatment recommendations.

## How It Works

1. **Image Upload**: Users upload a tomato leaf image via the frontend form.
2. **Image Processing**: The image is sent to the Flask backend, where it is processed and passed to the trained machine learning model.
3. **Prediction**: The model predicts if the tomato leaf is healthy or has a disease, and returns the result.
4. **Treatment**: The application provides treatment recommendations based on the predicted disease.


## Acknowledgments

- The dataset used for training the model.
- TensorFlow for the deep learning model.
- Flask for creating the web application.

