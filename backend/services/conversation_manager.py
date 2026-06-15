from pathlib import Path

import json
import uuid

from datetime import datetime


class ConversationManager:

    def __init__(
        self,
        registry_path="storage/metadata/conversations.json"
    ):
        self.registry_path = Path(
            registry_path
        )

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_registry(
        self
    ):

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

    def create_conversation(
        self,
        document_id: str
    ):

        registry = (
            self.load_registry()
        )

        conversation_id = (
            f"conv_{uuid.uuid4().hex[:8]}"
        )

        conversation = {
            "conversation_id": (
                conversation_id
            ),
            "document_id": (
                document_id
            ),
            "title": "New Conversation",
            "created_at": (
                datetime.utcnow()
                .isoformat()
            ),
            "messages": []
        }

        registry[
            conversation_id
        ] = conversation

        self.save_registry(
            registry
        )

        return conversation

    def get_conversation(
        self,
        conversation_id: str
    ):

        registry = (
            self.load_registry()
        )

        return registry.get(
            conversation_id
        )

    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str
    ):

        registry = (
            self.load_registry()
        )

        if (
            conversation_id
            not in registry
        ):
            raise ValueError(
                f"Conversation "
                f"{conversation_id} "
                f"not found"
            )

        # registry[
        #     conversation_id
        # ][
        #     "messages"
        # ].append(
        #     {
        #         "role": role,
        #         "content": content
        #     }
        # )
        conversation = registry[
            conversation_id
        ]

        if (
            role == "user"
            and conversation["title"]
            == "New Conversation"
        ):

            title = content.strip()

            if len(title) > 40:

                title = (
                    title[:40] + "..."
                )

            conversation["title"] = (
                title
            )

        conversation[
            "messages"
        ].append(
            {
                "role": role,
                "content": content
            }
        )

        self.save_registry(
            registry
        )

    def get_messages(
        self,
        conversation_id: str
    ):

        conversation = (
            self.get_conversation(
                conversation_id
            )
        )

        if conversation is None:

            raise ValueError(
                f"Conversation "
                f"{conversation_id} "
                f"not found"
            )

        return conversation[
            "messages"
        ]
    
    def get_recent_messages(
        self,
        conversation_id: str,
        limit: int = 10
    ):

        messages = self.get_messages(
            conversation_id
        )

        return messages[-limit:]
    
    def get_conversations_by_document(
        self,
        document_id: str
    ):

        registry = self.load_registry()

        conversations = []

        for conversation in registry.values():

            if (
                conversation["document_id"]
                == document_id
            ):
                conversations.append(
                    conversation
                )

        return conversations