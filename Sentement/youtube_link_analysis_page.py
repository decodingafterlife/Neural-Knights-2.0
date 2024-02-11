from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import analysis

def download_results1():
    # Your function call or code to execute when the button is clicked
    # For example, you can print a message
    print("Downloading results for first model...")

def video(video_link):

    st.title("Youtube Analysis")

    if video_link:
        # Providing the API key
        api_key = "youtube-api-key"

        # Initializing object of youtube class
        video_analysis = yt(api_key)

        # Getting Youtube API service
        youtube_api_service = video_analysis.get_youtube_api_service()

        # Getting video id based on the link
        video_id = video_analysis.get_video_id(video_link)

        # Getting max number of comments from the user
        max_results = st.number_input("Enter maximum number of comments", value=100, min_value = 1, max_value = 200)


        if True:

            data = video_analysis.get_data(video_id, max_results)

            video_details = video_analysis.get_video_details(youtube_api_service, video_id)

            if video_details:
                title = video_details['title']
                st.write("Title: " + title)

            st.dataframe(data, hide_index=True)

            comments = video_analysis.get_comments(data)
            
            # Set up the inference pipeline using the first model
            sentiment_analysis1 = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
            # Set up the inference pipeline using the second model
            sentiment_analysis2 = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")

            predictions1 = None
            predictions2 = None

            # Making predictions
            if comments:
                predictions1 = sentiment_analysis1(comments)
                predictions2 = sentiment_analysis2(comments)
            else:
                st.write("No comments found")

            # Visualize the sentiments
            if predictions1 and predictions2:
                df1 = pd.DataFrame(predictions1)
                df2 = pd.DataFrame(predictions2)

                # Visualize the sentiments
                df1_chart = analysis.pie_chart(df1)
                df2_chart = analysis.pie_chart(df2)


                # Merge the DataFrames column-wise
                merged_df1 = pd.concat([data, df2], axis= 1)
                merged_df2 = pd.concat([data, df2], axis=1)

                st.write("Sentiment Analysis Results:")
                st.dataframe(merged_df1, hide_index=True)
                st.dataframe(merged_df2, hide_index=True)

                # Plotting the wordcloud for the particular category
                analysis.positive_wordcloud(merged_df1)
                analysis.negative_wordcloud(merged_df1)
                analysis.neutral_wordcloud(merged_df1)

                