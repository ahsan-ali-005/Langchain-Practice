from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

# 1. Define custom tools using the @tool decorator
@tool
def get_current_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # Mock implementation for demonstration
    if "tokyo" in location.lower():
        data = "The weather in Tokyo is 18°C and cloudy."
    else:
        data = f"The weather in {location} is 22°C and sunny."
    return data

@tool
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given length and width."""
    return length * width

# List of tools available to the model
tools = [get_current_weather, calculate_area]

# 2. Initialize the Gemini model and bind the tools
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# 3. Invoke the model with a query that requires tool use
query = "What is the weather like in Tokyo right now?"
ai_msg = llm_with_tools.invoke(query)

print("--- AI Message Tool Calls ---")
print(ai_msg.tool_calls)

# 4. Execute the requested tool(s) and return the output
# In a full agent loop, LangChain handles this automatically, 
# but manually mapping looks like this:
tool_map = {tool.name: tool for tool in tools}

messages = [query, ai_msg]

for tool_call in ai_msg.tool_calls:
    selected_tool = tool_map[tool_call["name"]]
    # Invoke the tool with the arguments provided by the model
    tool_output = selected_tool.invoke(tool_call["args"])
    print(f"\nTool Output ({tool_call['name']}): {tool_output}")
    
    # Append the tool response message back to chat history if continuing