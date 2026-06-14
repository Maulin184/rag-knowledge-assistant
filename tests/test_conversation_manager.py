from backend.services.conversation_manager import (
    ConversationManager
)


def main():

    manager = (
        ConversationManager()
    )

    print(
        "\nCreating conversation..."
    )

    conversation = (
        manager.create_conversation(
            document_id="doc_001"
        )
    )

    conversation_id = (
        conversation[
            "conversation_id"
        ]
    )

    print(
        f"Conversation ID: "
        f"{conversation_id}"
    )

    print(
        "\nAdding messages..."
    )

    manager.add_message(
        conversation_id,
        "user",
        "What is attention?"
    )

    manager.add_message(
        conversation_id,
        "assistant",
        (
            "Attention is a mechanism "
            "that allows the model "
            "to focus on important "
            "parts of the input."
        )
    )

    print(
        "\nLoading messages..."
    )

    messages = (
        manager.get_messages(
            conversation_id
        )
    )

    print(
        "\nMessages:\n"
    )

    for message in messages:

        print(
            f"{message['role']}: "
            f"{message['content']}"
        )

    print(
        "\nConversation "
        "Manager Test Passed"
    )


if __name__ == "__main__":
    main()