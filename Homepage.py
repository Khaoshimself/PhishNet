import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import time

st.title('PhishNet')

#image = Image.open('Logo.jpg')
#st.image(image, caption='PhishNet first logo')

#tabs
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

# To upload file
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)



