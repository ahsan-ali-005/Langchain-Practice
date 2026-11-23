# Using Structured Tool is best when you want data+type validation.
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(..., description="First Argument/Number")
    b: int = Field(..., description="Second Argument/Number")

def multiply_func(a, b):
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply_tool",
    description="Multiply two numbers.",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a": 2, "b": 4})
print(result)