from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

documents = [
    "Islamabad is capital of Pakistan.",
    "But, Lahore Lahore hy!",
    "Pr Karachi oska Shohar hy!"
]

result = embedding.embed_documents(documents)

print(str(result))