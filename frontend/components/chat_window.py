import streamlit as st


def render_chat_window(
    api_client
):

    # -------------------------
    # No Document Selected
    # -------------------------

    if (
        st.session_state.selected_document_id
        is None
    ):

        st.title(
            "📚 RAG Knowledge Assistant"
        )

        st.markdown(
            """
            Upload a PDF and chat with your documents using
            Retrieval-Augmented Generation (RAG).

            ### What can you do?

            - 📄 Summarize documents
            - 🧠 Explain concepts
            - 📝 Generate study notes
            - 🔍 Extract key insights
            - 💬 Ask follow-up questions

            ### Getting Started

            1. Upload a PDF from the sidebar
            2. Select the document
            3. Create a conversation
            4. Start chatting
            """
        )

        st.divider()

        st.subheader(
            "💡 Example Questions"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                "Summarize this document"
            )

            st.info(
                "What are the key concepts?"
            )

        with col2:

            st.info(
                "Create study notes"
            )

            st.info(
                "Explain this like I'm 10"
            )

        return

    # -------------------------
    # Header
    # -------------------------

    st.title(
        f"📄 {st.session_state.selected_document_name}"
    )

    st.caption(
        "Ask questions and get source-grounded answers"
    )

    st.info(
        f"""
    Selected Document:
    {st.session_state.selected_document_name}

    Status:
    Ready for chat
    """
    )

    st.divider()

    # -------------------------
    # Display Existing Messages
    # -------------------------

    for message in (
        st.session_state.messages
    ):

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

            if (
                message["role"]
                == "assistant"
            ):

                sources = (
                    message.get(
                        "sources",
                        []
                    )
                )

                if sources:

                    with st.expander(
                        "📚 Sources"
                    ):

                        # for source in sources:

                        #     st.markdown(
                        #         f"""
                        #         **Page:** {source['page']}

                        #         **Chunk ID:** {source['chunk_id']}

                        #         **Distance:** {source['distance']:.4f}
                        #         """
                        #     )

                        #     st.divider()

                        for i, source in enumerate(sources):
                            snippet = source['snippet'][:250]
                            st.markdown(
                                f"""
                        ### 📄 Source {i + 1}

                        ** Page: ** {source['page']}

                        > {snippet}...

                        """
                            )

                            st.divider()

    # -------------------------
    # No Conversation Selected
    # -------------------------

    if (
        st.session_state.conversation_id
        is None
    ):

        st.info(
            "Create or select a conversation to start chatting."
        )

        return

    # -------------------------
    # Chat Input
    # -------------------------

    user_question = st.chat_input(
        "Ask a question..."
    )

    if not user_question:

        return

    # -------------------------
    # Show User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message(
        "user"
    ):

        st.markdown(
            user_question
        )

    # -------------------------
    # Generate Assistant Response
    # -------------------------

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            response = (
                api_client.chat(
                    conversation_id=(
                        st.session_state.conversation_id
                    ),
                    document_id=(
                        st.session_state.selected_document_id
                    ),
                    question=user_question
                )
            )

        answer = (
            response["answer"]
        )

        st.markdown(
            answer
        )

        sources = response.get(
            "sources",
            []
        )

        if sources:

            with st.expander(
                "📚 Sources"
            ):

                for i, source in enumerate(sources):
                    
                    snippet = source["snippet"][:250]
                    st.markdown(
                         f"""
                        ### 📄 Source {i + 1}

                        ** Page: ** {source['page']}

                        > {snippet}...
                        """
                    )

                    st.divider()

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": response.get(
                "sources",
                []
            )
        }
    )