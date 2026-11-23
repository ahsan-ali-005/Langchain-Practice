from langchain_community.document_loaders import WebBaseLoader

url = "https://en.wikipedia.org/wiki/Machine_learning"

loader = WebBaseLoader(url)

content = loader.load()

print(content)