"""
This module defines the StockcomparisonTask class to handle stock comparisons.
The task uses the StockAgent to compare multiple stocks based on their data.
"""

from crewai import Task
from textwrap import dedent

class CompareTasks:
    """
    Defines the StockcomparisonTask for comparing multiple stocks based on provided information.
    This task interacts with the StockAgent to analyze and compare stock data.
    """

    @staticmethod
    def StockcomparisonTask(agent, stocks):
        """
        Creates and returns a Task to compare multiple stocks based on their data.
        
        Args:
            agent (Agent): The StockAgent that performs stock comparisons.
            stocks (list): A list of stock ticker symbols to be compared.

        Returns:
            Task: A Task object that encapsulates the stock comparison task.
        """
        return Task(
            description=dedent(f"""
                Compare the following stocks based on the provided information:
                {stocks}
                Highlight key differences and similarities.
            """),
            agent=agent,
            expected_output="Provide a concise summary of analyses."
        )
