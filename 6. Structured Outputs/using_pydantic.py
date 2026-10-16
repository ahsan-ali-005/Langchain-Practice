# use pydantic if needs data validation, type coercion etc
from pydantic import BaseModel, Field
from typing import Annotated
from langchain_google_genai import ChatGoogleGenerativeAI


class Review(BaseModel):

    summary : Annotated[str, Field(description="Brief Summary of the Review.")]
    sentiment: Annotated[str, Field(description="Sentiment of the Review.")]

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""I ordered this book expecting a compelling read, but the pacing was agonizingly slow and the characters felt completely flat. The physical quality was equally disappointing, arriving with a damaged cover and bent pages straight out of the box. Save your money and time—this was a complete letdown from start to finish.""")

print(response)