import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

# Load your trained model
model = load_model(r"C:\Users\haris\Machine Learning\Deep learning\malaria_cell_detection.h5")  # Updated model path

# Title and description
st.title("Malarial Cell Disease Detection")
st.write("Upload an image of the cell")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image = image.resize((64, 64))
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Prediction button
    if st.button("Predict"):
        prediction = model.predict(image_array)[0][0]  # Extracting the prediction value directly
        confidence = prediction * 100  # Convert to percentage confidence
        if prediction > 0.5:
            st.write(f"### Cell is Parasitized with {confidence:.2f}% confidence")
        else:
            st.write(f"### Cell is Uninfected with {(100-confidence):.2f}% confidence")

# Run the Streamlit app using: streamlit run filename.py
