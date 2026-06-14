from sentence_transformers import SentenceTransformer

from backend.models.domain import (
    Chunk,
    EmbeddedChunk
)

from backend.config import (
    EMBEDDING_MODEL
)


class EmbeddingManager:

    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def embed_documents(
        self,
        chunks: list[Chunk]
    ) -> list[EmbeddedChunk]:

        texts = [
            chunk.text
            for chunk in chunks
        ]

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        embedded_chunks = []

        for chunk, vector in zip(
            chunks,
            vectors
        ):

            embedded_chunks.append(
                EmbeddedChunk(
                    text=chunk.text,
                    source=chunk.source,
                    page=chunk.page,
                    total_pages=chunk.total_pages,
                    chunk_id=chunk.chunk_id,
                    embedding=vector.tolist()
                )
            )

        return embedded_chunks

    def embed_query(
        self,
        query: str
    ) -> list[float]:

        vector = self.model.encode(
            query,
            normalize_embeddings=True
        )

        return vector.tolist()