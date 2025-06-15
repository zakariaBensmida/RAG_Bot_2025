
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import logging

logger = logging.getLogger(__name__)

def create_vector_store(docs):
    """
    Create a ChromaDB vector store from documents using HuggingFace embeddings.
    """
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = Chroma.from_documents(docs, embeddings, persist_directory="data/processed")
        logger.info("Created vector store with %d documents", len(docs))
        return vector_store
    except Exception as e:
        logger.error("Failed to create vector store: %s", e)
        raise

