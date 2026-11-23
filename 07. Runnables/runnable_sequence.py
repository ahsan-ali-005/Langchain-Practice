from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed Report on the topic: {topic}",
    input_variables=["topic"]
)

topic = input("Enter The topic: ")

prompt2 = PromptTemplate(
    template="Give me 5 most important points for this report: {report}",
    input_variables=["report"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

response = chain.invoke({"topic": topic})

print(response)