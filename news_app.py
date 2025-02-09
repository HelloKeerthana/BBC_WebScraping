import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import streamlit as st

# News sources
news_sources = {
    'BBC': 'https://www.bbc.com/news',
    'CNN': 'https://edition.cnn.com/world'
}

news_data = []

def scrape_bbc():
    url = news_sources['BBC']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3')
    
    for headline in headlines[:10]:
        text = headline.get_text(strip=True)
        if text:
            sentiment = TextBlob(text).sentiment.polarity
            news_data.append({
                'Source': 'BBC',
                'Headline': text,
                'Sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
            })

def scrape_cnn():
    url = news_sources['CNN']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('span', class_='container__headline-text')

    for headline in headlines[:10]:
        text = headline.get_text(strip=True)
        if text:
            sentiment = TextBlob(text).sentiment.polarity
            news_data.append({
                'Source': 'CNN',
                'Headline': text,
                'Sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
            })

# Streamlit UI
st.title("News Headline Sentiment Analysis")
st.write("Scraping and analyzing headlines from BBC and CNN.")

if st.button("Scrape News"):
    news_data.clear()  # Clear previous data
    scrape_bbc()
    scrape_cnn()
    st.success("Scraping completed!")

if news_data:
    st.subheader("News Headlines and Sentiments")
    for news in news_data:
        st.write(f"**Source:** {news['Source']}")
        st.write(f"**Headline:** {news['Headline']}")
        st.write(f"**Sentiment:** {news['Sentiment']}")
        st.markdown("---")
    
    # Sentiment Distribution Chart
    st.subheader("Sentiment Distribution")
    sentiment_counts = {
        'Positive': sum(1 for news in news_data if news['Sentiment'] == 'Positive'),
        'Neutral': sum(1 for news in news_data if news['Sentiment'] == 'Neutral'),
        'Negative': sum(1 for news in news_data if news['Sentiment'] == 'Negative'),
    }
    st.bar_chart(sentiment_counts)
else:
    st.info("Click the button to scrape news and see the results.")
