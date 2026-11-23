from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

documents = [
    "Solar panels generate electricity by absorbing sunlight using photovoltaic cells.",
    "A shot of espresso tastes sour if extracted too fast and bitter if overcooked.",
    "Creatures in deep ocean zones live under immense water pressure and complete darkness.",
]

query = "How to make a balanced cup of coffee?"


doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0] # values of cosine_similarity should always in 2d
doc_index, score = sorted(list(enumerate(scores)), key=lambda x : x[1])[-1]

print(query)
print(f"{doc_index}. {documents[doc_index]}")