"""
Subfolder: messages
Role: This subfolder defines the data structures for communication between agents and workflows. 
It standardizes how messages and queries are formatted and passed across the system.

File: state.py
Purpose: Defines the `AgentState` message structure, which encapsulates the input and intermediate state of the agents.
"""

from typing import TypedDict, List

class AgentState(TypedDict):
    """
    A typed dictionary to define the structure of agent states/messages.
    This ensures consistency in how data is passed between different agents and workflows.
    """
    messages: List[str]  # List of all messages exchanged
    query: str           # The user's input query
    stock: str           # Stock-related information
    news: str            # News-related information
    city: str            # City name for weather queries
    stock_list: List[str]  # List of stocks for comparison or analysis