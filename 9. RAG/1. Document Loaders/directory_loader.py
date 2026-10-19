from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path="PDFs", glob="*.pdf", loader_cls=PyPDFLoader)

# pdfs = loader.load() # slow as it opens all the files at once in the memory.
pdf =  loader.lazy_load() # fast-> returns generator of documents. You can load one document at a time
for doc in pdf:
    print(doc.page_content)
    print("-" * 50)
