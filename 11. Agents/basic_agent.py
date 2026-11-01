from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return their sum."""
    return a + b


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)


agent = create_agent(
    model=model,
    tools=[add_numbers],
    system_prompt="You are a helpful AI assistant. Use the calculator tool whenever the user asks you to add numbers."
)


response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is 125 + 375? Use your calculator tool."
            }
        ]
    }
)


print(response["messages"][-1].content[0]["text"])