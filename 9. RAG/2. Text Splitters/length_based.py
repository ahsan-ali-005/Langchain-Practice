from langchain_text_splitters import CharacterTextSplitter


text = """
Building scalable and accurate AI applications relies heavily on the quality of the underlying data pipeline. Mastering document loading, metadata management, and text splitting forms the essential foundation for creating robust knowledge retrieval systems, semantic search engines, and enterprise-grade AI assistants.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10, #for passing context of previouse chunk to next chunk
    separator=""
    
)

docs = splitter.split_text(text=text)

print(docs)