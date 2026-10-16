from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated

# TypedDict provides type hinting but not data validation like pydantic..
class Review(TypedDict):

    # annotated to help model understand better about attributes by that 
    # we don't completely rely on llm that it understands our attributes itself.
    summary: Annotated[str, "A breif summary of the Review."]
    sentiment: Annotated[str, "Give Sentiment either positive, negative or neutral"]


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""I ordered this book expecting a compelling read, but the pacing was agonizingly slow and the characters felt completely flat. The physical quality was equally disappointing, arriving with a damaged cover and bent pages straight out of the box. Save your money and time—this was a complete letdown from start to finish.""")

print(response)