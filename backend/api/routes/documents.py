from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from pathlib import Path
import shutil
from backend.dependencies import pipeline
from backend.dependencies import (
    document_manager
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    upload_dir = Path(
        "storage/uploads"
    )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = (
        upload_dir / file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    document_info = (
        pipeline.ingest_pdf(
            str(file_path)
        )
    )

    return document_info
    # return {
    #     "filename": file.filename,
    #     "saved_to": str(file_path)
    # }

@router.get("/")
def get_documents():

    documents = (
        document_manager
        .get_all_documents()
    )

    return documents