"""
This module defines the StockAnalaysisTask class to handle stock analysis.
The task uses the StockAgent to analyze real-time stock data and provide a concise summary.
"""

from crewai import Task
from textwrap import dedent

class StockTasks:
    """
    Defines the StockAnalaysisTask for performing stock analysis based on stock tickers.
    This task interacts with the StockAgent to fetch real-time stock data and provide insights.
    """

    @staticmethod
    def StockAnalaysisTask(agent, stock):
        """
        Creates and returns a Task to analyze real-time stock data and provide insights.
        
        Args:
            agent (Agent): The StockAgent that analyzes stock data.
            stock (str): The stock ticker symbol.

        Returns:
            Task: A Task object that encapsulates the stock analysis task.
        """
        return Task(
            description=dedent(f"""
                Analyze real-time stock data and provide insights.
                Consider price movements, trading volume, and any available company information.
                Provide a concise summary of the stock's current status and any notable trends or events.
                {stock}
            """),
            agent=agent,
            expected_output="Concise summary of the stock's current status and any notable trends or events."
        )
