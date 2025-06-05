
"""Load Hugging Face Transformers model."""

from transformers import pipeline
import os

# Use distilgpt2 for lightweight generation, fetched online
llm = pipeline(
    "text-generation",
    model="distilgpt2",
    tokenizer="distilgpt2",
    max_length=1024,
    max_new_tokens=128,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    repetition_penalty=1.2,
    do_sample=True,
    pad_token_id=50256,
    device=-1
)

def invoke(prompt):
    """Wrapper to mimic LangChain LLM invoke."""
    try:
        result = llm(
            prompt,
            max_length=1024,
            max_new_tokens=128,
            top_k=50,
            repetition_penalty=1.2,
            truncation=True,
            clean_up_tokenization_spaces=True
        )[0]["generated_text"]
        return result[len(prompt):].strip()
    except Exception as e:
        raise Exception(f"Generation failed: {e}")
