# Malarial Cell Disease Detection using Streamlit

This project is a deep learning-based web application developed using Streamlit to detect malaria infection from cell images. It uses a Convolutional Neural Network (CNN) model trained to classify cell images as either parasitized (infected) or uninfected.

## Features
- **User-Friendly Interface:** Upload cell images through a simple drag-and-drop interface.
- **Image Preprocessing:** Automatically resizes and normalizes the uploaded image.
- **Real-Time Prediction:** Provides infection results along with confidence scores.
- **Deep Learning Model:** Utilizes a pre-trained Keras model (`my_model.keras`).

## Dataset Used
The dataset used for training the model can be found [here](https://www.kaggle.com/datasets/ashishjangra27/malarial-cell-image).


## Technologies Used
- Python
- TensorFlow/Keras
- Streamlit
- Pillow
- NumPy

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-link>
   ```
2. Install required packages:
   ```bash
   pip install streamlit tensorflow pillow numpy
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run malaria_detection_app.py
   ```

## Project Structure
- `model/my_model.keras`: Pre-trained malaria detection model.
- `malaria_detection_app.py`: Main Streamlit application code.
- `README.md`: Project documentation.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests.

## License
This project is open-source and available under the MIT License.

