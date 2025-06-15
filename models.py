from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
load_dotenv()  # reads .env file

API_TOKEN = os.getenv("HF_API_TOKEN")
client = InferenceClient(token=API_TOKEN)

def invoke(prompt: str) -> str:
    """
    Invoke the HuggingFace Inference API for text generation.
    Returns the generated text (continuation) from the prompt.
    """
    try:
        response = client.text_generation(
            model="mistralai/Mistral-7B-Instruct-v0.1",  # You can replace with a better model here
            inputs=prompt,
            parameters={
                "max_new_tokens": 128,
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 50,
                "repetition_penalty": 1.2,
                "do_sample": True,
            },
        )
        # response.generated_text contains prompt + generated text, so we return all text
        return response.generated_text.strip()
    except Exception as e:
        raise Exception(f"Generation failed: {e}")

