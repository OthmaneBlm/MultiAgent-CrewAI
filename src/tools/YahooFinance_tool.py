"""
This script defines a tool for fetching real-time stock data and historical information using Yahoo Finance.

### Features:
- Fetches real-time stock data and historical data (price movements, trading volume, etc.) for a single stock ticker.
- Provides historical stock data and real-time stock information for a list of tickers.
- Handles errors and provides meaningful error messages in case of failed API calls.

### Dependencies:
- `yfinance`: For fetching stock data from Yahoo Finance.
- `requests`: For making HTTP requests (SSL verification disabled).
- `langchain.tools`: To integrate the finance tool into a larger system.
"""

from langchain.tools import tool
import yfinance as yf
from dotenv import load_dotenv
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings (optional)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Fetch data with SSL verification disabled
session = requests.Session()
session.verify = False

class YHTools:
    
    @tool("Fetch Yahoo Finance Data")
    def get_yahoo_finance_data(ticker: str, period: str = '1d', interval: str = '1m'):
        """
        Fetches real-time stock data and historical information from Yahoo Finance for a given stock ticker.

        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL').
            period (str): The period for historical data (default: '1d').
            interval (str): The interval for historical data (default: '1m').

        Returns:
            dict: A dictionary containing historical data and stock information or an error message if the request fails.
        """
        try:
            # Fetch stock data using yfinance
            stock = yf.Ticker(ticker, session=session)
            yf_data = stock.history(period=period, interval=interval)  # Synchronous call for historical data
            yf_realtime = stock.info  # Fetch real-time stock info

            # Prepare the formatted result
            input_data = f"""
            Yahoo Finance Data:
            {yf_realtime}
            Recent Stock History:
            {yf_data.tail().to_string() if yf_data is not None else 'Data unavailable'}"""
            
            return input_data
        except Exception as e:
            # Handle any errors and return a meaningful message
            return {"error": f"Error fetching Yahoo Finance data for {ticker}: {e}"}
            
    @tool("Fetch Yahoo Finance Data for stocks to compare")
    def get_yahoo_finance_data_comparison(tickers: list, period: str = '1d', interval: str = '1m'):
        """
        Fetches real-time stock data and historical information from Yahoo Finance for a list of stock tickers.

        Args:
            tickers (list): A list of stock ticker symbols (e.g., ['AAPL', 'AMZN']).
            period (str): The period for historical data (default: '1d').
            interval (str): The interval for historical data (default: '1m').

        Returns:
            dict: A dictionary containing historical data and stock information for each ticker or an error message.
        """
        try:
            results = {}
            # Fetch data for each ticker in the list
            for ticker in tickers:
                stock = yf.Ticker(ticker, session=session)
                yf_data = stock.history(period=period, interval=interval)  # Synchronous call for historical data
                yf_realtime = stock.info  # Fetch real-time stock info
                
                # Prepare the formatted result for each stock
                input_data = f"""
                Yahoo Finance Data for {ticker}:
                {yf_realtime}
                Recent Stock History for {ticker}:
                {yf_data.tail().to_string() if yf_data is not None else 'Data unavailable'}"""
                
                results[ticker] = input_data
            return results
        except Exception as e:
            # Handle errors and return a meaningful message
            return {"error": f"Error fetching Yahoo Finance data for {tickers}: {e}"}
