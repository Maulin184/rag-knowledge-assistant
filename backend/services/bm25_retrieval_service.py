from rank_bm25 import BM25Okapi
import re

from backend.models.domain import (
    RetrievedChunk
)
from backend.models.domain import (
    RetrievalResult
)


class BM25RetrievalService:

    def __init__(
        self,
        vector_store
    ):
        self.vector_store = vector_store

    def retrieve(
        self,
        question: str,
        k: int = 4
    ):

        documents = []

        for chunk in self.vector_store.metadata:

            documents.append(
                self.tokenize(
                    chunk.text
                )
            )

        bm25 = BM25Okapi(
            documents
        )

        scores = bm25.get_scores(
            self.tokenize(
                question
            )
        )

        ranked_indices = (
            sorted(
                range(len(scores)),
                key=lambda i: scores[i],
                reverse=True
            )[:k]
        )

        results = []

        for idx in ranked_indices:

            chunk = (
                self.vector_store.metadata[idx]
            )

            results.append(
                RetrievedChunk(
                    text=chunk.text,
                    source=chunk.source,
                    page=chunk.page,
                    total_pages=chunk.total_pages,
                    chunk_id=chunk.chunk_id,
                    distance=0.0
                )
            )

        # return results
        return RetrievalResult(
            context="\n\n".join([r.text for r in results]),
            retrieved_chunks=results
        )
    
    def tokenize(
        self,
        text: str
    ):

        text = text.lower()

        return re.findall(
            r"\w+",
            text
        )