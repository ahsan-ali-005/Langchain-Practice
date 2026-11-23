# use jsonschema if you are using multiple languages for you projecct as json is understandable by all
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")


review_schema = {
    "title": "Review",
    "type": "object",  # Batana zaroori hai ke outer structure ek object (dictionary) hai
    "properties": {
        "summary": {
            "type": "string",
            "description": "A brief summary of the review.",
        },
        "sentiment": {
            "type": "string",
            "description": "The sentiment of the review (e.g. positive, negative, neutral).",
        },
    },
    "required": ["summary", "sentiment"],
}

structured_model = model.with_structured_output(review_schema)

response = structured_model.invoke("""I ordered this book expecting a compelling read, but the pacing was agonizingly slow and the characters felt completely flat. The physical quality was equally disappointing, arriving with a damaged cover and bent pages straight out of the box. Save your money and time—this was a complete letdown from start to finish.""")

print(type(response))