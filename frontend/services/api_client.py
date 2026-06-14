import requests


class APIClient:

    def __init__(
        self,
        base_url="http://localhost:8000"
    ):
        self.base_url = (
            base_url
        )

    # -------------------------
    # Documents
    # -------------------------

    def upload_document(
        self,
        file
    ):

        files = {
            "file": (
                file.name,
                file,
                "application/pdf"
            )
        }

        response = requests.post(
            f"{self.base_url}/documents/upload",
            files=files
        )

        response.raise_for_status()

        return response.json()

    def get_documents(
        self
    ):

        response = requests.get(
            f"{self.base_url}/documents"
        )

        response.raise_for_status()

        return response.json()

    # -------------------------
    # Conversations
    # -------------------------

    def create_conversation(
        self,
        document_id
    ):

        payload = {
            "document_id": (
                document_id
            )
        }

        response = requests.post(
            f"{self.base_url}/conversations",
            json=payload
        )

        response.raise_for_status()

        return response.json()

    def get_conversations(
        self,
        document_id
    ):

        response = requests.get(
            f"{self.base_url}/conversations/document/{document_id}"
        )

        response.raise_for_status()

        return response.json()

    def get_conversation(
        self,
        conversation_id
    ):

        response = requests.get(
            f"{self.base_url}/conversations/{conversation_id}"
        )

        response.raise_for_status()

        return response.json()

    # -------------------------
    # Chat
    # -------------------------

    def chat(
        self,
        conversation_id,
        document_id,
        question
    ):

        payload = {
            "conversation_id": (
                conversation_id
            ),
            "document_id": (
                document_id
            ),
            "question": (
                question
            )
        }

        response = requests.post(
            f"{self.base_url}/chat",
            json=payload
        )

        response.raise_for_status()

        return response.json()