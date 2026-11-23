from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from typing import Literal
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative", "Neutral"]

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

str_parser = StrOutputParser()

feed_back_parser = PydanticOutputParser(pydantic_object=Feedback)

feedback = "The smartphone cover is very ugly. I don't recommend it."

prompt1 = PromptTemplate(
    template="Give the Sentiment from either positive, negative or neutral on the given feedback: {feedback}\n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction" : feed_back_parser.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Generate a oneline appropriate response to this positive feedback: {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Generate a oneline appropriate response to this negative feedback: {feedback}",
    input_variables=["feedback"],
)

sentiment_chain = prompt1 | model | feed_back_parser

conditinal_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive" or "positive", prompt2 | model | str_parser),
    (lambda x: x.sentiment == "Negative" or "negative", prompt3 | model | str_parser),
    RunnableLambda(lambda x: "can't able to find sentiment..") # converting to chain its a default chain
)

chain = sentiment_chain | conditinal_chain

result = chain.invoke({"feedback": feedback})
print(result)