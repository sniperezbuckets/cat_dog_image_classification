# Dog and Cat Image Classification with Streamlit

This repository contains code and resources for a dog and cat image classification project using Streamlit. The project includes a notebook for experimentation, trained models for classification, and a Streamlit app for interactive visualization.

## Project Structure

The repository is organized as follows:

- `notebook/`: This directory contains the Jupyter notebook (`experimentation.ipynb`) where the initial data exploration, preprocessing, and model experimentation were carried out.

- `model/`: This directory contains the trained models used for classification.

  - `cnn_model/`: This subdirectory contains the source code and weights for a Convolutional Neural Network (CNN) model that was built from scratch and achieved an accuracy of 90%. It includes both the model architecture and the trained weights.

  - `efficientnet_model/`: This subdirectory contains the code and weights for a pre-trained EfficientNetB0 model, which achieved an accuracy of 97%. It includes both the model architecture and the pre-trained weights.

- `app.py`: This file contains the Streamlit code for the interactive web application. Users can upload images of dogs and cats to the app and get real-time predictions using the trained models.

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

