# Using Base Tool is best for custom complex tools to get full control over everything.
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a : int = Field(..., description="First Argument/Number")
    b : int = Field(..., description="Second Argument/Number")


class MultiplyTool(BaseTool):

    name: str = "multiply"
    description : str = "Multiply two numbers"

    args_schema : Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int):
        return a*b

multiply_tool = MultiplyTool()
result = multiply_tool.invoke({"a": 2, "b": 4})
print(result)