# main.py - FastAPI App
from fastapi import FastAPI, HTTPException
from query_handler import generate

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    try:
        answer = generate(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

