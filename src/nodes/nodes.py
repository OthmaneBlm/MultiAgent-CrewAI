"""
Subfolder: nodes
Role: The purpose of this subfolder is to define nodes that orchestrate agent execution and workflow management.
Each node corresponds to an agent's task, guiding it to execute specific functionalities based on the current state.
The nodes facilitate the communication between various tasks (stock analysis, weather check, search tasks, etc.).
"""

from agents.Multi_agents import SearchAgents, StockAgents, WeatherAgents
from tasks.stock_task1 import StockTasks
from tasks.stock_task2 import NewsTasks
from tasks.stock_task3 import CompareTasks
from tasks.search_task import SearchTasks
from tasks.weathercheck_task import WeatherTasks
from langchain_openai import AzureChatOpenAI
import os 
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv('.env')

# API Keys and endpoints from environment variables
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
TAVILY_API_KEY = os.environ['TAVILY_API_KEY']
AZURE_OPENAI_API_VERSION = os.environ['AZURE_OPENAI_API_VERSION']
AZURE_OPENAI_API_KEY = os.environ['AZURE_OPENAI_API_KEY']
AZURE_OPENAI_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ['AZURE_OPENAI_DEPLOYMENT_NAME']

# Initialize the language model from OpenAI Azure
llm = AzureChatOpenAI(azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME, api_version=AZURE_OPENAI_API_VERSION)

class Nodes:
    """
    This class defines the different nodes for managing tasks and coordinating between agents. 
    Each node runs a specific task based on the input state and returns an updated message list.
    """

    def StockNode(self, state):
        """
        StockNode:
        - Handles stock analysis, news, or comparison tasks based on provided state.
        - If the 'stock' key is provided, it triggers stock analysis.
        - If 'news' is provided, it triggers stock news analysis.
        - If 'stock_list' is provided, it triggers comparison of stocks.
        """
        print("The state in node stock:#################", state)
        messages = state["messages"]
        
        if state["stock"]:
            stockAgent = StockAgents.StockAgent()
            stockTask = StockTasks.StockAnalaysisTask(stockAgent, state["stock"])
            result = stockTask.execute_sync()
            messages.append(result)
        
        elif state["news"]:
            stockAgent = StockAgents.StockAgent()
            NewsTask = NewsTasks.NewsAnalysisTask(stockAgent, state["news"])
            result = NewsTask.execute_sync()
            messages.append(result)
        
        elif state["stock_list"]:
            stockAgent = StockAgents.StockAgent()
            compareTask = CompareTasks.StockcomparisonTask(stockAgent, state["stock_list"])
            result = compareTask.execute_sync()
            messages.append(result)
        
        return {"messages": messages}
    
    def SearchNode(self, state):
        """
        SearchNode:
        - Handles web search tasks based on the user's query.
        - If 'query' is provided, it triggers the web search task and returns the result.
        """
        
        if state["query"]:
            searchAgent = SearchAgents.SearchAgent()
            websearchTask = SearchTasks.WebSearchTask(searchAgent, state["query"])
            result = websearchTask.execute_sync()
            messages = state["messages"]
            messages.append(result)
            return {"messages": messages}
    
    def WeatherNode(self, state):
        """
        WeatherNode:
        - Handles weather check tasks based on the city provided in the state.
        - If 'city' is provided, it triggers the weather analysis task and returns the result.
        """
        
        if state["city"]:
            weatherAgent = WeatherAgents.WeatherAgent()
            weatherTask = WeatherTasks.WeatherAnalaysisTask(weatherAgent, state["city"])
            result = weatherTask.execute_sync()
            messages = state["messages"]
            messages.append(result)
            return {"messages": messages}

    def replyNode(self, state):
        """
        replyNode:
        - This node invokes the language model with the user's query and appends the response to the messages.
        """
        query = state["query"]
        agent = llm.invoke(f"""
            {query}
        """)
        messages = state["messages"]
        messages.append(agent.content)
        return {"messages": messages}
    
    def entryNode(self, state):
        """
        entryNode:
        - This is the first node to process the user's query.
        - Categorizes the query into different predefined categories (e.g., stock analysis, search, weather).
        - Returns a categorized response in a JSON format.
        """
        input_query = state["query"]
        agent = llm.invoke(f"""
        User input
        ---
        {input_query}
       You have given one user input and you have to perform actions on it based on given instructions

        Categorize the user input in below categories
        stock_analysis: if the user wants a stock market analysis for a specific stock
        stock_news: If user wants to know what in the news about a specific stock
        stock_comparison: If user wants a comparative analysis of more than one stock
        city_weather: If user wants asking something related to the weather of a city
        other: If it is any other query

        After categorizing your final RESPONSE must be in json format , only json with no additions before or after, with these properties:
        category: category of user input
        stock: If category is 'stock_analysis' then give the stock ticker symbol of the company or stock mentioned here else keep it blank, give only the stock ticker.
        news: If category is 'stock_news' then give the stock ticker symbol of the company or stock mentioned here else keep it blank, give only the stock ticker.
        stock_list: If category is 'stock_comparison' then give a list of stock tickers to analyse else keep it blank, give only the list of stock tickers.
        city: If category is 'city_weather' then the name of the city or keep it blank, give only the name of the city.
        query: If category is 'other' then add the user's query here else keep it blank
        Remember the output should be just the json format with properties inside without any specification before or after.
        """)
        print("this the agent response ##################", agent)
        response = json.loads(agent.content)
        return {'stock': response["stock"], 'news': response['news'], 'city': response['city'], 'stock_list': response['stock_list'],'query': response['query'], 'category': response['category']}
