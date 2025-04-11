# main.py - FastAPI App with HTML interface

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from query_handler import generate
import uvicorn

app = FastAPI()

# Mount template and static directories
templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Web interface
@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "question": "", "answer": ""})

@app.post("/", response_class=HTMLResponse)
def form_post(request: Request, question: str = Form(...)):
    try:
        answer = generate(question)
    except Exception as e:
        answer = f"Error: {e}"
    return templates.TemplateResponse("index.html", {"request": request, "question": question, "answer": answer})

# Optional: API route (still accessible if needed)
@app.get("/ask")
def ask(question: str):
    try:
        answer = generate(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional for local running
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


