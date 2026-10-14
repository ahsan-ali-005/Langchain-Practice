from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.5, max_tokens=10) #llm model old

result = model.invoke("What is the capital of Pakistan?")

print(result)
