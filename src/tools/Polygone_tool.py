"""
This script defines a tool for fetching news articles related to specific stock tickers 
from the Polygon.io API.

### Features:
- Fetches recent news articles about a given stock ticker symbol.
- Limits the number of articles returned (default is 1).
- Uses the Polygon.io API to retrieve real-time data about stock-related news.
- Handles errors gracefully if the API request fails.

### Dependencies:
- `requests`: To make HTTP requests to the Polygon.io API.
- `dotenv`: For loading environment variables securely.
- `langchain.tools`: For integrating the function as a tool in a larger system.
"""
from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os

# Suppress SSL warnings (optional)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Load environment variables
load_dotenv('.env')

# Constants
POLYGONE_API_KEY = os.environ['POLYGONE_API_KEY']
POLYGONE_BASE_URL = "https://api.polygon.io"

class Tools:
    
    @tool("Fetch Polygon News")
    def get_polygon_news(ticker: str, limit: int = 1):
        """
        Fetches recent news articles from Polygon.io related to a specific stock ticker.

        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL').
            limit (int): The number of news articles to fetch (default: 1).

        Returns:
            list: A list of news articles with details like headline, timestamp, and summary.
        """
        def fetch_news():
            try:
                # Define the API endpoint and parameters
                endpoint = "/v2/reference/news/"
                url = f"{POLYGONE_BASE_URL}{endpoint}"
                params = {"ticker": ticker, "limit": limit, "apiKey": POLYGONE_API_KEY}
                
                # Fetch the news data
                response = requests.get(url, params=params, verify=False)
                response.raise_for_status()  # Raise an exception for HTTP errors
                
                # Parse and return the relevant news
                news = response.json()
                print(news)
                return news['results'][:3]  # Return top 3 news articles
                
            except Exception as e:
                print(f"Error fetching Polygon.io news for {ticker}: {e}")
                return []

        # Return the fetched news
        return fetch_news()
