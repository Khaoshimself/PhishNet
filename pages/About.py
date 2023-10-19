import streamlit as st
from PIL import Image

import streamlit as st
from PIL import Image

# Define your logo
logo = '<img src="Logo.jpg" style="max-width: 150px;">'

# Apply a color theme (optional)
st.markdown(
    """
    <style>
        .title {
            color: #009688;
            text-align: center;
        }
        .header {
            color: #1565C0;
            text-align: center;
        }
        .description {
            color: #333;
            text-align: justify;
        }
        .teams {
            color: #FF5722;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered Title
st.markdown("<h1 class='title'>About</h1>", unsafe_allow_html=True)

# Main Content
st.header("What is PhishNet and what was the process like?")

image = Image.open('Logo.jpg')

st.image(image, caption='PhishNet Logo', width=300)

description = '''
PhishNet, our exciting venture in Fall 2023, exudes pure enthusiasm for thwarting email scams. With a tech arsenal featuring Python, Streamlit, and PyTorch, we set out to create a scam-busting marvel.

Our journey kicked off with a data adventure, curating and refining a dataset that would serve as our project's foundation. Witnessing the transformation from raw data to a high-quality training set was nothing short of a eureka moment, showcasing the pivotal role data quality plays in accurate scam detection.

Collaboration became our superpower, thanks to Git and GitHub. These tools turned teamwork into a seamless dance, allowing us to groove through development stages with synchronized finesse.

The heart of PhishNet beats with an advanced machine learning algorithm, meticulously crafted for pinpoint accuracy in identifying potential scams. The process was a delightful puzzle, with each refinement contributing to a more robust and reliable solution. The pursuit of algorithmic brilliance became a source of boundless joy.

As the finishing touch, we unveiled our creation on a cloud platform. The result? A user-friendly, accessible web application that invites users with open arms. This final step was a celebration of our commitment to user-centric design.

Through PhishNet, we learned that data quality is the secret sauce, collaboration is the melody, and algorithmic finesse is the dance that makes a project truly sing. This endeavor is not just a project; it's a celebration of our dedication to online security, wrapped in a ribbon of sheer joy.
'''
st.markdown(description, unsafe_allow_html=True)

# Teams
st.header("Teams")
st.markdown("<div class='teams'>", unsafe_allow_html=True)
st.write("Machine Learning")
st.write("Data Processing")
st.write("Streamlit")
st.markdown("</div>", unsafe_allow_html=True)
