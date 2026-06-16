from backend.services.bm25_retrieval_service import (
    BM25RetrievalService
)

from backend.models.domain import (
    EmbeddedChunk
)


class MockVectorStore:

    def __init__(self):

        self.metadata = [
            EmbeddedChunk(
                text=(
                    "Supervised learning learns from "
                    "input output examples."
                ),
                source="test.pdf",
                page=1,
                total_pages=10,
                chunk_id=1,
                embedding=[]
            ),
            EmbeddedChunk(
                text=(
                    "Unsupervised learning discovers "
                    "patterns without labels."
                ),
                source="test.pdf",
                page=2,
                total_pages=10,
                chunk_id=2,
                embedding=[]
            ),
            EmbeddedChunk(
                text=(
                    "Deep learning uses neural "
                    "networks with many layers."
                ),
                source="test.pdf",
                page=3,
                total_pages=10,
                chunk_id=3,
                embedding=[]
            )
        ]


def test_bm25_retrieval():

    vector_store = MockVectorStore()

    bm25_service = (
        BM25RetrievalService(
            vector_store
        )
    )

    results = (
        bm25_service.retrieve(
            "What is supervised learning?",
            k=2
        )
    )

    assert len(results) == 2

    assert (
        results[0].chunk_id == 1
    )