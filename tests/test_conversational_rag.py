import os

from dotenv import load_dotenv

from backend.core.document_loader import (
    DocumentLoader
)

from backend.core.chunking import (
    ChunkingManager
)

from backend.core.embeddings import (
    EmbeddingManager
)

from backend.core.vector_store import (
    VectorStoreManager
)

from backend.services.document_manager import (
    DocumentManager
)

from backend.services.conversation_manager import (
    ConversationManager
)

from backend.services.retrieval_service import (
    RetrievalService
)

from backend.services.llm_service import (
    LLMService
)

from backend.services.rag_pipeline import (
    RAGPipeline
)


def main():

    load_dotenv()

    print(
        "\nInitializing Components...\n"
    )

    document_manager = (
        DocumentManager()
    )

    conversation_manager = (
        ConversationManager()
    )

    loader = (
        DocumentLoader()
    )

    chunker = (
        ChunkingManager()
    )

    embedder = (
        EmbeddingManager()
    )

    vector_store = (
        VectorStoreManager()
    )

    retrieval_service = (
        RetrievalService(
            embedder=embedder,
            vector_store=vector_store
        )
    )

    llm_service = (
        LLMService(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )
    )

    pipeline = (
        RAGPipeline(
            document_manager=document_manager,
            loader=loader,
            chunker=chunker,
            embedder=embedder,
            vector_store=vector_store,
            retrieval_service=retrieval_service,
            llm_service=llm_service
        )
    )

    print(
        "\nCreating Conversation...\n"
    )

    conversation = (
        conversation_manager
        .create_conversation(
            document_id="doc_001"
        )
    )

    conversation_id = (
        conversation[
            "conversation_id"
        ]
    )

    print(
        f"Conversation ID: "
        f"{conversation_id}"
    )

    print(
        "\nAdding Previous Messages...\n"
    )

    conversation_manager.add_message(
        conversation_id,
        "user",
        "What is attention?"
    )

    conversation_manager.add_message(
        conversation_id,
        "assistant",
        (
            "Attention is a mechanism "
            "that allows a model to "
            "focus on important parts "
            "of the input."
        )
    )

    chat_history = (
        conversation_manager
        .get_recent_messages(
            conversation_id
        )
    )

    print(
        "\nChat History:\n"
    )

    for message in chat_history:

        print(
            f"{message['role']}: "
            f"{message['content']}"
        )

    print(
        "\nAsking Follow-up Question...\n"
    )

    response = (
        pipeline.ask(
            document_id="doc_001",
            question=(
                "Can you give me an example?"
            ),
            chat_history=chat_history
        )
    )

    print(
        "\nAnswer:\n"
    )

    print(
        response.answer
    )

    print(
        "\nConversational RAG "
        "Test Passed"
    )


if __name__ == "__main__":
    main()