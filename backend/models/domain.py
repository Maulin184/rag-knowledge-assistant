from dataclasses import dataclass

@dataclass
class Document:
    content: str
    source: str
    page: int
    total_pages: int

@dataclass
class Chunk:
    text: str
    source: str
    page: int
    total_pages: int
    chunk_id: int

@dataclass
class EmbeddedChunk:
    text: str
    source: str
    page: int
    total_pages: int
    chunk_id: int
    embedding: list[float]

@dataclass
class RetrievedChunk:
    text: str
    source: str
    page: int
    total_pages: int
    chunk_id: int
    distance: float

@dataclass
class RetrievalResult:
    context: str
    retrieved_chunks: list[RetrievedChunk]

@dataclass
class DocumentInfo:
    document_id: str
    filename: str
    file_hash: str
    created_at: str

@dataclass
class RAGResponse:
    answer: str
    sources: list