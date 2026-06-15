from pydantic import BaseModel
from typing import List


class CreateConversationRequest(
    BaseModel
):
    document_id: str


class CreateConversationResponse(
    BaseModel
):
    conversation_id: str
    document_id: str


class ConversationResponse(
    BaseModel
):
    conversation_id: str
    document_id: str
    title: str
    created_at: str


class ConversationListResponse(
    BaseModel
):
    conversations: List[
        ConversationResponse
    ]


class MessageResponse(
    BaseModel
):
    role: str
    content: str


class ConversationDetailResponse(
    BaseModel
):
    conversation_id: str
    document_id: str
    created_at: str
    messages: List[
        MessageResponse
    ]