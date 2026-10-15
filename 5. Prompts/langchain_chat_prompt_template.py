# ChatPromptTemplate used for dynamic prompts in list of messages(for Multi-turn conversation)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful {domain} expert."),
        ('human', "Explain in simple terms: {topic}.")
    ]
)

prompt = chat_template.invoke({'domain': "tech", "topic": "RAG"})
print(prompt)