import streamlit as st
import instagram
import pandas as pd
from transformers import pipeline
import analysis

def post(post_link):

    st.write("Instagram Analysis")

    # Getting max number of comments from the user
    max_length = st.number_input("Enter maximum comments duration", value=30, min_value = 1, max_value = 100)

    button = st.button("Analyze")

    if button:

        data = instagram.extract_instagram_comments(post_link, max_length)

        st.dataframe(data, hide_index=True)

        comments = data["Comment"].tolist()
            
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

            # Plotting the wordcloud for the particular category
            analysis.positive_wordcloud(merged_df1)
            analysis.negative_wordcloud(merged_df1)
            analysis.neutral_wordcloud(merged_df1)

            # Download the data
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode('utf-8')

            csv1 = convert_df(merged_df1)
            csv2 = convert_df(merged_df2)

            download_button_1 = st.download_button(
                label="Download Results for first Model",
                data=csv1,
                file_name='sentiment_analysis_results1.csv',
                mime='text/csv'
            )

            download_button_2 = st.download_button(
                label="Download Results for second Model",
                data=csv2,
                file_name='sentiment_analysis_results.csv',
                mime='text/csv',
            )    