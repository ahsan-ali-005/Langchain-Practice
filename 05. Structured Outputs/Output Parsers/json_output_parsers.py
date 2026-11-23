from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# in JsonOutputParser we cannot enforce schema because we have to tell llm about the names of each attribute it should use inside the prompt
parser = JsonOutputParser()
format_instructions = parser.get_format_instructions()

review_text = "The product arrived late, but the build quality is outstanding!"

prompt = PromptTemplate(
    template="Analyze the following product review and return a JSON object with 'summary' and 'sentiment' keys.\nReview: {review}\n{format_instructions}",
    input_variables=["review"],
    partial_variables={"format_instructions": format_instructions}
)


chain = prompt | model | parser

result = chain.invoke({"review" : review_text})

print(result)