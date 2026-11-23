from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, max_completion_tokens=150)

response = llm.invoke("What is meant by RAG?")

print(response.content)