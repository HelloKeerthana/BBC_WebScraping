import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Example URLs for scraping
news_sources = {
    'BBC': 'https://www.bbc.com/news',
    'CNN': 'https://edition.cnn.com/world'
}

news_data = []

# Function to scrape BBC headlines as an example
def scrape_bbc():
    url = news_sources['BBC']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all <h2> elements with the specific class
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3')

    for headline in headlines[:5]:  # Get top 10 headlines
        text = headline.get_text(strip=True)
        if text:
            sentiment = TextBlob(text).sentiment.polarity
            news_data.append({
                'Source': 'BBC',
                'Headline': text,
                'Sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
            })

# Function to scrape CNN headlines as an example
def scrape_cnn():
    url = news_sources['CNN']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all <span> elements with the class 'container__headline-text'
    headlines = soup.find_all('span', class_='container__headline-text')

    for headline in headlines[:5]:
        text = headline.get_text(strip=True)
        if text:
            sentiment = TextBlob(text).sentiment.polarity
            news_data.append({
                'Source': 'CNN',
                'Headline': text,
                'Sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
            })

# Call scraping functions
scrape_bbc()
scrape_cnn()

# Print the scraped news data
for news in news_data:
    print(f"Source: {news['Source']}")
    print(f"Headline: {news['Headline']}")
    print(f"Sentiment: {news['Sentiment']}")
    print("-" * 40)

print("Scraping completed.")
