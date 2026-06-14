from backend.models.domain import (
    RetrievalResult
)


class RetrievalService:

    def __init__(
        self,
        embedder,
        vector_store
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(
        self,
        question: str,
        k: int = 4
    ) -> RetrievalResult:
        
        query_embedding = (
            self.embedder.embed_query(
                question
            )
        )

        chunks = (
            self.vector_store.search(
                query_embedding,
                k=k
            )
        )

        context_parts = []

        for chunk in chunks:

            context_parts.append(
                chunk.text
            )

        context = "\n\n".join(
            context_parts
        )

        return RetrievalResult(
            context=context,
            retrieved_chunks=chunks
        )