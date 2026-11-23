from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Initialize the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

sample_text = """
Artificial intelligence and machine learning are revolutionizing modern technology. Deep learning models, particularly transformers, allow computers to process natural language with incredible accuracy. Data pipelines and vector databases play a vital role in feeding high-quality context to these AI models for semantic search and retrieval systems.

Space exploration has entered a new era with commercial spaceflight and planetary missions. NASA and private aerospace companies are working together to establish human bases on the Moon and eventually send crewed missions to Mars. Advanced propulsion systems and autonomous rovers are critical for gathering sample data from distant planetary surfaces.

Preparing a traditional Italian pasta dish requires mastering simple yet precise cooking techniques. Boiling fresh pasta in well-salted water ensures optimal texture, while emulsifying pasta water with high-quality olive oil or butter creates a silky sauce. Fresh basil, aged Parmigiano-Reggiano, and vine-ripened tomatoes elevate the flavor profile to restaurant quality.
"""

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_amount=1,
    breakpoint_threshold_type="standard_deviation"  # Yahan hyphen ki jagah underscore lagayein
)

chunks = text_splitter.split_text(sample_text)

print(f"Total Chunks Created: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.strip())
    print("\n")