from langchain.tools import tool

@tool
def Multiply(a: int, b: int) -> int:
    """Multiply Two Numbers"""
    return a * b

@tool
def Add(a: int, b: int) -> int:
    """Addition of Two Numbers"""
    return a + b

# Toolkit is used to group similar tools together to make them reusable
class MathOperationsToolkit:
    def get_tools(self):
        return [Multiply, Add]


toolkit = MathOperationsToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name)