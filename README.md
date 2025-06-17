# Facial Recognition App

This project is a facial recognition system built with TensorFlow/Keras and features a user-friendly Streamlit web app for real-time predictions.

## Features

- Train and test a facial recognition model using your own dataset.
- Upload images via a Streamlit web interface to identify people.
- Handles large model files with Git LFS.

## Project Structure

```
.
├── app.py                  # Streamlit app for facial recognition
├── model_train.ipynb       # Notebook for training the model
├── model_test.ipynb        # Notebook for testing the model
├── mobilefacenet_trained.h5# Trained model (tracked with Git LFS)
├── class_indices.json      # Mapping of class indices to names
├── requirements.txt        # Python dependencies
├── download_images.py     # Automatically download the desired number of images from google
├── image_crop.py           # Crop the images to train the model
├── dataset/                # Raw images for training
├── cropped/                # Cropped/processed images
├── original/               # Original images downloaded from google
└── faceenv/                # Conda environment (optional)
```

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/Nishantr846/Facial-Recognition-App.git
cd Facial-Recognition-App
```

### 2. Install Git LFS

If you haven’t already:
```sh
git lfs install
```

### 3. Pull LFS files

```sh
git lfs pull
```

### 4. Create and activate a Python environment

You can use conda or venv. Example with conda:
```sh
conda create -n faceenv python=3.8
conda activate faceenv
```

### 5. Install dependencies

```sh
pip install -r requirements.txt
```

## Running the Streamlit App

```sh
streamlit run app.py
```

- Upload an image to get the predicted person’s name.

## Training

- Use `model_train.ipynb` to train your model on your dataset.
- Use `model_test.ipynb` to evaluate the model.

## Notes

- The model file (`mobilefacenet_trained.h5`) is tracked with Git LFS due to its large size.
- Update `class_indices.json` if you add or remove classes.

## License

MIT License
