from backend.models.domain import (
    RetrievalResult
)


class HybridRetrievalService:

    def __init__(
        self,
        semantic_retriever,
        bm25_retriever
    ):
        self.semantic_retriever = (
            semantic_retriever
        )

        self.bm25_retriever = (
            bm25_retriever
        )

    def retrieve(
        self,
        question: str,
        k: int = 4
    ):

        semantic_result = (
            self.semantic_retriever.retrieve(
                question=question,
                k=k
            )
        )

        semantic_chunks = (
            semantic_result.retrieved_chunks
        )

        bm25_result = (
            self.bm25_retriever.retrieve(
                question=question,
                k=k
            )
        )

        bm25_chunks = bm25_result.retrieved_chunks

        rrf_scores = {}

        rrf_k = 60

        # -------------------
        # Semantic Results
        # -------------------

        for rank, chunk in enumerate(
            semantic_chunks,
            start=1
        ):

            chunk_id = chunk.chunk_id

            if chunk_id not in rrf_scores:

                rrf_scores[
                    chunk_id
                ] = {
                    "chunk": chunk,
                    "score": 0.0
                }

            rrf_scores[
                chunk_id
            ][
                "score"
            ] += (
                1 / (rrf_k + rank)
            )

        # -------------------
        # BM25 Results
        # -------------------

        for rank, chunk in enumerate(
            bm25_chunks,
            start=1
        ):

            chunk_id = chunk.chunk_id

            if chunk_id not in rrf_scores:

                rrf_scores[
                    chunk_id
                ] = {
                    "chunk": chunk,
                    "score": 0.0
                }

            rrf_scores[
                chunk_id
            ][
                "score"
            ] += (
                1 / (rrf_k + rank)
            )

        fused_chunks = []

        for item in (
            rrf_scores.values()
        ):

            chunk = item["chunk"]

            chunk.rrf_score = (
                item["score"]
            )

            fused_chunks.append(
                chunk
            )

        fused_chunks.sort(
            key=lambda chunk:
            chunk.rrf_score,
            reverse=True
        )

        final_chunks = (
            fused_chunks[:k]
        )

        context = "\n\n".join(
            [
                chunk.text
                for chunk in final_chunks
            ]
        )

        return RetrievalResult(
            context=context,
            retrieved_chunks=final_chunks
        )