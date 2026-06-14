class DocumentLoaderError(Exception):
    """Base exception for document loading."""


class InvalidPDFError(DocumentLoaderError):
    """Raised when file is not a valid PDF."""


class EmptyPDFError(DocumentLoaderError):
    """Raised when PDF contains no extractable text."""