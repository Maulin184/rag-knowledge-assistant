from backend.services.hybrid_retrieval_service import (
    HybridRetrievalService
)

from backend.models.domain import RetrievedChunk, RetrievalResult


class MockRetriever:

    def __init__(self, chunks):
        self.chunks = chunks

    def retrieve(self, question, k=4):
        return RetrievalResult(
            context="",
            retrieved_chunks=self.chunks
        )


def test_hybrid_retrieval_rrf_fusion():

    # ------------------------
    # Fake semantic results
    # ------------------------
    semantic_chunks = [
        RetrievedChunk(
            text="chunk A",
            source="doc",
            page=1,
            total_pages=10,
            chunk_id=1,
            distance=0.2
        ),
        RetrievedChunk(
            text="chunk B",
            source="doc",
            page=2,
            total_pages=10,
            chunk_id=2,
            distance=0.3
        ),
    ]

    # ------------------------
    # Fake BM25 results
    # ------------------------
    bm25_chunks = [
        RetrievedChunk(
            text="chunk B",
            source="doc",
            page=2,
            total_pages=10,
            chunk_id=2,
            distance=0.0
        ),
        RetrievedChunk(
            text="chunk C",
            source="doc",
            page=3,
            total_pages=10,
            chunk_id=3,
            distance=0.0
        ),
    ]

    semantic_retriever = MockRetriever(semantic_chunks)
    bm25_retriever = MockRetriever(bm25_chunks)

    hybrid = HybridRetrievalService(
        semantic_retriever=semantic_retriever,
        bm25_retriever=bm25_retriever
    )

    result = hybrid.retrieve(
        question="test question",
        k=3
    )

    # ------------------------
    # Assertions
    # ------------------------

    assert isinstance(result, RetrievalResult)

    assert len(result.retrieved_chunks) == 3

    # Chunk B should rank highest (appears in both)
    top_chunk = result.retrieved_chunks[0]

    assert top_chunk.chunk_id == 2

    # Context should include all texts
    assert "chunk B" in result.context
    assert "chunk A" in result.context
    assert "chunk C" in result.context