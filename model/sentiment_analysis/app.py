import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import youtube as yt
from target_based_analysis_page import target
from aboutus import about_us
from PIL import Image 
from link import link_analysis

def home():

    st.write("Understanding Audience Feedback Effectively")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown("""<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'><h2>Welcome to Sentiment-Hub</h2>
Here we delve into the heartbeat of social media conversations. Our cutting-edge sentiment analysis tools decode the emotions hidden in every comment, offering a unique perspective on audience engagement and content reception. Analyzing sentiments in comments provides valuable insights into audience reactions, preferences, and opinions, which can be beneficial for content creators, marketers, and platform administrators
""", unsafe_allow_html=True)


def main():
    st.title("Sentiment-Hub")

    menu = ["Home", "Link Analysis", "Target Analysis"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Home":
        home()
    elif choice == "Link Analysis":
        link_analysis()
    elif choice == "Target Analysis":
        target()
    
if __name__ == "__main__":
    main()
