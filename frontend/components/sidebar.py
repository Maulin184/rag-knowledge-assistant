import streamlit as st


def render_sidebar(api_client):

    with st.sidebar:

        st.title(
            "📚 RAG Assistant"
        )

        st.divider()

        # -------------------------
        # Upload Section
        # -------------------------

        st.subheader(
            "Upload Document"
        )

        with st.form(
            "upload_form",
            clear_on_submit=True
        ):

            uploaded_file = st.file_uploader(
                "Choose a PDF",
                type=["pdf"]
            )

            upload_clicked = (
                st.form_submit_button(
                    "Upload Document",
                    use_container_width=True
                )
            )

            if (
                upload_clicked
                and uploaded_file is not None
            ):

                with st.spinner(
                    "Processing document..."
                ):

                    api_client.upload_document(
                        uploaded_file
                    )

                st.success(
                    "Document uploaded successfully"
                )

        st.divider()

        # -------------------------
        # Documents Section
        # -------------------------

        st.subheader(
            "Documents"
        )

        documents = (
            api_client.get_documents()
        )

        if not documents:

            st.info(
                "No documents uploaded"
            )

        else:

            for document in documents:

                selected = (
                    document["document_id"]
                    ==
                    st.session_state.selected_document_id
                )

                label = (
                    f"📄 {document['filename']}"
                    if selected
                    else document["filename"]
                )

                if st.button(
                    label,
                    key=document[
                        "document_id"
                    ],
                    use_container_width=True
                ):

                    st.session_state.selected_document_id = (
                        document[
                            "document_id"
                        ]
                    )

                    st.session_state.selected_document_name = (
                        document[
                            "filename"
                        ]
                    )

                    st.session_state.conversation_id = None

                    st.session_state.messages = []

                    st.rerun()

        st.divider()

        # -------------------------
        # Conversations Section
        # -------------------------

        st.subheader(
            "Conversations"
        )

        if (
            st.session_state.selected_document_id
            is None
        ):

            st.info(
                "Select a document"
            )

        else:

            conversations = (
                api_client.get_conversations(
                    st.session_state.selected_document_id
                )
            )

            if st.button(
                "➕ New Chat",
                key="new_chat",
                use_container_width=True
            ):

                conversation = (
                    api_client.create_conversation(
                        st.session_state.selected_document_id
                    )
                )

                st.session_state.conversation_id = (
                    conversation[
                        "conversation_id"
                    ]
                )

                st.session_state.messages = []

                st.rerun()

            for conversation in (
                conversations.get(
                    "conversations",
                    []
                )
            ):

                conversation_id = (
                    conversation[
                        "conversation_id"
                    ]
                )

                selected = (
                    conversation_id
                    ==
                    st.session_state.conversation_id
                )

                # label = (
                #     f"💬 {conversation_id['title']}"
                # )
                label = (
                    f"💬 {conversation.get('title', 'New Conversation')}"
                )

                if selected:

                    label = (
                        f"👉 {label}"
                    )

                if st.button(
                    label,
                    key=conversation_id,
                    use_container_width=True
                ):

                    st.session_state.conversation_id = (
                        conversation_id
                    )

                    conversation_data = (
                        api_client.get_conversation(
                            conversation_id
                        )
                    )

                    st.session_state.messages = (
                        conversation_data[
                            "messages"
                        ]
                    )

                    st.rerun()