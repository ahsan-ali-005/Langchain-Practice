from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()

review_text = "The product arrived late, but the build quality is outstanding!"

prompt = PromptTemplate(
    template="Analyze the following product review and give a one-sentence overall summary:\n{review}",
    input_variables=["review"]
)

chain = prompt | model | parser

result = chain.invoke({
    "review" : review_text
})

print(result)