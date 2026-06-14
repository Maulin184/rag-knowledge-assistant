# RAG Knowledge Assistant

**Production-Ready Conversational RAG System using FastAPI, Streamlit, FAISS, Sentence Transformers, and Groq Llama 3.3 70B**

## Overview

RAG Knowledge Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and interact with them through natural language conversations.

The system combines semantic search, vector embeddings, conversational memory, and Large Language Models (LLMs) to provide context-aware answers grounded in the uploaded documents. Each response includes source citations, enabling users to verify where information was retrieved from.

This project was built to demonstrate production-oriented GenAI engineering practices including document ingestion, vector search, retrieval pipelines, conversational memory, API development, and modern frontend integration.

## Why This Project?

Most RAG tutorials focus only on document retrieval and answer generation.

This project was designed to explore the complete lifecycle of a production-oriented Retrieval-Augmented Generation system, including document ingestion, semantic search, conversational memory, source attribution, API design, frontend integration, testing, and maintainable software architecture.

The goal was not simply to build a chatbot, but to engineer a modular and extensible platform that mirrors real-world GenAI applications.

---

## Key Features

### Document Processing

* Upload PDF documents
* Automatic text extraction
* Intelligent document chunking
* Persistent document registry
* Duplicate document detection using file hashing

### Retrieval-Augmented Generation (RAG)

* Semantic search using embeddings
* FAISS vector database
* Top-K context retrieval
* Context-aware answer generation
* Source-grounded responses

### Conversational AI

* Multi-conversation support
* Conversation history management
* Context-aware follow-up questions
* Persistent conversation storage

### Source Citations

* Page-level references
* Retrieved chunk tracking
* Similarity score visibility
* Transparent answer generation

### Modern Application Stack

* FastAPI backend
* Streamlit frontend
* Modular architecture
* REST API design
* Automated test suite

---

## System Architecture

```text
PDF Document
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
(Sentence Transformers)
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Groq Llama 3.3 70B
      │
      ▼
Answer + Citations
      │
      ▼
Streamlit UI
```

---

## Project Structure

```text
backend/
│
├── api/
├── core/
├── models/
├── services/
├── main.py
└── dependencies.py

frontend/
│
├── components/
├── services/
├── utils/
└── app.py

tests/

storage/
```

---

## Technology Stack

### Backend

* FastAPI
* Python
* Pydantic

### Retrieval Layer

* FAISS
* Sentence Transformers

### LLM

* Groq
* Llama 3.3 70B Versatile

### Frontend

* Streamlit

### Testing

* Pytest

### Version Control

* Git
* GitHub

---

## Design Decisions

### Why FastAPI?

FastAPI provides type-safe API development, automatic OpenAPI documentation, and excellent performance for AI applications.

### Why FAISS?

FAISS offers fast similarity search and efficient vector storage, making it ideal for local RAG experimentation and development.

### Why Streamlit?

Streamlit enables rapid development of interactive AI applications while keeping the focus on backend and retrieval engineering.

### Why Groq + Llama 3.3 70B?

Groq provides extremely low-latency inference while Llama 3.3 70B delivers strong reasoning and instruction-following capabilities.

## Current Capabilities

* Upload and process PDF documents
* Generate embeddings and build vector indexes
* Persist document indexes locally
* Ask questions about uploaded documents
* Maintain multiple conversations per document
* Display retrieval citations for every answer
* Retrieve conversation history

---

## API Endpoints

### Documents

```http
POST /documents/upload
GET /documents
```

### Conversations

```http
POST /conversations
GET /conversations/document/{document_id}
GET /conversations/{conversation_id}
```

### Chat

```http
POST /chat
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Maulin184/rag-knowledge-assistant.git
cd rag-knowledge-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Running the Application

### Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://localhost:8000
```

### Start Frontend

```bash
streamlit run frontend/app.py
```

Frontend:

```text
http://localhost:8501
```

---

## Roadmap

### Completed

* PDF ingestion
* Chunking pipeline
* Embedding generation
* FAISS integration
* Retrieval service
* Conversational memory
* Source citations
* FastAPI backend
* Streamlit frontend

### Planned Enhancements

* Conversation summarization
* Hybrid search
* Reranking
* Multi-document chat
* Authentication
* Deployment
* Evaluation framework
* LangChain integration where appropriate

---

## Screenshots

Screenshots and demo GIFs will be added in future updates.

---

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Semantic search
* LLM application development
* FastAPI
* Streamlit
* Software architecture
* API design
* Testing and validation
* Production-oriented GenAI engineering

---

## License

This project is intended for educational, research, and portfolio purposes.
