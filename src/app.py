# This script is the core of a multi-agent conversational system using Chainlit for message handling
# and LangChain for workflow orchestration. The system is designed to route user queries to different
# nodes based on the type of request (e.g., stock data, weather information, or search queries).
#
# The key components of the refactored code are:
# 
# 1. **Workflow Setup (`create_workflow` function)**: Assembles the state graph and adds nodes that correspond to specific query types.
# 2. **Message Streaming**: Allows for real-time streaming of responses to users.
# 3. **Modular Design**: Functions are separated to handle specific tasks, improving maintainability and extensibility.


from nodes.nodes import Nodes
from messages.state import AgentState
from orchestrator.task_orchestrator import Orchestrator
from langgraph.graph import END, StateGraph
import chainlit as cl
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from typing import cast

# Suppress SSL warnings (optional)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Fetch data with SSL verification disabled
session = requests.Session()
session.verify = False

# Define the workflow function
def create_workflow():
    """
    Assembles the workflow and returns a compiled StateGraph app.
    """
    workflow = StateGraph(AgentState)
    node = Nodes()
    workflow.add_node('entryNode', node.entryNode)
    workflow.add_node('StockNode', node.StockNode)
    workflow.add_node('SearchNode', node.SearchNode)
    workflow.add_node('WeatherNode', node.WeatherNode)
    workflow.add_node("responder", node.replyNode)

    workflow.add_conditional_edges('entryNode', Orchestrator.route_query, {
        "stock": "StockNode",
        "search": "SearchNode",
        "city": "WeatherNode"
    })
    workflow.add_edge("StockNode", END)
    workflow.add_edge("WeatherNode", END)
    workflow.add_edge("SearchNode", END)
    workflow.add_edge("responder", END)

    workflow.set_entry_point("entryNode")
    return workflow.compile()

# Instantiate the compiled workflow app
app = create_workflow()

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="""👋 **Welcome** 🤖

🚀 **What Can I Do?**

I'm here to assist you with a variety of tasks using the power of CrewAI's Agentic Framework. Here's what I can help you with:

1. 📈 **Stock Market Analysis**:
   - **Stock Evolution**: Get detailed analysis of stock price changes for specific companies.
     - Example: "How is Tesla stock evolving?"
   - **Compare Stock Performances**: Compare the stock performances of one or more companies.
     - Example: "Compare the stock performance of Apple and Microsoft."
   - **Latest News and Market Impact**: Retrieve the latest news and analyze its impact on the financial market for specific companies.
     - Example: "What's the latest news about Amazon?"

2. 🌦️ **Weather Forecast**:
   - Get real-time weather information and forecasts for any city.
     - Example: "What's the weather like in Paris?"

3. 🔍 **Web Searches**:
   - Conduct web searches to find the latest information on any topic.
     - Example: "what is a large language model?.""").send()

@cl.on_message
async def on_message(message):
    try:
        # Get the user input
        user_query = message.content
        inputs = {"query": user_query, "messages": [user_query]}
        # Create a new message object for streaming
        msg = cl.Message(content="Agent response ...\n")
        await msg.send()

        # Simulate streaming output
        result = app.invoke(inputs)  # This assumes `app.invoke` provides final output at once
        agent_response = result['messages'][-1]  # Assuming 'messages' contains the response chain
         # Ensure the response is a string
        if not isinstance(agent_response, str):
            agent_response = str(agent_response)
        
        # Stream response character by character
        streamed_text = ""
        for char in agent_response:
            streamed_text += char
            await msg.stream_token(char)  # Stream one token at a time

        # Finalize the streamed message
        await msg.send()
    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()

# Start the Chainlit app
if __name__ == "__main__":
    cl.run(debug=True)
