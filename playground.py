from phi.agent import Agent
import phi.api
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os
import phi
from phi.playground import Playground,serve_playground_app
# Load environment variables from .env file
load_dotenv()
Groq.api_key = os.getenv("GROQ_API_KEY")

phi.api = os.getenv("PHI_API_KEY")

##  Web Search Agent
web_search_agent = Agent(
    name= "Web Search Agent",
    role= "Search the web for information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions=["Always include Sources"],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent
financial_agent = Agent(
    name= "Financial AI Agent",
    role= "Search the web for information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,stock_fundamentals=True,analyst_recommendations=True,company_news=True)],
    instructions=["Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app= Playground(agents= [web_search_agent,financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)

