from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager
from backend.core.embeddings import EmbeddingManager
from backend.core.vector_store import VectorStoreManager


def main():

    print("=" * 50)
    print("LOADING DOCUMENTS")
    print("=" * 50)

    loader = DocumentLoader()
    documents = loader.load_pdf("brief_ml_notes.pdf")

    print(f"Documents Loaded: {len(documents)}")

    print("\n" + "=" * 50)
    print("CREATING CHUNKS")
    print("=" * 50)

    chunker = ChunkingManager()
    chunks = chunker.create_chunks(documents)

    print(f"Chunks Created: {len(chunks)}")

    print("\n" + "=" * 50)
    print("GENERATING EMBEDDINGS")
    print("=" * 50)

    embedder = EmbeddingManager()
    embedded_chunks = embedder.embed_documents(chunks)

    print(f"Embedded Chunks: {len(embedded_chunks)}")

    print("\n" + "=" * 50)
    print("CREATING FAISS INDEX")
    print("=" * 50)

    vector_store = VectorStoreManager()

    vector_store.create_index(
        embedded_chunks
    )

    print(
        f"Vectors In Index: "
        f"{vector_store.index.ntotal}"
    )

    print("\n" + "=" * 50)
    print("TESTING SEARCH")
    print("=" * 50)

    query = "What is unsupervised Learning?"

    query_embedding = (
        embedder.embed_query(query)
    )

    results = vector_store.search(
        query_embedding=query_embedding,
        k=3
    )

    print(f"Query: {query}")

    print("\nTop Results:\n")

    for idx, result in enumerate(
        results,
        start=1
    ):

        print("-" * 50)
        print(f"Rank: {idx}")
        print(f"Chunk ID: {result.chunk_id}")
        print(f"Page: {result.page}")
        print(f"Distance: {result.distance}")

        print("\nPreview:\n")

        print(result.text[:300])

        print()

    print("=" * 50)
    print("TEST COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()