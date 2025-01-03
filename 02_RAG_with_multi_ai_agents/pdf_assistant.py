import typer
from typing import Optional,List
from phi.assistant import Assistant        #it will assist us in different tasks
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2