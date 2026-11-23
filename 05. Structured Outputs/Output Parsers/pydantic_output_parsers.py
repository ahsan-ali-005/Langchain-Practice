from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Annotated

class Review(BaseModel):
    summary : Annotated[str, Field(description="Brief Summary of the Review.")]
    sentiment: Annotated[str, Field(description="Sentiment of the Review.")]


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# In PydanticOutputParser both schema and data validation can be Enforced. So, its always best.
parser = PydanticOutputParser(pydantic_object=Review)

format_instructions = parser.get_format_instructions()

review_text = "The product arrived late, but the build quality is outstanding!"

# i don't evne have to tell attributes names in prompt explicitly in case of PydanticOutputParser
prompt = PromptTemplate(
    template="Analyze the following product review.\nReview: {review}\n{format_instructions}",
    input_variables=["review"],
    partial_variables={"format_instructions": format_instructions}
)

chain = prompt | model | parser

result = chain.invoke({"review" : review_text})

print(result)