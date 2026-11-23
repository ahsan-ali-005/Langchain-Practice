from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("PDFs/The Prompt Ladder.pdf")

pdf = loader.load()

print(pdf)
