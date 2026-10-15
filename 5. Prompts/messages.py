from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is RAG?")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content[0]['text'].strip()))

print(messages)