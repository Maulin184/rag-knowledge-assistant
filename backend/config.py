from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 4

MAX_CHAT_HISTORY = 5

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"