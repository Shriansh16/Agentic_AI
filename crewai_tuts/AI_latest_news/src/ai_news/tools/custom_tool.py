"""This code defines a custom tool using crewai.tools.BaseTool, which is intended to be used by an AI agent in CrewAI."""
from crewai.tools import BaseTool  #The base class for defining custom tools in CrewAI.
from typing import Type   #Used to specify that args_schema is a type of BaseModel.
from pydantic import BaseModel, Field  #Used to define structured input data.


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    """This class defines the expected input format for the tool:

Inherits from BaseModel, ensuring that inputs are properly validated.
Has a single field, argument, which:
Is a string (str).
Uses Field(..., description="Description of the argument.") to enforce validation (... means it is required).
Provides a description, which helps the AI agent understand what the argument is for."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    """This class defines the actual tool:

Inherits from BaseTool, making it a usable tool in CrewAI.
Defines metadata:
name: The name of the tool.
description: A clear explanation of what the tool does (useful for AI agents).
args_schema: Specifies that the tool requires an input in the format of MyCustomToolInput."""
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        """_run(self, argument: str) -> str:

This method executes the tool when called.
It takes argument (a string) as an input.
It returns a string as output.
Placeholder Implementation:

Right now, it just returns a hardcoded string:
"this is an example of a tool output, ignore it and move along."
In a real-world scenario, this function would perform some useful task based on argument."""
        return "this is an example of a tool output, ignore it and move along."
