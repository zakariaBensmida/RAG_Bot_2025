# models.py - Load Llama Model
from langchain_community.llms import LlamaCpp
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/llama-2-7b.Q5_K_M.gguf")
llm = LlamaCpp(model_path=MODEL_PATH)

