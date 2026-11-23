# RunnablePassThrough just returns the input as it is.
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough


def get_word_count(inputs: dict) -> int:
    return len(inputs["feedback"].split())

chain = RunnablePassthrough.assign(
    word_count=RunnableLambda(get_word_count),
    status=RunnableLambda(lambda x: "Processed Successfully")
)

# Input data
input_data = {"feedback": "The smartphone cover is very ugly and bad."}

# Chain ko invoke karna
result = chain.invoke(input_data)
print("Final Output:", result)