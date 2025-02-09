import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Example URLs for scraping
news_sources = {
    'BBC': 'https://www.bbc.com/news'
}

news_data = []

# Function to scrape BBC headlines as an example
def scrape_bbc():
    url = news_sources['BBC']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3') # BBC headlines are in h2 tags and the following is the className of the div containing the headline

    for headline in headlines[:10]:  # Get top 10 headlines
        text = headline.get_text(strip=True)
        if text:
            sentiment = TextBlob(text).sentiment.polarity
            news_data.append({
                'Source': 'BBC',
                'Headline': text,
                'Sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
            })


# Call scraping functions
scrape_bbc()

# Print the scraped news data
for news in news_data:
    print(f"Source: {news['Source']}")
    print(f"Headline: {news['Headline']}")
    print(f"Sentiment: {news['Sentiment']}")
    print("-" * 40)

print("Scraping completed.")
