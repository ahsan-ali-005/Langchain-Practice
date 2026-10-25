from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

doc1 = Document(
    page_content="Python is a high-level programming language used in AI, machine learning, and web development.",
    metadata={"category": "Python", "level": "beginner"}
)
doc2 = Document(
    page_content="FastAPI is a modern Python framework used to build fast REST APIs with asynchronous support.",
    metadata={"category": "FastAPI", "level": "intermediate"}
)
doc3 = Document(
    page_content="Vector databases store embeddings and enable semantic similarity search for AI applications.",
    metadata={"category": "Vector Databases", "level": "intermediate"}
)

docs = [doc1, doc2 , doc3]

vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300),
    persist_directory="chroma_db",
    collection_name="sample"
)

# Add Documents
vector_store.add_documents(docs, ids=["1","2","3"])

# Get Documents
print(vector_store.get(include=["embeddings", "metadatas", "documents"]))
print(vector_store.get_by_ids(ids=["1","2"]))
print(vector_store.get(where={"category": "Python"}))

# Search Documents
result = vector_store.similarity_search(
    query="what is fastapi?",
    k = 2 # Number of most similar documents
)

# Search Documents with score
score = vector_store.similarity_search_with_score(
    query="Vector database embeddings",
    k = 2,
    filter={"level": "intermediate"} # filter on the basis of metadata
)


new_document = Document(
    page_content="Python is one of the mostly used Programming Languages in today's world.",
    metadata= {"category": "Python", "level": "beginner"}
)

# Update Document
vector_store.update_document(document_id="1", document=new_document)

# Delete Document
vector_store.delete(ids=["1"])