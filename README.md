# Dog and Cat Image Classification with Streamlit

This repository contains code and resources for a dog and cat image classification project using Streamlit. The project includes a notebook for experimentation, trained models for classification, and a Streamlit app for interactive visualization.
I have downloaded the data on [Kaggle.com](https://www.kaggle.com/).
You can get the data [here](https://drive.google.com/file/d/1w2Z-XREFr7bCLfLCJ5dKPo4osOsjjZxx/view?usp=sharing).

## Project Structure

The repository is organized as follows:

- `notebook/`: This directory contains the Jupyter notebook (`experimentation.ipynb`) where the initial data exploration, preprocessing, and model experimentation were carried out.

-  `data_preprocessing.py/`:  There are 12500 images of cats and 12500 images of dogs. The data was not preprocessed (all images in a single folder), Therefore I've created a simple python script to split the images into different folders, Train, Validation and test all containing subfolders of cat and dog images. The Test folder contains 10% and the validation folder 15% of the dataset (25000) images.

- `model/`: This directory contains the trained models used for classification.

  - `cnn_model/`: This subdirectory contains the source code and weights for a Convolutional Neural Network (CNN) model that was built from scratch and achieved an accuracy of 90%. It includes both the model architecture and the trained weights.

  - `efficientnet_model/`: This subdirectory contains the code and weights for a pre-trained EfficientNetB0 model, which achieved an accuracy of 97%. It includes both the model architecture and the pre-trained weights.

- `app.py`: This file contains the Streamlit code for the interactive web application. Users can upload images of dogs and cats to the app and get real-time predictions using the trained models.
- `requirements.txt`: This file contains all packages that need to be installed for the app to work.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/dog-cat-classification-streamlit.git

2. Navigate to the repository's directory:

   ```bash
   cd dog-cat-classification-streamlit
   
3. Install the required dependencies. It's recommended to create a virtual environment before installing the dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:

    ```bash
    streamlit run app.py

