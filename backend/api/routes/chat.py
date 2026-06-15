from fastapi import APIRouter

from backend.api.schemas.chat import (
    ChatRequest,
    ChatResponse,
    SourceResponse
)

from backend.dependencies import (
    pipeline,
    conversation_manager
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post(
    "",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    chat_history = (
        conversation_manager
        .get_recent_messages(
            request.conversation_id
        )
    )

    response = (
        pipeline.ask(
            document_id=request.document_id,
            question=request.question,
            chat_history=chat_history
        )
    )

    conversation_manager.add_message(
        request.conversation_id,
        "user",
        request.question
    )

    conversation_manager.add_message(
        request.conversation_id,
        "assistant",
        response.answer
    )

    sources = []

    for source in response.sources:

        sources.append(
            SourceResponse(
                chunk_id=str(source.chunk_id),
                page=source.page,
                snippet=source.text[:300],
                distance=source.distance
            )
        )

    return ChatResponse(
        answer=response.answer,
        sources=sources
    )