![bbc_cnn_newsScrapping](https://github.com/user-attachments/assets/77caa25f-3ca9-4b84-9915-7c4bb635a127)

<h1>BeautifulSoup News Scraper</h1>

<h2>Overview</h2>
<p>This project scrapes news headlines from BBC and CNN using BeautifulSoup and performs sentiment analysis on the headlines using TextBlob.</p>

<h2>Features</h2>
<ul>
  <li>Scrapes the top 10 news headlines from BBC and CNN.</li>
  <li>Performs sentiment analysis (Positive, Negative, or Neutral) on each headline.</li>
  <li>Prints the headlines along with their sentiment classification.</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Install the required libraries:
    <pre><code>pip install requests beautifulsoup4 textblob</code></pre>
  </li>
  <li>Run the script:
    <pre><code>python scraper.py</code></pre>
  </li>
  <li>View the scraped headlines and sentiment analysis in the terminal.</li>
</ol>

<h2>Example Output</h2>
<pre>
Source: BBC
Headline: "Global climate summit sparks hope for change"
Sentiment: Positive
----------------------------------------
Source: CNN
Headline: "Economic turmoil continues in major markets"
Sentiment: Negative
----------------------------------------
</pre>

<h2>Dependencies</h2>
<ul>
  <li>Python 3.x</li>
  <li>BeautifulSoup4</li>
  <li>Requests</li>
  <li>TextBlob</li>
</ul>

<h2>Note</h2>
<p>Ensure the HTML structure of the websites is up to date with the selectors in the code. If headlines are not appearing, inspect the website and update the tag/class selectors accordingly.</p>
