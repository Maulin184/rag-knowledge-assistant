from pydantic import BaseModel


class ChatRequest(
    BaseModel
):
    conversation_id: str
    document_id: str
    question: str


class SourceResponse(
    BaseModel
):
    chunk_id: str
    page: int
    snippet:str
    distance: float


class ChatResponse(
    BaseModel
):
    answer: str
    sources: list[SourceResponse]