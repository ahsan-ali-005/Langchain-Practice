from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="my_dataset.csv")

docs = loader.load()

print(docs[0].page_content)