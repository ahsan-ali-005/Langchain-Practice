from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

documents = [
    "Islamabad is capital of Pakistan.",
    "But, Lahore Lahore hy!",
    "Pr Karachi oska Shohar hy!"
]

result = embedding.embed_documents(documents)

print(str(result))