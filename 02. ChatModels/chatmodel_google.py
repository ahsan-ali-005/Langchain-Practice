from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.2)

response = llm.invoke("What is RAG?")

print(response.content[0]["text"].strip())