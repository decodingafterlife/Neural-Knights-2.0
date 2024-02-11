from youtube import Youtube as yt
import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
import analysis
from wordcloud import WordCloud, STOPWORDS
import warnings

# Suppress Streamlit warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def target():

    st.title("Target Analysis")

    target = st.text_input("Enter the target:")

    if target:
        # Providing the API key
        api_key = "youtube-api-key"

        # Initializing object of youtube class
        target_analysis = yt(api_key)

        # Getting Youtube API service
        youtube_api_service = target_analysis.get_youtube_api_service()

        

        # Getting max number of comments from the user
        max_results = st.number_input("Enter maximum number of videos", value=1, min_value = 1, max_value = 20)

        button = st.button("Analyze")

        if button:

            # Getting video ids
            video_ids = target_analysis.search_videos(youtube_api_service, target, max_results)

            # Fetching comment for each video and then storing it into the single pandas dataframe
            data = pd.DataFrame()

            # Fetching comment for the each video
            for video_id in video_ids:
                temp = target_analysis.get_data(video_id)
                data = pd.concat([data, temp], ignore_index=True)

            # Displaying the title of each video
            target_details = []
            for video_id in video_ids:
                target_details.append(target_analysis.get_video_details(youtube_api_service, video_id))
            
            st.write("Titles:")
            for video in target_details:
                if video:
                    title = video['title']
                    st.write(title)

            #showing fetched comments
            st.dataframe(data, hide_index=True)
                
            # Getting comments
            comments = target_analysis.get_comments(data)
            
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