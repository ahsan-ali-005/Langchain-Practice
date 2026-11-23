from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import EmbeddingsFilter



embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", 
    output_dimensionality=300
)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0)

docs = [
    Document(page_content="Python supports concurrency using asyncio and async/await."),
    Document(page_content="FastAPI supports asynchronous endpoints for handling concurrent requests."),
    Document(page_content="Python lists store ordered collections of items.")
]


vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="multiquery_demo"
)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    base_compressor=EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.7)
)

query = "How does Python handle concurrent requests?"

compressed_docs = compression_retriever.invoke(query)

print("\n--- Contextually Filtered Documents ---")
for i, doc in enumerate(compressed_docs, 1):
    print(f"\nDocument {i}:\n{doc.page_content}")


"""
Removes Irrelevant Information: Filters out information that is not relevant to the user's query.
Reduces Context Size: Passes only useful content to the LLM, reducing unnecessary tokens.
Improves Answer Quality: Helps the LLM focus on the most relevant information within a document.

1. User's Query
       ↓
2. Base Retriever Searches Vector Database
       ↓
3. Retrieve Relevant Documents
       ↓
4. Compressor Filters / Extracts Relevant Content
       ↓
5. Return Compressed Documents
       ↓
6. LLM Generates Answer Using Relevant Context

"""