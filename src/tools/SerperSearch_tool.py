"""
This script defines a tool to perform web searches using the Serper API to answer user queries.
It fetches relevant web links and their details based on a given query.

### Features:
- Sends a search query to Serper's web search service.
- Returns search results in a structured format, including web links and details.
- Handles errors gracefully and returns appropriate error messages.

### Dependencies:
- `http.client`: For making HTTP requests.
- `json`: For formatting the payload and response.
- `dotenv`: For securely loading API keys.
- `langchain.tools`: To integrate the search function into a larger system.
"""

from langchain.tools import tool
from dotenv import load_dotenv
import json 
import os
import http.client

# Load environment variables securely
load_dotenv('.env')

# Fetch the Serper API key from environment variables
SERPER_API_KEY = os.environ['SERPER_SEARCH_API']

# Set up the HTTPS connection to Serper's search endpoint
conn = http.client.HTTPSConnection("google.serper.dev")

class SerperTools:
    
    @tool("Fetch web search data")
    def search_query(query: str):
        """
        Sends a search query to the Serper API and returns relevant web links.

        Args:
            query (str): The user query to search on the web.
        
        Returns:
            dict: A dictionary containing search results or an error message if failed.
        """
        # Prepare the payload and headers for the API request
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': SERPER_API_KEY,
            'Content-Type': 'application/json'
        }

        try:
            # Make the POST request to the Serper API
            conn.request("POST", "/search", payload, headers)
            res = conn.getresponse()
            data = res.read()

            # Print the raw data for debugging (optional)
            print("This is the data: ", data)

            # Decode and return the response as a UTF-8 string
            return data.decode("utf-8")
        
        except Exception as e:
            # Handle errors gracefully and return a helpful error message
            print(f"Error getting search details for {query}: {e}")
            return {"error": f"Error fetching search links: {e}"}
