from pathlib import Path
import json
import hashlib
from datetime import datetime


class DocumentManager:

    def __init__(
        self,
        registry_path="storage/metadata/documents.json"
    ):
        self.registry_path = Path(
            registry_path
        )

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_registry(self):

        if not self.registry_path.exists():
            return {}

        with open(
            self.registry_path,
            "r"
        ) as f:

            return json.load(f)
        
    def save_registry(
        self,
        registry
    ):

        with open(
            self.registry_path,
            "w"
        ) as f:

            json.dump(
                registry,
                f,
                indent=4
            )

    def calculate_hash(
        self,
        file_path
    ):
        
        sha256 = hashlib.sha256()

        with open(
            file_path,
            "rb"
        ) as f:

            while chunk := f.read(8192):

                sha256.update(chunk)

        return sha256.hexdigest()
    
    def find_document_by_hash(
        self,
        file_hash
        ):

        registry = self.load_registry()

        for document in registry.values():

            if (
                document["file_hash"]
                == file_hash
            ):
                return document

        return None
    
    def register_document(
        self,
        file_path
    ):

        registry = self.load_registry()

        file_hash = self.calculate_hash(
            file_path
        )

        existing_document = (
            self.find_document_by_hash(
                file_hash
            )
        )

        if existing_document:

            return {
                "document_id": existing_document["document_id"],
                "filename": existing_document["filename"],
                "file_hash": existing_document["file_hash"],
                "already_exists": True
            }

        document_id = (
            f"doc_{len(registry) + 1:03d}"
        )

        document_info = {
            "document_id": document_id,
            "filename": Path(file_path).name,
            "file_hash": file_hash,
            "created_at": datetime.now().isoformat()
        }

        registry[document_id] = document_info

        self.save_registry(
            registry
        )

        return {
            **document_info,
            "already_exists": False
        }
    
    def get_all_documents(self):

        registry = self.load_registry()

        return list(
            registry.values()
        )