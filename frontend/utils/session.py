import streamlit as st


def initialize_session():

    if "documents" not in st.session_state:
        st.session_state.documents = []

    if "selected_document_id" not in st.session_state:
        st.session_state.selected_document_id = None

    if "selected_document_name" not in st.session_state:
        st.session_state.selected_document_name = None

    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = None

    if "messages" not in st.session_state:
        st.session_state.messages = []