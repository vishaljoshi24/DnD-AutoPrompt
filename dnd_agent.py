import dspy
import os
from dspy_config import OLLAMA_CONFIG
from dotenv import load_dotenv
from pathlib import Path
from modules import GenerateGameMasterInstruction, GeneratePremise, GeneratePlayerInstruction

ollama_key=load_dotenv(Path("~/.env"))

class DnDAgent(dspy.Module):
    def __init__(self):
        lm = dspy.LM(f"ollama_chat/{OLLAMA_CONFIG["default_model"]}", 
                     api_base="http://localhost:11434", 
                     api_key=OLLAMA_CONFIG["api_key"])
        dspy.configure(lm=lm)
    
    

        