# Maximum Marginal Relevance Retriever:-
# How can we pick results that are not only relevant to the query but also different from each other.(MRR Core Philosophy-> gives diverse perspective )

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

retriever = vector_store.as_retriever(search_type="mmr" ,search_kwargs={"k": 2, "lambda_mult":0},)

result = retriever.invoke(query)
print(result)

# lambda_mult -> 1: Works like same as similarity search
# lambda_mult -> 0: Gives fully diverse Perstectives so keep it between 0 and 1