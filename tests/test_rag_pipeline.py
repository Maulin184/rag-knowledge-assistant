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


def main():

    load_dotenv()

    print("=" * 60)
    print("INITIALIZING COMPONENTS")
    print("=" * 60)

    document_manager = DocumentManager()

    loader = DocumentLoader()

    chunker = ChunkingManager()

    embedder = EmbeddingManager()

    vector_store = VectorStoreManager()

    retrieval_service = RetrievalService(
        embedder=embedder,
        vector_store=vector_store
    )

    api_key = os.getenv(
        "GROQ_API_KEY"
    )

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env"
        )

    llm_service = LLMService(
        api_key=api_key
    )

    pipeline = RAGPipeline(
        document_manager=document_manager,
        loader=loader,
        chunker=chunker,
        embedder=embedder,
        vector_store=vector_store,
        retrieval_service=retrieval_service,
        llm_service=llm_service
    )

    print("\n" + "=" * 60)
    print("INGESTING PDF")
    print("=" * 60)

    document_info = (
        pipeline.ingest_pdf(
            "ML_for_science.pdf"
        )
    )

    print("\nDocument Information:\n")

    for key, value in document_info.items():

        print(
            f"{key}: {value}"
        )

    print("\n" + "=" * 60)
    print("ASKING QUESTION")
    print("=" * 60)

    question = (
        "How Machine learning is helpful in science?"
    )

    response = pipeline.ask(
        document_id=document_info[
            "document_id"
        ],
        question=question
    )

    print(
        f"\nQuestion: {question}"
    )

    print("\nAnswer:\n")

    print(response.answer)

    print("\n" + "=" * 60)
    print("SOURCES")
    print("=" * 60)

    for rank, source in enumerate(
        response.sources,
        start=1
    ):

        print(
            f"\nSource {rank}"
        )

        print(
            f"Chunk ID: "
            f"{source.chunk_id}"
        )

        print(
            f"Page: "
            f"{source.page}"
        )

        print(
            f"Distance: "
            f"{source.distance}"
        )

    print("\n" + "=" * 60)
    print("RAG PIPELINE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()