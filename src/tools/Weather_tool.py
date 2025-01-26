"""
This script defines a tool to fetch current weather data for a given city using the WeatherAPI.

### Features:
- Fetches current weather data for a specified city using the WeatherAPI.
- Returns weather details such as temperature, humidity, and weather conditions.
- Handles errors gracefully and returns appropriate error messages if data is unavailable.

### Dependencies:
- `requests`: For making HTTP requests to the WeatherAPI.
- `dotenv`: For securely loading API keys.
- `langchain.tools`: To integrate the weather tool into a larger system.
"""

from langchain.tools import tool
from dotenv import load_dotenv
import os
import requests

# Load environment variables securely
load_dotenv('.env')

# Fetch the WeatherAPI key from environment variables
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

class WeatherTools:
    
    @tool('Fetch weather data')
    def get_weather(query: str):
        """
        Fetches current weather information for a given city using WeatherAPI.

        Args:
            query (str): The city name for which to retrieve weather data.
        
        Returns:
            dict: A dictionary containing weather indicators or an error message if data is unavailable.
        """
        # Construct the endpoint URL for the weather API request
        endpoint = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={query}"

        try:
            # Send the GET request to fetch the weather data
            response = requests.get(endpoint)
            data = response.json()

            # Check if data for the location is found and return the result
            if data.get("location"):
                return data
            else:
                return {"error": "Weather data not found"}
        
        except Exception as e:
            # Handle any request or API errors
            print(f"Error fetching weather data for {query}: {e}")
            return {"error": f"Error fetching weather data: {e}"}
