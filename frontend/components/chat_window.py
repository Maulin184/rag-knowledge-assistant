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
            "📄 Document Chat"
        )

        st.info(
            "Select a document to begin."
        )

        return

    # -------------------------
    # Header
    # -------------------------

    st.title(
        st.session_state.selected_document_name
    )

    st.caption(
        "Chat with your document"
    )

    st.divider()

    # -------------------------
    # Display Existing Messages
    # -------------------------

    # for message in (
    #     st.session_state.messages
    # ):

    #     with st.chat_message(
    #         message["role"]
    #     ):

    #         st.markdown(
    #             message["content"]
    #         )

    st.json(
        st.session_state.messages
    )
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

                        for source in sources:

                            st.markdown(
                                f"""
                                **Page:** {source['page']}

                                **Chunk ID:** {source['chunk_id']}

                                **Distance:** {source['distance']:.4f}
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

                for source in sources:

                    st.markdown(
                        f"""
    **Page:** {source['page']}

    **Chunk ID:** {source['chunk_id']}

    **Distance:** {source['distance']:.4f}
    """
                    )

                    st.divider()

    # -------------------------
    # Save Assistant Message
    # -------------------------

    # st.session_state.messages.append(
    #     {
    #         "role": "assistant",
    #         "content": answer
    #     }
    # )

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