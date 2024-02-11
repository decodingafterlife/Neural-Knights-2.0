import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import warnings

# Suppress Streamlit warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def pie_chart(df):
    """
    Generate a pie chart to visualize sentiment distribution.

    Parameters:
    - df: DataFrame containing 'label' column indicating sentiment.

    Returns:
    None
    """
    sentiment_counts = df['label'].value_counts()
    total = len(df)  # Total number of samples
    
    colors = plt.cm.tab10.colors  # Use predefined color map for distinct colors
    
    # Create the pie chart
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    patches, _, _ = ax.pie(sentiment_counts, labels=sentiment_counts.index, startangle=90, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax.legend(loc='best', bbox_to_anchor=(0.5, 0.5))

    st.pyplot(fig)

    # Create the table
    table_data = {'Index': range(1, len(sentiment_counts)+1), 'Sentiment': sentiment_counts.index, 'Count': sentiment_counts.values}
    color_mapping = {sentiment: color for sentiment, color in zip(sentiment_counts.index, colors)}
    table_df = pd.DataFrame(table_data)
    table_df['Percentage'] = (table_df['Count'] / total) * 100  # Calculate percentages
    

    st.sidebar.table(table_df.set_index('Index'))


    



def positive_wordcloud(merged_df):
    """
    Generate a word cloud for positive comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    positive_comments = merged_df['Comment'][merged_df["label"] == 'POS']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    positive_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(positive_comments))
    plt.figure()
    plt.title("Positive comments - Wordcloud")
    plt.imshow(positive_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()

def negative_wordcloud(merged_df):
    """
    Generate a word cloud for negative comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    negative_comments = merged_df['Comment'][merged_df["label"] == 'NEG']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    negative_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(negative_comments))
    plt.figure()
    plt.title("Negative comments - Wordcloud")
    plt.imshow(negative_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()

def neutral_wordcloud(merged_df):
    """
    Generate a word cloud for neutral comments.

    Parameters:
    - merged_df: DataFrame containing 'label' and 'comment' columns.

    Returns:
    None
    """
    neutral_comments = merged_df['Comment'][merged_df["label"] == 'NEU']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    positive_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words).generate(str(neutral_comments))
    plt.figure()
    plt.title("Neutral comments - Wordcloud")
    plt.imshow(positive_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()




