import os
from dotenv import load_dotenv

from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager
from backend.core.embeddings import EmbeddingManager
from backend.core.vector_store import VectorStoreManager

from backend.services.document_manager import DocumentManager
from backend.services.retrieval_service import RetrievalService
from backend.services.llm_service import LLMService
from backend.services.rag_pipeline import RAGPipeline
from backend.services.conversation_manager import (
    ConversationManager
)

document_manager = DocumentManager()

loader = DocumentLoader()

chunker = ChunkingManager()

embedder = EmbeddingManager()

vector_store = VectorStoreManager()

retrieval_service = RetrievalService(
    embedder=embedder,
    vector_store=vector_store
)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found in .env"
    )

llm_service = LLMService(api_key=api_key)

conversation_manager = ConversationManager()

pipeline = RAGPipeline(
    document_manager=document_manager,
    loader=loader,
    chunker=chunker,
    embedder=embedder,
    vector_store=vector_store,
    retrieval_service=retrieval_service,
    llm_service=llm_service
)