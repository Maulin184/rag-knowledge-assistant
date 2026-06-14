import streamlit as st

from components.sidebar import (
    render_sidebar
)

from components.chat_window import (
    render_chat_window
)

from services.api_client import (
    APIClient
)

from utils.session import (
    initialize_session
)

client = APIClient()

initialize_session()

st.set_page_config(
    page_title=(
        "RAG Knowledge Assistant"
    ),
    page_icon="📚",
    layout="wide"
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

render_sidebar(client)

render_chat_window(client)