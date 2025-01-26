"""
This module defines the WebSearchTask class to facilitate web search tasks.
The task uses the SearchAgent to compile relevant search results and provide concise answers.
"""

from crewai import Task
from textwrap import dedent

class SearchTasks:
    """
    Defines the WebSearchTask for performing search operations based on user queries.
    This task interacts with the SearchAgent and compiles the results from web searches.
    """

    @staticmethod
    def WebSearchTask(agent, query):
        """
        Creates and returns a Task to perform web search and provide a summary of the results.
        
        Args:
            agent (Agent): The SearchAgent that handles web searches.
            query (str): The search query from the user.

        Returns:
            Task: A Task object that encapsulates the web search task.
        """
        return Task(
            description=dedent(f"""
                Compile the search output. Consider information relevant to the user query.
                Provide a concise answer to the user query from the search results. 
                If nothing in the search results is relevant to the user query, don't invent new things.
                {query}
            """),
            agent=agent,
            expected_output="Answer of query"
        )
