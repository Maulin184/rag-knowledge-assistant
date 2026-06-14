import os

from dotenv import load_dotenv

from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager
from backend.core.embeddings import EmbeddingManager
from backend.core.vector_store import VectorStoreManager

from backend.services.retrieval_service import RetrievalService
from backend.services.llm_service import LLMService


def main():

    load_dotenv()

    print("=" * 60)
    print("LOADING DOCUMENT")
    print("=" * 60)

    loader = DocumentLoader()

    documents = loader.load_pdf(
        "brief_ml_notes.pdf"
    )

    print(
        f"Documents Loaded: "
        f"{len(documents)}"
    )

    print("\n" + "=" * 60)
    print("CREATING CHUNKS")
    print("=" * 60)

    chunker = ChunkingManager()

    chunks = chunker.create_chunks(
        documents
    )

    print(
        f"Chunks Created: "
        f"{len(chunks)}"
    )

    print("\n" + "=" * 60)
    print("GENERATING EMBEDDINGS")
    print("=" * 60)

    embedder = EmbeddingManager()

    embedded_chunks = (
        embedder.embed_documents(
            chunks
        )
    )

    print(
        f"Embedded Chunks: "
        f"{len(embedded_chunks)}"
    )

    print("\n" + "=" * 60)
    print("CREATING FAISS INDEX")
    print("=" * 60)

    vector_store = VectorStoreManager()

    vector_store.create_index(
        embedded_chunks
    )

    print(
        f"Vectors In Index: "
        f"{vector_store.index.ntotal}"
    )

    print("\n" + "=" * 60)
    print("INITIALIZING RETRIEVAL SERVICE")
    print("=" * 60)

    retrieval_service = RetrievalService(
        embedder=embedder,
        vector_store=vector_store
    )

    print("\n" + "=" * 60)
    print("INITIALIZING LLM SERVICE")
    print("=" * 60)

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env"
        )

    llm_service = LLMService(
        api_key=api_key
    )

    question = "What is Machine Learning?"

    print(f"Question: {question}")

    print("\n" + "=" * 60)
    print("RETRIEVING CONTEXT")
    print("=" * 60)

    retrieval_result = (
        retrieval_service.retrieve(
            question=question,
            k=4
        )
    )

    print(
        f"Retrieved Chunks: "
        f"{len(retrieval_result.retrieved_chunks)}"
    )

    print("\n" + "=" * 60)
    print("GENERATING ANSWER")
    print("=" * 60)

    answer = llm_service.generate_answer(
        question=question,
        context=retrieval_result.context
    )

    print("\nANSWER:\n")

    print(answer)

    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()