from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

query = "What is fastapi?"
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
    collection_name="sample"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

result = retriever.invoke(query)
print(result)

# Why don't use similarity_search function for it:

#1) Retriever is a runnable which means it can be easily added in chain, similarity_search won't
#2) Retriever proives modern searching techniques for retrieval on queries.
#3) Give invoke function for better connection with other components.