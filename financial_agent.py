from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv
load_dotenv()
Groq.api_key = os.getenv("GROQ_API_KEY")

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

multi_ai_agent = Agent(
team = [web_search_agent,financial_agent],
model = Groq(id="llama-3.3-70b-versatile"),
instructions=["Always include Sources","Use Tables to display the data"],
show_tool_calls=True,
markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)

