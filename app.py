import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import PIL
import validators
import requests
from io import BytesIO

how_to_use_it = """
  1. Enter a **cat** or **dog** image link or upload it from your computer.
  2. Choose a model. 
  3. Hit on the 'What do you see' button to predict the image.
  4. Wait for the prediction.
  5. Repeat the process if you want to continue.
"""

warning = 'This is only a **cat and dog image classifier**, therefore you **MUST** only provide cat and dog image or the result will be inacurate.'


def resize_and_read_img(img, img_shape=(1000, 700)):
    return st.image(img.resize(img_shape))


def upload_image(upload_type):
    if upload_type == 'Computer':
        image_file = st.file_uploader(
            label='Choose a file from your computer', type=['png', 'jpg', 'jpeg'])
        if image_file is not None:
            img = Image.open(image_file)
            resize_and_read_img(img)
            prep_img = preprocess_img(img)
            return prep_img

    elif upload_type == 'Url':
        img_url = st.text_input('Enter Url')
        if img_url and not validators.url(img_url):
            st.error('Not a valid url. Please enter a valid one')

        elif img_url and validators.url(img_url):
            response = requests.get(img_url)
            try:
                img = Image.open(BytesIO(response.content))
                resize_and_read_img(img)
                prep_img = preprocess_img(img)
                return prep_img
            except PIL.UnidentifiedImageError:
                st.error(
                    'An unexpected error occured, please retry or upload another image link.')


def preprocess_img(img):
    img = tf.constant(img, dtype=tf.float32)
    img = tf.image.resize(img, [224, 224])
    img = img / 255.

    return tf.expand_dims(img, axis=0)


@st.cache_resource
def load_model(model_name):
    if model_name == 'Default':
        default_model = tf.keras.models.load_model('models/cat_dog_model.h5')
        return default_model
    elif model_name == 'EfficientNetB0':
        custom_objects = {'KerasLayer': hub.KerasLayer}
        efficentnetb0 = tf.keras.models.load_model(
            'models/cat_dog_pretrained.h5', custom_objects=custom_objects)
        return efficentnetb0


def predict_image(prep_img, model_name):
    model = load_model(model_name)
    pred = tf.round(model.predict(prep_img)).numpy()
    pred_label = 'cat' if pred == 0 else 'dog'
    return pred_label


def main():
    st.title('Cat and Dog Image Classification')
    st.subheader(
        'Classify cat and dog images using deep learning with TensorFlow')
    img = Image.open('cat-and-dog.jpg')
    st.image(img, use_column_width=True)

    with st.expander("How to use it ?"):
        st.info(how_to_use_it)
        st.warning(warning)

    st.markdown("---")

    upload_type = st.radio("Upload image from", options=['Computer', 'Url'])

    img = upload_image(upload_type=upload_type)

    model_name = st.selectbox('Choose a model', options=[
                              'Default', 'EfficientNetB0'])

    if model_name == 'Default':
        st.info(
            'This a the default model. It has been built from scratch and has an accuracy close to 90 percent.')
    else:
        st.info('This a pretrained model. It performs better than the default one (which is also good) with an accuracy close to 97 percent.')

    if img is not None:
        if st.button('What do you see ?'):
            pred = predict_image(img, model_name)
            st.write(f'I see a **{pred}**')


if __name__ == '__main__':
    main()
