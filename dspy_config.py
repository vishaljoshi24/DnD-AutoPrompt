import os
from pathlib import Path
from dotenv import load_dotenv

ollama_key=load_dotenv(Path("~/.env"))

OLLAMA_CONFIG = {
    "api_key": os.getenv("OLLAMA_KEY"),
    "default_model": "llama3.2:1b",
    "embed_model": "nomic-embed-text",
    "temperature": 0.1,
}

DSPY_CONFIG = {
    "model": f"ollama_chat/{OLLAMA_CONFIG["default_model"]}",
    "api_key": OLLAMA_CONFIG["api_key"],
    "temperature": 0.1,
    "max_tokens": 1024,
}


TRAIN = [
    
]