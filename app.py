import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import json

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('mobilefacenet_trained.h5')

model = load_model()

# Load class indices
def load_class_indices():
    with open('class_indices.json', 'r') as f:
        class_indices = json.load(f)
    # Reverse mapping: index to name
    idx_to_name = {v: k for k, v in class_indices.items()}
    return idx_to_name

idx_to_name = load_class_indices()

st.title('Facial Recognition App')

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    # Display the image at a smaller width
    st.image(image, caption='Uploaded Image', width=200)
    
    # Preprocess the image (update this as per your model's requirements)
    img = image.resize((112, 112))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict
    prediction = model.predict(img_array)
    pred_idx = np.argmax(prediction)
    pred_name = idx_to_name.get(pred_idx, 'Unknown')
    st.write('Prediction:', pred_name)