
"""Handle queries with RAG."""

from vector_store import create_vector_store
from models import llm, invoke
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
import bs4
import logging
import os

logger = logging.getLogger(__name__)

# Set USER_AGENT to suppress warning
os.environ["USER_AGENT"] = "RAG_Bot_2025/1.0"

# Load and chunk contents of the blog
try:
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()
    logger.info("Loaded %d documents from web", len(docs))
except Exception as e:
    logger.error("Failed to load web content: %s", e)
    raise

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
all_splits = text_splitter.split_documents(docs)
logger.info("Split into %d chunks", len(all_splits))

# Store embeddings in ChromaDB
vector_store = create_vector_store(all_splits)

def retrieve(question: str) -> list:
    """Retrieve relevant documents."""
    try:
        docs = vector_store.similarity_search(question, k=3)
        logger.info("Retrieved %d documents for question: %s", len(docs), question)
        return docs
    except Exception as e:
        logger.error("Retrieval failed: %s", e)
        raise

def generate(question: str) -> str:
    """Generate answer using RAG."""
    try:
        retrieved_docs = retrieve(question)
        context = "\n".join(doc.page_content for doc in retrieved_docs)[:500]
        prompt = (
            f"You are an assistant answering questions based solely on the provided context about AI agents. "
            f"Provide a clear, concise answer directly related to the context. "
            f"If the question is vague, interpret it in the context of AI agents. "
            f"Avoid generic or repetitive phrases.\n\n"
            f"Context: {context}\n\n"
            f"Question: {question}\n\n"
            f"Answer:"
        )
        answer = invoke(prompt)
        logger.info(f"Query: {question}\nAnswer: {answer}")
        return answer
    except Exception as e:
        logger.error(f"Generation failed: %s", e)
        raise
