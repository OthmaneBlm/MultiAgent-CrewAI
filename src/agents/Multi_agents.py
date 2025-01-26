# Agents Subfolder Refactor
# ==========================
# Purpose: This folder contains the definitions of various agents used in the multi-agent system.
# Each agent has a specific role, backstory, and set of tools to perform specific tasks.
# The agents leverage Azure OpenAI for processing and use external tools for task execution.

# Common Setup for All Agents
# ---------------------------
# The following setup is shared across all agents to avoid redundancy and ensure consistency.

import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from langchain_openai import AzureChatOpenAI

# Load environment variables
load_dotenv('.env')

# Extract Azure OpenAI credentials
AZURE_OPENAI_API_VERSION = os.environ['AZURE_OPENAI_API_VERSION']
AZURE_OPENAI_API_KEY = os.environ['AZURE_OPENAI_API_KEY']
AZURE_OPENAI_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ['AZURE_OPENAI_DEPLOYMENT_NAME']

# Set environment variables for Azure OpenAI
os.environ['AZURE_API_KEY'] = AZURE_OPENAI_API_KEY
os.environ['AZURE_API_BASE'] = AZURE_OPENAI_ENDPOINT
os.environ['AZURE_API_VERSION'] = AZURE_OPENAI_API_VERSION

# Initialize the AzureChatOpenAI instance
llm = AzureChatOpenAI(azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME, 
                      api_version=AZURE_OPENAI_API_VERSION)

# Agent Definitions
# ------------------

class StockAgents:
    """
    A collection of agent classes, each with specific roles and tools to perform their tasks.
    """

    @staticmethod
    def StockAgent():
        """
        Stock analysis agent to analyze real-time stock data, news, or comparisons.
        """
        from tools.YahooFinance_tool import YHTools
        from tools.Polygone_tool import Tools

        return Agent(
            role="StockAgent",
            backstory=(
                """You are an expert stock analyst. Your task is to analyze real-time stock data, 
                news, or compare stocks and give a summary. Consider any available stock information. 
                Provide a concise summary with a small elaboration."""
            ),
            goal=(
                """You are an expert stock analyst. Your task is to analyze the provided stock insights 
                and give a concise summary."""
            ),
            tools=[
                YHTools.get_yahoo_finance_data,
                Tools.get_polygon_news,
                YHTools.get_yahoo_finance_data_comparison
            ],
            verbose=True,
            allow_delegation=False,
            llm=LLM(model=f'azure/{AZURE_OPENAI_DEPLOYMENT_NAME}')
        )

class SearchAgents:
    """
    A search assistant agent that compiles web search results into a concise output.
    """

    @staticmethod
    def SearchAgent():
        from tools.SerperSearch_tool import SerperTools

        return Agent(
            role="SearchAgent",
            backstory=(
                """You are a search assistant. Your task is to analyze the results of a web search 
                and compile them into one answer."""
            ),
            goal=(
                """You are a search assistant. Your task is to compile a Google search output for 
                a specific query into one concise answer."""
            ),
            tools=[
                SerperTools.search_query
            ],
            verbose=True,
            allow_delegation=False,
            llm=LLM(model=f'azure/{AZURE_OPENAI_DEPLOYMENT_NAME}')
        )

class WeatherAgents:
    """
    A weather specialist agent to analyze and summarize weather data for specific locations.
    """

    @staticmethod
    def WeatherAgent():
        from tools.Weather_tool import WeatherTools

        return Agent(
            role="WeatherAgent",
            backstory=(
                """You are a weather specialist. Your task is to analyze weather data for a specific 
                location and give a summary."""
            ),
            goal=(
                """You are a weather analyst. Your task is to look into weather data and answer queries."""
            ),
            tools=[
                WeatherTools.get_weather
            ],
            verbose=True,
            allow_delegation=False,
            llm=LLM(model=f'azure/{AZURE_OPENAI_DEPLOYMENT_NAME}')
        )
