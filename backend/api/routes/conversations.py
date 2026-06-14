from fastapi import APIRouter
from fastapi import HTTPException

from backend.dependencies import (
    conversation_manager
)

from backend.api.schemas.conversation import (
    CreateConversationRequest,
    CreateConversationResponse,
    ConversationResponse,
    ConversationListResponse,
    ConversationDetailResponse,
    MessageResponse
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)

@router.post(
    "",
    response_model=CreateConversationResponse
)
def create_conversation(
    request: CreateConversationRequest
):

    conversation = (
        conversation_manager
        .create_conversation(
            request.document_id
        )
    )

    return CreateConversationResponse(
        conversation_id=conversation[
            "conversation_id"
        ],
        document_id=conversation[
            "document_id"
        ]
    )

@router.get(
    "/document/{document_id}",
    response_model=ConversationListResponse
)
def get_document_conversations(
    document_id: str
):

    conversations = (
        conversation_manager
        .get_conversations_by_document(
            document_id
        )
    )

    response = []

    for conversation in conversations:

        response.append(
            ConversationResponse(
                conversation_id=conversation[
                    "conversation_id"
                ],
                document_id=conversation[
                    "document_id"
                ],
                created_at=conversation[
                    "created_at"
                ]
            )
        )

    return ConversationListResponse(
        conversations=response
    )

@router.get(
    "/{conversation_id}",
    response_model=ConversationDetailResponse
)
def get_conversation(
    conversation_id: str
):

    conversation = (
        conversation_manager
        .get_conversation(
            conversation_id
        )
    )

    if conversation is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )
    
    messages = []

    for message in conversation[
        "messages"
    ]:

        messages.append(
            MessageResponse(
                role=message["role"],
                content=message["content"]
            )
        )

    return (
        ConversationDetailResponse(
            conversation_id=conversation[
                "conversation_id"
            ],
            document_id=conversation[
                "document_id"
            ],
            created_at=conversation[
                "created_at"
            ],
            messages=messages
        )
    )