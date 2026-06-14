from pathlib import Path
from pypdf import PdfReader

from backend.models.domain import Document
from backend.core.exceptions import (
    InvalidPDFError,
    EmptyPDFError,
)


class DocumentLoader:
    """
    Loads PDF documents and converts them
    into Document objects.
    """

    def load_pdf(self, file_path: str) -> list[Document]:

        path = Path(file_path)

        # Check file existence
        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # Validate extension
        if path.suffix.lower() != ".pdf":
            raise InvalidPDFError(
                "Only PDF files are supported."
            )

        try:
            reader = PdfReader(file_path)

        except Exception as e:
            raise InvalidPDFError(
                f"Unable to read PDF: {e}"
            )

        total_pages = len(reader.pages)

        documents = []

        for page_num, page in enumerate(
            reader.pages,
            start=1
        ):

            text = page.extract_text()

            if text and text.strip():

                document = Document(
                    content=text.strip(),
                    source=path.name,
                    page=page_num,
                    total_pages=total_pages,
                )

                documents.append(document)

        if not documents:
            raise EmptyPDFError(
                "No extractable text found in PDF."
            )

        return documents