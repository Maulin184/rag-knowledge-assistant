from backend.core.document_loader import (
    DocumentLoader
)

from backend.core.chunking import (
    ChunkingManager
)

from backend.core.embeddings import (
    EmbeddingManager
)


def main():

    loader = DocumentLoader()
    chunker = ChunkingManager()
    embedder = EmbeddingManager()

    documents = loader.load_pdf(
        "brief_ml_notes.pdf"
    )

    chunks = chunker.create_chunks(
        documents
    )

    embedded_chunks = (
        embedder.embed_documents(
            chunks
        )
    )

    print("=" * 50)
    print(f"Chunks: {len(chunks)}")
    print(
        f"Embedded Chunks: "
        f"{len(embedded_chunks)}"
    )
    print("=" * 50)

    first = embedded_chunks[0]

    print(
        f"Chunk ID: {first.chunk_id}"
    )

    print(
        f"Embedding Length: "
        f"{len(first.embedding)}"
    )

    print(
        f"Page: {first.page}"
    )

    print(
        f"Source: {first.source}"
    )

    print(
        f"Embedding: {first.embedding[:5]}"
    )

    query_vector = embedder.embed_query(
        "What is attention?"
    )

    print(len(query_vector))


if __name__ == "__main__":
    main()