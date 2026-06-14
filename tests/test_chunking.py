from backend.core.document_loader import DocumentLoader
from backend.core.chunking import ChunkingManager


def main():

    loader = DocumentLoader()
    chunker = ChunkingManager()

    documents = loader.load_pdf(
        "brief_ml_notes.pdf"
    )

    chunks = chunker.create_chunks(
        documents
    )

    print("=" * 50)
    print(f"Documents : {len(documents)}")
    print(f"Chunks    : {len(chunks)}")
    print("=" * 50)

    first_chunk = chunks[70]

    print(f"Chunk ID : {first_chunk.chunk_id}")
    print(f"Source   : {first_chunk.source}")
    print(f"Page     : {first_chunk.page}")

    print("\nPreview:\n")

    print(first_chunk.text[:500])


if __name__ == "__main__":
    main()