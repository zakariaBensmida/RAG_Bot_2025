from vector_store import create_vector_store
from web_loader import load_web_content
from models import llm

# Load web content and initialize vector store
docs = load_web_content("https://lilianweng.github.io/posts/2023-06-23-agent/")
vector_store = create_vector_store(docs)  # ✅ Define vector_store

def retrieve(question):
    return vector_store.similarity_search(question)

def generate(question):
    retrieved_docs = retrieve(question)
    context = "\n".join(doc.page_content for doc in retrieved_docs)
    prompt = f"Answer based on context:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    return llm(prompt)
