# RAG Knowledge Assistant

A production-grade Retrieval Augmented Generation (RAG) application built with:

- Python
- Streamlit
- FAISS
- HuggingFace Embeddings
- Groq LLM
- LangChain

## Features

- PDF Upload
- Semantic Search
- Vector Retrieval
- Context-Aware Answers
- Source Citations


How to run test files:
- Eg. "python -m tests.test_document_loader"

How to run main.py file:
- uvicorn backend.main:app --reload