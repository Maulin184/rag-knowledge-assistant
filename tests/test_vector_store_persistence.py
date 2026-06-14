from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager
from backend.core.embeddings import EmbeddingManager
from backend.core.vector_store import VectorStoreManager


def main():

    document_id = "doc_001"

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
    print("SAVING INDEX")
    print("=" * 60)

    vector_store.save_index(
        document_id=document_id
    )

    print(
        f"Index Saved For: "
        f"{document_id}"
    )

    print("\n" + "=" * 60)
    print("LOADING INDEX")
    print("=" * 60)

    new_store = VectorStoreManager()

    new_store.load_index(
        document_id=document_id
    )

    print(
        f"Vectors Loaded: "
        f"{new_store.index.ntotal}"
    )

    print("\n" + "=" * 60)
    print("TESTING SEARCH")
    print("=" * 60)

    query = "What is attention?"

    query_embedding = (
        embedder.embed_query(
            query
        )
    )

    results = new_store.search(
        query_embedding=query_embedding,
        k=3
    )

    print(f"Query: {query}")

    print("\nTop Results:\n")

    for rank, result in enumerate(
        results,
        start=1
    ):

        print("-" * 60)
        print(f"Rank: {rank}")
        print(f"Chunk ID: {result.chunk_id}")
        print(f"Page: {result.page}")
        print(f"Distance: {result.distance}")

        print("\nPreview:\n")

        print(
            result.text[:300]
        )

        print()

    print("=" * 60)
    print("PERSISTENCE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()