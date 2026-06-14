from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 4

MAX_CHAT_HISTORY = 5

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

LLM_MODEL = "llama-3.3-70b-versatile"

MAX_TOKENS = 1024

TEMPERATURE = 0.1