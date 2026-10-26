import logging
from langchain_chroma import Chroma
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Enable logging to see the generated sub-queries in the terminal
logging.basicConfig()
logging.getLogger("langchain_community.retrievers.multi_query").setLevel(logging.INFO)


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", 
    output_dimensionality=300
)


docs = [
    Document(page_content="FastAPI is a modern Python web framework built on Starlette and Pydantic for high performance."),
    Document(page_content="Python is widely used in artificial intelligence, backend development, and data automation."),
    Document(page_content="Asynchronous programming in Python allows handling thousands of concurrent requests without blocking execution."),
    Document(page_content="Vector databases like Chroma store high-dimensional embeddings to enable fast semantic retrieval."),
]

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="multiquery_demo"
)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0)

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    llm=llm
)

query = "How to build async APIs in Python?"
retrieved_docs = retriever.invoke(query)

print("\n--- Final Unique Documents Retrieved ---")
for i, doc in enumerate(retrieved_docs, 1):
    print(f"\nDocument {i}:\n{doc.page_content}")



"""
Improves Recall: Retrieves relevant documents using multiple variations of the original query.
Handles Different Wording: Finds relevant information even when documents use different words to express the same concept.
Reduces Missing Information: Combines results from multiple queries and removes duplicate documents.

1. User's Original Query
          ↓
2. LLM Generates Multiple Query Variations
          ↓
3. Each Query Searches the Vector Database
          ↓
4. Combine Retrieved Documents
          ↓
5. Remove Duplicate Documents
          ↓
6. Return Unique Relevant Documents 

"""