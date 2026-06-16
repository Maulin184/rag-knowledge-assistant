# RAG Knowledge Assistant

**Production-Oriented Conversational RAG System using FastAPI, Streamlit, FAISS, BM25, Sentence Transformers, and Groq Llama 3.3 70B**

---

## Overview

RAG Knowledge Assistant is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them through natural language conversations.

The system combines semantic retrieval, keyword retrieval, vector embeddings, conversational memory, and Large Language Models (LLMs) to generate context-aware answers grounded in uploaded documents. Every response is accompanied by source citations, allowing users to inspect the retrieved evidence and verify the generated answer.

The project was intentionally built with a production-oriented mindset rather than as a simple RAG demo. The focus was on modular architecture, retrieval quality, explainability, maintainability, testing, and extensibility.

---

## Why This Project?

Most RAG tutorials stop at:

* Upload PDF
* Create embeddings
* Retrieve chunks
* Generate answer

Real-world GenAI systems require much more.

This project explores the complete lifecycle of a retrieval-augmented application including:

* Document ingestion
* Chunking and embedding pipelines
* Persistent vector storage
* Hybrid retrieval
* Conversational memory
* Source attribution
* API development
* Frontend integration
* Retrieval evaluation
* Automated testing
* Modular software architecture

The objective was not simply to build a chatbot, but to engineer a maintainable and extensible GenAI platform that mirrors real-world AI products.

---

## Key Features

### Document Processing

* Upload PDF documents
* Automatic text extraction
* Intelligent text chunking
* Persistent document registry
* Duplicate document detection using SHA-256 hashing
* Local document storage and indexing

### Retrieval-Augmented Generation (RAG)

* Semantic search using embeddings
* Keyword search using BM25
* Hybrid retrieval using Reciprocal Rank Fusion (RRF)
* FAISS vector database
* Top-K context retrieval
* Context-aware answer generation
* Source-grounded responses

### Conversational AI

* Multi-conversation support
* Conversation history management
* Follow-up question handling
* Context-aware interactions
* Persistent conversation storage

### Source Citations

* Page-level references
* Retrieved chunk tracking
* Similarity score visibility
* Source snippets
* Transparent answer generation

### Evaluation & Testing

* Retrieval evaluation framework
* Hit@K measurement
* Retrieval benchmarking dataset
* Unit testing with Pytest
* Retrieval quality validation

### Modern Application Stack

* FastAPI backend
* Streamlit frontend
* Modular architecture
* REST API design
* Service-oriented backend structure

---
## Application Demo

### Dashboard
![Dashboard]<img width="1366" height="768" alt="Dashboard" src="https://github.com/user-attachments/assets/856e4ff6-ba2a-4f66-9400-3fa977dd3c3b" />

### Question Answering
![Question Answering]<img width="1366" height="768" alt="question_answering_2" src="https://github.com/user-attachments/assets/4790ad07-97e4-4578-9f49-5512a67c9e47" />

### Source Citations
![Source Citations]<img width="1366" height="768" alt="sources" src="https://github.com/user-attachments/assets/82cc9243-bd00-45a1-b555-6833b7c0b414" />


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
      ├─────────────► Semantic Retrieval
      │
      └─────────────► BM25 Retrieval
                          │
                          ▼
                Reciprocal Rank Fusion
                          │
                          ▼
                  Hybrid Retrieval
                          │
                          ▼
                  Context Assembly
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
│
├── test_bm25_retrieval.py
├── test_hybrid_retrieval.py
└── evaluation/
    ├── evaluation_dataset.json
    └── test_retrieval_evaluation.py

storage/
│
├── conversations/
├── documents/
└── metadata/
```

---

## Technology Stack

### Backend

* FastAPI
* Python
* Pydantic

### Retrieval Layer

* FAISS
* BM25
* Sentence Transformers
* Reciprocal Rank Fusion (RRF)

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

FastAPI provides type-safe API development, automatic OpenAPI documentation, and high performance for AI-powered applications.

### Why FAISS?

FAISS offers efficient vector indexing and similarity search, making it ideal for local retrieval experimentation and production-style RAG pipelines.

### Why BM25?

Dense embeddings and semantic retrieval are powerful, but they often struggle with exact terminology, definitions, and keyword-heavy queries.

BM25 complements semantic search by capturing lexical relevance and improving retrieval robustness.

### Why Hybrid Retrieval?

Real-world retrieval systems rarely rely on a single retrieval strategy.

Hybrid retrieval combines:

* Semantic understanding from embeddings
* Exact matching from BM25

using Reciprocal Rank Fusion (RRF), resulting in more reliable retrieval performance.

### Why Streamlit?

Streamlit enables rapid development of interactive AI applications while allowing focus on retrieval engineering and backend architecture.

### Why Groq + Llama 3.3 70B?

Groq provides extremely low-latency inference while Llama 3.3 70B delivers strong reasoning, instruction-following capability, and high-quality response generation.

---

## Current Capabilities

* Upload and process PDF documents
* Generate embeddings and build vector indexes
* Build BM25 indexes
* Persist document indexes locally
* Hybrid retrieval using semantic search + BM25
* Ask questions about uploaded documents
* Maintain multiple conversations per document
* Display retrieval citations for every answer
* Retrieve conversation history
* Evaluate retrieval quality using benchmark questions

---

## Retrieval Evaluation Framework

One of the major goals of this project was to evaluate retrieval quality rather than relying solely on subjective chatbot responses.

The evaluation framework supports:

* Question-answer benchmark datasets
* Expected page annotations
* Hit@K evaluation
* Retrieval debugging
* Retrieval quality comparison

Example metrics:

```text
Questions: 10
Hits: 8
Hit@4: 80%
```

This provides a measurable way to improve retrieval quality over time.

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

Linux / Mac:

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

## Future Improvements

The project intentionally stops at a strong production-style MVP.

Potential future enhancements include:

### Retrieval Quality

* Dynamic Top-K retrieval
* Relevance threshold filtering
* Duplicate chunk removal
* Retrieval reranking models
* Query expansion techniques

### Context Management

* Token-aware context window management
* Adaptive context compression
* Conversation summarization
* Long-context support

### Citation Quality

* Inline citations
* Query-term highlighting
* Source relevance badges
* Improved evidence presentation

### Product Features

* Multi-document chat
* User authentication
* Document collections
* Team workspaces
* Export conversations

### Evaluation

* Recall@K
* Precision@K
* MRR (Mean Reciprocal Rank)
* NDCG
* LLM-as-a-Judge evaluation

### Deployment

* Docker
* CI/CD pipelines
* Cloud deployment
* Monitoring and observability

---

## Screenshots

Screenshots and demo GIFs will be added in future updates.

---

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Hybrid Retrieval Systems
* Semantic Search
* BM25 Retrieval
* Vector Databases
* Large Language Models (LLMs)
* FastAPI
* Streamlit
* API Design
* Software Architecture
* Testing & Validation
* Retrieval Evaluation
* Production-Oriented GenAI Engineering

---

## License

This project is intended for educational, research, and portfolio purposes.
