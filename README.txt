
# RAG Bot 2025: Document Q&A

A FastAPI-based RAG app for answering queries over web-scraped and PDF documents using LangChain, ChromaDB, Hugging Face Transformers, and a modern web interface.

## Features
- Web scraping with LangChain’s WebBaseLoader
- PDF text extraction with PyMuPDF
- Embeddings with Hugging Face (all-MiniLM-L6-v2)
- Vector storage with ChromaDB
- Query answering with Hugging Face Transformers (distilgpt2, no token required)
- FastAPI web interface with Tailwind CSS
- Linting with black and ruff
- Optional AWS S3 integration via aws_utils (placeholder for cloud skills)

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Place PDFs or text files in `data/raw/` or use web scraping.
3. Run app: `uvicorn main:app --host 127.0.0.1 --port 8000 --reload`
4. Access at `http://localhost:8000`.

## Notes
- Global Python used; virtual environments recommended.
- Sensitive data (e.g., `.env`, `data/`) excluded via `.gitignore`.
- AWS placeholders in `.env.example` demonstrate cloud compatibility.
- Uses Hugging Face Transformers with no token or persistent download.

## Project Structure
```
├── data/
│   ├── raw/
│   └── processed/
├── templates/
│   └── index.html
├── src/
│   ├── aws_utils.py
├── web_loader.py
├── pdf_extractor.py
├── vector_store.py
├── query_handler.py
├── models.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
