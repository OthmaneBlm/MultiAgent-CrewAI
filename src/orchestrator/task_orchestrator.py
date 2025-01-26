"""
This module defines the Orchestrator class, responsible for routing queries 
based on the category of the query.
The route_query method directs the query to the appropriate category-specific task.
"""



class Orchestrator:
    """
    The Orchestrator class is responsible for routing queries based on their category.
    The route_query method evaluates the category in the query and returns the appropriate handler.
    """

    @staticmethod
    def route_query(state):
        """
        Routes the query based on its category to the appropriate task handler.

        Args:
            state (dict): The state containing the query information, including the category.

        Returns:
            str: The appropriate task handler category ('stock', 'city', 'search', or 'reply').
        """
        category = state.get('category', 'other')
        print("Category: ", category)
        
        # Routing logic based on the category
        if category in ['stock_analysis', 'stock_news', 'stock_comparison']:
            return "stock"
        elif category == 'city_weather':
            return "city"
        elif category == "other":
            return "search"
        else:
            return "reply"
