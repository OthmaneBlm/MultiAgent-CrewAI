"""
This module defines the NewsAnalysisTask class to handle news analysis.
The task uses the StockAgent to analyze recent news related to stocks and provide a concise summary.
"""

from crewai import Task
from textwrap import dedent

class NewsTasks:
    """
    Defines the NewsAnalysisTask for analyzing news articles related to specific stocks.
    This task interacts with the StockAgent to fetch news articles and provide insights.
    """

    @staticmethod
    def NewsAnalysisTask(agent, query):
        """
        Creates and returns a Task to analyze recent news articles related to stocks.
        
        Args:
            agent (Agent): The StockAgent that analyzes news articles.
            query (str): The search query or news topic.

        Returns:
            Task: A Task object that encapsulates the news analysis task.
        """
        return Task(
            description=dedent(f"""
                Analyze recent news articles related to specific stocks or the overall market.
                Consider the potential impact of news events on stock prices or market trends.
                Provide a concise summary of key news items and their potential market implications.
                {query}
            """),
            agent=agent,
            expected_output="Provide a concise summary of key news items and their potential market implications."
        )
