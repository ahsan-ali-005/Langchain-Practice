from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write simple and to the point notes on the topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give some quiz questions on the topic: {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="Merge both notes and quiz of the topic. notes: {notes} & quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parallel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})

merge_chain = prompt3 | model | parser
chain = parallel_chain | merge_chain

result = chain.invoke({"topic": "Regression in Machine Learning"})
print(result)