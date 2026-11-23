# not loading all wikipedia articles searching for a specific so that's why its a retriever not a document loader
import wikipedia
from langchain_community.retrievers import WikipediaRetriever

# Set a custom user-agent to comply with Wikimedia's API policy
wikipedia.set_user_agent("LangChainPracticeApp/1.0 (mr.ahsanali4554@gmail.com)")

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "What is Machine Learning?"

docs = retriever.invoke(query)

print(docs)