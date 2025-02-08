# models.py - Load Llama Model
from langchain_community.llms import LlamaCpp
import os

MODEL_PATH = r"C:\Users\zakar\Chatbot\models\llama-2-7b.Q5_K_M.gguf"
llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_ctx=4096,  # Set the context length
    temperature=0.7,  # Control response randomness
    max_tokens=512  # Limit output length
)


