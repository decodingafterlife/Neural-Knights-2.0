import sys
import pandas as pd
sys.path.append('/home/amey/Desktop/DevKraft/Sentement/')
from youtube import Youtube as yt
from urllib.parse import urlparse
import analysis
from transformers import pipeline
import instagram
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

url = sys.argv[3]

def display_results(predictions):
    df2 = pd.DataFrame(predictions)

    sentiment_counts = df2['label'].value_counts()
    total = len(df2)
    table_data = {'Index': range(1, len(sentiment_counts)+1), 'Sentiment': sentiment_counts.index, 'Count': sentiment_counts.values}
    table_df = pd.DataFrame(table_data)
    table_df['Percentage'] = (table_df['Count'] / total) * 100 

    emotions = ["neutral", "joy", "surprise", "anger", "sadness", "fear", "disgust"]
    for i in range(7):
        not_found = True
        for j in range(len(table_df)):
            if emotions[i] == table_df["Sentiment"].iloc[j]:
                print(table_df["Percentage"].iloc[j])
                not_found = False
                break
        if not_found:
            print(0)

    
def video(video_link, model2):

    if video_link:
        # Providing the API key
        api_key = "AIzaSyCFEieCDS70gjiOWy8f90JaNqu5Ithn5Qo"

        # Initializing object of youtube class
        video_analysis = yt(api_key)

        # Getting Youtube API service
        youtube_api_service = video_analysis.get_youtube_api_service()

        # Getting video id based on the link
        video_id = video_analysis.get_video_id(video_link)


        data = video_analysis.get_data(video_id, 30)

        comments = video_analysis.get_comments(data)
            
        # predictions1 = sentiment_analysis1(comments)
        predictions = model2(comments)

        display_results(predictions)


def post(post_link, model2):

    data = instagram.extract_instagram_comments(post_link, 20)

    comments = data["Comment"].tolist()
    predictions = model2(comments)
    display_results(predictions)
                

# Set up the inference pipeline using the first model
sentiment_analysis1 = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
# Set up the inference pipeline using the second model
sentiment_analysis2 = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")

# Parse the URL to identify the platform
parsed_url = urlparse(url)
domain = parsed_url.netloc
if domain == 'www.instagram.com':
    # Extract comments from Instagram
    post(url, sentiment_analysis1)
elif domain == 'www.youtube.com':
    # Extract comments from YouTube
    video(url, sentiment_analysis1)


