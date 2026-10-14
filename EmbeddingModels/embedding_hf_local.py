from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

result = embedding.embed_query("Islamabad is capital of Pakistan.")

print(str(result))