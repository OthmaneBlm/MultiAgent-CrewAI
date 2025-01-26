# 🛠️ Hands-On Project: Multi-Agent Applications with CrewAI  

## 🚀 Overview  

This project is a **hands-on guide** to creating **multi-agent applications** using **CrewAI’s Agentic Framework**. It demonstrates how to build a system where agents can:  
- Perform **stock market analysis** using Yahoo Finance.  
- Retrieve **real-time weather data** using WeatherAPI.  
- Conduct **web searches** with Serper API.  

The project focuses on **demystifying the creation of multi-agent applications**, showcasing how agents can **execute several tasks** by reusing multiple tools and APIs.  

## 🤔 Why Choose CrewAI?

CrewAI transforms the way we think about multi-agent systems by enabling AI agents to work collaboratively, just like a skilled human team. Whether solving complex problems or handling diverse tasks, CrewAI's architecture provides a flexible and efficient framework for building powerful AI applications. Here's why it's a game-changer:

### **Key Components of CrewAI 🧩**

1. **Agents 🤖**  
   - Specialized virtual team members with distinct roles and expertise.  
   - Autonomous decision-makers capable of handling tasks within their domain.  
   - Examples include Researchers, Analysts, Writers, and Coders.  
   - Customizable with specific language models, APIs, or knowledge bases to enhance performance.

2. **Tasks 📋**  
   - Clearly defined units of work with specific goals, constraints, and success criteria.  
   - Tasks can be executed sequentially, in parallel, or as interdependent modules.  
   - Complex problems are broken into manageable subtasks, promoting efficiency and clarity.

3. **Crews 👥**  
   - Teams of agents dynamically assembled to achieve a common goal or tackle a project.  
   - A centralized coordination system oversees task distribution and progress.  
   - Crews enable seamless collaboration, information sharing, and dynamic adaptability to task demands.

---

### **How It All Works: The CrewAI Symphony 🎼**

Think of CrewAI as an orchestra, where every agent plays a vital role, contributing to a harmonious performance. Here’s how it orchestrates tasks:

- **Autonomous Collaboration**: Agents work together, sharing knowledge and complementing each other’s strengths.  
- **Flexibility in Execution**: Tasks can flow sequentially, like a relay race, or operate in parallel for faster results.  
- **Dynamic Problem Solving**: Crews are formed on-demand, ensuring the right agents are available for the job.

This structured yet flexible approach makes CrewAI ideal for handling **diverse, complex challenges** while maintaining efficiency and scalability.


---

## 🛠️ Project Setup  

### 1. Clone the Repository  

```bash  
git clone <repository_url>  
cd <project_directory>  
```  

### 2. Set Up the Conda Environment  

Use the provided `env.yaml` file to set up the environment:  

```bash  
conda env create -f env.yaml  
```  

Activate the environment:  

```bash  
conda activate <env_name>  
```  

### 3. Configure API Keys  

Add your API keys to a `.env` file inside the `src` directory. Example:  

```plaintext  
POLYGONE_API_KEY="your_polygon_api_key"  
SERPER_SEARCH_API="your_serper_search_api_key"  
WEATHER_API_KEY="your_weather_api_key"  
TAVILY_API_KEY="your_tavily_api_key"  
AZURE_OPENAI_API_VERSION="your_azure_openai_version"  
AZURE_OPENAI_API_KEY="your_azure_openai_key"  
AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"  
AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name"  
FRED_API_KEY="your_fred_api_key"  
```  

### 4. Start the Application  

Run the app using Chainlit:  

```bash  
chainlit run app.py  
```  

### 5. Interact with the App  

Once launched, use the conversational interface to ask questions. Examples:  
- "What is the stock price of Tesla?"  
- "What’s the weather in Paris?"  
- "Search for the latest advancements in AI."  

---

## 🧩 Project Architecture  

This project leverages **CrewAI’s modular architecture**, structured as follows:  

### 📂 Directory Structure  

- **`agents/`**: Defines agents capable of executing specific tasks, such as stock analysis, weather queries, and web searches. Each agent uses CrewAI to structure and manage tasks effectively.  
- **`tools/`**: Contains reusable tools and API integrations for services like Yahoo Finance, WeatherAPI, and Serper. These tools can be shared across multiple agents.  
- **`orchestrator/`**: Manages task routing by analyzing user input and directing it to the appropriate agent.  
- **`app.py`**: The main entry point for running the application, integrating Chainlit for real-time conversational responses.  
- **`.env`**: Stores API keys and other environment-specific variables.  
- **`env.yaml`**: Specifies all dependencies for setting up the environment.  

### 🧠 Key Features of CrewAI in This Project  

1. **Agent Modularity**:  
   - Each agent is dedicated to either a specific or multiple tasks, ensuring clear separation of concerns.  
   - Example: The `StockNode` handles stock-related queries, while the `WeatherNode` processes weather requests.  

2. **Reusable Tools**:  
   - Tools for interacting with APIs are designed for **reuse** across agents.  
   - Example: The `Yahoo Finance Tool` can be used by multiple agents requiring financial data.  

3. **Dynamic Task Routing**:  
   - The **Orchestrator** uses CrewAI to determine which agent should handle a user query, ensuring efficient execution.  

4. **Real-Time Streaming**:  
   - Chainlit enables interactive conversations by streaming responses as agents complete their tasks.  

---

## 🌟 Example Use Cases  

This project demonstrates how **multi-agent systems** can be applied to solve real-world problems:  

- **Financial Market Analysis**: Retrieve stock prices and analyze trends using Yahoo Finance and Polygone.io.
- **Weather Updates**: Provide real-time weather information for any city.  
- **General Queries**: Perform web searches to answer diverse questions.  

### Query Examples  

1. **Stock Analysis**:  
   - Input: *"What’s the current price of Apple stock?"*  
   - Agent: StockNode → Uses Yahoo Finance Tool → Returns stock data with a brief analysis.  
   - Input: *"What’s in the news about Apple today?"*  
   - Agent: StockNode → Uses Polygone Tool → Returns a list of major news linked to apple with a brief analyses of the market implications.

2. **Weather Information**:  
   - Input: *"What’s the weather in Dubai?"*  
   - Agent: WeatherNode → Uses WeatherAPI Tool → Returns weather forecast.  

3. **Web Search**:  
   - Input: *"Find the latest advancements in machine learning."*  
   - Agent: SearchNode → Uses Serper Tool → Returns search results.  

---

## 🔑 Key Dependencies  

The project relies on the following libraries:  

- **`crewai`**: The foundation of the multi-agent framework.  
- **`langchain`**: For creating chains and integrating language models.  
- **`chainlit`**: Provides a conversational interface for user interaction.  
- **`requests`**: Used to interact with APIs.  
- **`yfinance`**: For fetching financial data.  
- **`pandas`**: Data manipulation and analysis.  
- **`ratelimit`**: To manage API rate limits.  
