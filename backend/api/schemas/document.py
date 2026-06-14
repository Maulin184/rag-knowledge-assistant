from pydantic import BaseModel


class DocumentUploadResponse(
    BaseModel
):
    document_id: str
    filename: str
    already_exists: bool

class DocumentResponse(
    BaseModel
):
    document_id: str
    filename: str
    file_hash: str
    created_at: str