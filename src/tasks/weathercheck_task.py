"""
This module defines the WeatherAnalaysisTask class to handle weather-related tasks.
The task uses the WeatherAgent to analyze weather data for a specified city.
"""

from crewai import Task
from textwrap import dedent

class WeatherTasks:
    """
    Defines the WeatherAnalaysisTask for analyzing weather data related to a specified city.
    This task interacts with the WeatherAgent to fetch and summarize weather information.
    """

    @staticmethod
    def WeatherAnalaysisTask(agent, city):
        """
        Creates and returns a Task to analyze weather data for a specified city.
        
        Args:
            agent (Agent): The WeatherAgent that analyzes weather data.
            city (str): The name of the city for weather analysis.

        Returns:
            Task: A Task object that encapsulates the weather analysis task.
        """
        return Task(
            description=dedent(f"""
                Analyze weather information. Consider all information.
                Answer the question using the weather information.
                {city}
            """),
            agent=agent,
            expected_output="Answer question using weather information"
        )
