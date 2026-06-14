from fastapi import FastAPI
from fastapi import FastAPI

from backend.api.routes.documents import (
    router as document_router
)
from backend.api.routes.chat import (
    router as chat_router
)
from backend.api.routes.conversations import (
    router as conversation_router
)


app = FastAPI(
    title="RAG Knowledge Assistant",
    version="1.0.0",
    description="Resume-ready RAG application built with FastAPI, FAISS and Groq"
)

app.include_router(
    document_router
)

app.include_router(
    chat_router
)

app.include_router(
    conversation_router
)


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }