from craiyon import Craiyon
from PIL import Image # pip install pillow
from io import BytesIO
import streamlit as st
import base64
def Generate(request):
    generator = Craiyon() # Instantiates the api wrapper
    result = generator.generate(request) # Generates 9 images by default
    images = result.images
    return images

generator = Craiyon(model_version="35s5hfwn9n78gb06")
st.title("AI Artist")
st.header("Hello, my name is Craiyon and I'm an AI digital artist!")
request = st.text_input("I am able to draw everything. Do you want to test me?","Ask me to draw something for you!")
if st.button("Draw"):
    image_files = Generate(request)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[0].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[1].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[2].encode("utf-8")))))
    with col2:
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[3].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[4].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[5].encode("utf-8")))))
    with col3:
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[6].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[7].encode("utf-8")))))
        st.image(Image.open(BytesIO(base64.decodebytes(image_files[8].encode("utf-8")))))
st.caption("This webpage has been developed by [Fabio Lonardoni](https://www.fabiolonardoni.it)")
