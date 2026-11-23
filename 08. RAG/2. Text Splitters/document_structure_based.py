from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Hello:
    def __init__(self):
        print("Starting..")
    def hello_world(self):
        print("Hello World")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,
    chunk_overlap=20
)

chunks = splitter.split_text(text=text)

print(len(chunks))
print(chunks)