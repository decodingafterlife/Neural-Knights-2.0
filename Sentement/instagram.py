import instaloader
from googleapiclient.discovery import build
import pandas as pd
import re
from urllib.parse import urlparse
import streamlit as st

def extract_instagram_comments(post_url, limit=5):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()
    loader.login(user="id_diot", passwd="Tanmay@2004*")

    try:
        # Load the post by its URL
        post = instaloader.Post.from_shortcode(loader.context, post_url.split('/')[-2])
        
        # Initialize lists to store comments and usernames
        comments_list = []
        usernames_list = []
        
        # Counter for limiting the number of comments
        count = 0
        
        # Iterate over comments and store them in lists
        for comment in post.get_comments():
            if len(comment.text):
                continue
            comments_list.append(comment.text)
            usernames_list.append(comment.owner.username)  # Accessing the username through owner
            
            # Increment the counter
            count += 1
            
            # Break the loop if the limit is reached
            if count >= limit:
                break
        
        # Create a DataFrame
        df = pd.DataFrame({'Username': usernames_list, 'Comment': comments_list})
        
        return df
        
    except Exception as e:
        st.write("Error:", e)