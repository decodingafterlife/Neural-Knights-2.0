import streamlit as st
from youtube_link_analysis_page import video
from instagram_link_analysis import post
from urllib.parse import urlparse


def link_analysis():


    st.write("Enter link from the social media platform")

    url = st.text_input("Enter video link:")

    button = st.button("Enter")
    
    if button:


        # Parse the URL to identify the platform
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain == 'www.instagram.com':
            # Extract comments from Instagram
            post(url)
        elif domain == 'www.youtube.com':
            # Extract comments from YouTube
            video(url)
        else:
            st.write("Unsupported platform.")
    