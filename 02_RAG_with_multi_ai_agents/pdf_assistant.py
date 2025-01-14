import typer
from typing import Optional,List
from phi.assistant import Assistant        #it will assist us in different tasks
from phi.storage.assistant.postgres import PgAssistantStorage   #for managing and storing data in a PostgreSQL database
from phi.knowledge.pdf import PDFUrlKnowledgeBase    #for managing and storing data in a PostgreSQL database
from phi.vectordb.pgvector import PgVector
from phi.model.groq import Groq    #for working with vector databases, specifically leveraging the pgvector extension for PostgreSQL. It allows for efficient storage and retrieval of vector embeddings
import os
from phi.agent import Agent
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="thai_recipes",
        db_url=db_url
    )
)
knowledge_base.load()

# Create the RAG agent
agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    knowledge=knowledge_base,  # Add the knowledge base to the agent
    show_tool_calls=True,
    markdown=True,
)

# Query the agent
agent.print_response("How do I make 'Khao Niew Dam Piek Maphrao Awn' ", stream=True)