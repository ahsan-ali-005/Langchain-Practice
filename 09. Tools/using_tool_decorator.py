from langchain.tools import tool

@tool
def Multiply(a: int, b: int) -> int:
    """Multiply Two Numbers"""
    return a * b


result = Multiply.invoke({"a": 2, "b": 4})
print(result)