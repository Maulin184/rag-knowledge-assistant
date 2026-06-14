import pickle
from pathlib import Path

import faiss
import numpy as np

from backend.models.domain import (
    EmbeddedChunk,
    RetrievedChunk
)

class VectorStoreManager:

    def __init__(self):

        self.index = None
        self.metadata = []

    def get_document_directory(
        self,
        document_id: str
    ) -> Path:

        document_dir = (
            Path("storage/documents")
            / document_id
        )

        document_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        return document_dir

    def create_index(
        self,
        embedded_chunks: list[EmbeddedChunk]
    ):

        vectors = np.array(
            [chunk.embedding
            for chunk in embedded_chunks],
            dtype=np.float32
        )

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(vectors)

        self.metadata = embedded_chunks

    def save_index(
        self,
        document_id: str
    ):

        document_dir = (
            self.get_document_directory(
                document_id
            )
        )

        index_path = (
            document_dir / "index.faiss"
        )

        metadata_path = (
            document_dir / "metadata.pkl"
        )

        faiss.write_index(
            self.index,
            str(index_path)
        )

        with open(
            metadata_path,
            "wb"
        ) as f:

            pickle.dump(
                self.metadata,
                f
            )

    def load_index(
        self,
        document_id: str
    ):

        document_dir = (
            self.get_document_directory(
                document_id
            )
        )

        index_path = (
            document_dir / "index.faiss"
        )

        metadata_path = (
            document_dir / "metadata.pkl"
        )

        self.index = faiss.read_index(
            str(index_path)
        )

        with open(
            metadata_path,
            "rb"
        ) as f:

            self.metadata = (
                pickle.load(f)
            )

    def search(
        self,
        query_embedding,
        k=4
    ):
        query_vector = np.array(
            [query_embedding],
            dtype=np.float32
        )

        distances, indices = (
            self.index.search(
                query_vector,
                k
            )
        )

        results = []

        for distance, idx in zip(
            distances[0],
            indices[0]
        ):

            chunk = self.metadata[idx]

            results.append(
                RetrievedChunk(
                    text=chunk.text,
                    source=chunk.source,
                    page=chunk.page,
                    total_pages=chunk.total_pages,
                    chunk_id=chunk.chunk_id,
                    distance=float(distance)
                )
            )

        return results