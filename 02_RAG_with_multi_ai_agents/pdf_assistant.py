import typer
from typing import Optional,List
from phi.assistant import Assistant        #it will assist us in different tasks
from phi.storage.assistant.postgres import PgAssistantStorage   #for managing and storing data in a PostgreSQL database
from phi.knowledge.pdf import PDFUrlKnowledgeBase    #for managing and storing data in a PostgreSQL database

from phi.vectordb.pgvector import PgVector2    #for working with vector databases, specifically leveraging the pgvector extension for PostgreSQL. It allows for efficient storage and retrieval of vector embeddings