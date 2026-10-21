from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
Building scalable and accurate AI applications relies heavily on the quality of the underlying data pipeline. Mastering document loading, metadata management, and text splitting forms the essential foundation for creating robust knowledge retrieval systems, semantic search engines, and enterprise-grade AI assistants.

Building scalable and accurate AI applications relies heavily on the quality of the underlying data pipeline. Mastering document loading, metadata management, and text splitting forms the essential foundation for creating robust knowledge retrieval systems, semantic search engines, and enterprise-grade AI assistants.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
)

chunks = splitter.split_text(text=text)

print(len(chunks))