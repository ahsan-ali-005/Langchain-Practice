# RnnableLambda creates a python function runnable, allow python function to run in AI Pipeline.
from langchain_core.runnables import RunnableLambda


def clean_feedback(text: str) -> str:
    print("--> Custom Python function: clean_feedback chala")
    return text.strip().lower()

def format_result(data: dict) -> str:
    print("--> Custom Python function: format_result chala")
    return f"Processed Sentiment: {data['sentiment'].upper()} | Text: {data['text']}"

clean_step = RunnableLambda(clean_feedback)
format_step = RunnableLambda(format_result)

def add_dummy_sentiment(text: str) -> dict:
    return {"text": text, "sentiment": "negative"}

analysis_step = RunnableLambda(add_dummy_sentiment)

chain = clean_step | analysis_step | format_step

raw_feedback = "   The smartphone cover is very ugly.   "
result = chain.invoke(raw_feedback)

print("\nFinal Output:")
print(result)