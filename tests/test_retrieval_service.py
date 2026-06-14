from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager
from backend.core.embeddings import EmbeddingManager
from backend.core.vector_store import VectorStoreManager
from backend.services.retrieval_service import RetrievalService

def main():

    print("=" * 60)
    print("LOADING DOCUMENT")
    print("=" * 60)

    loader = DocumentLoader()
    documents = loader.load_pdf("brief_ml_notes.pdf")

    print(f"Documents Loaded: {len(documents)}")

    print("\n" + "=" * 60)
    print("CREATING CHUNKS")
    print("=" * 60)

    chunker = ChunkingManager()
    chunks = chunker.create_chunks(documents)

    print(f"Chunks Created: {len(chunks)}")

    print("\n" + "=" * 60)
    print("GENERATING EMBEDDINGS")
    print("=" * 60)

    embedder = EmbeddingManager()

    embedded_chunks = embedder.embed_documents(
        chunks
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

    question = "What is supervised learning?"

    print(f"Question: {question}")

    result = retrieval_service.retrieve(
        question=question,
        k=4
    )

    print("\n" + "=" * 60)
    print("RETRIEVED CHUNKS")
    print("=" * 60)

    print(
        f"Number of Retrieved Chunks: "
        f"{len(result.retrieved_chunks)}"
    )

    for rank, chunk in enumerate(
        result.retrieved_chunks,
        start=1
    ):

        print("\n" + "-" * 60)
        print(f"Rank      : {rank}")
        print(f"Chunk ID  : {chunk.chunk_id}")
        print(f"Page      : {chunk.page}")
        print(f"Source    : {chunk.source}")
        print(f"Distance  : {chunk.distance}")

        print("\nPreview:\n")

        print(chunk.text[:300])

    print("\n" + "=" * 60)
    print("GENERATED CONTEXT")
    print("=" * 60)

    print(result.context[:1500])

    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    main()
