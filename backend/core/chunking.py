from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from backend.models.domain import (
    Document,
    Chunk
)

from backend.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class ChunkingManager:

    def __init__(self):

        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP
            )
        )

    def create_chunks(
        self,
        documents: list[Document]
    ) -> list[Chunk]:

        chunks = []

        chunk_id = 1

        for document in documents:

            split_texts = (
                self.text_splitter.split_text(
                    document.content
                )
            )

            for text in split_texts:

                chunks.append(
                    Chunk(
                        text=text,
                        source=document.source,
                        page=document.page,
                        chunk_id=chunk_id,
                        total_pages=document.total_pages
                    )
                )

                chunk_id += 1

        return chunks