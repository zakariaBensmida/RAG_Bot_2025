# query_handler.py - RAG Logic
def retrieve(question, vector_store):
    return vector_store.similarity_search(question)
    
def generate(question):
    retrieved_docs = retrieve(question, vector_store)  # ✅ Pass vector_store
    context = "\n".join(doc.page_content for doc in retrieved_docs)
    prompt = f"Answer based on context:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    return llm(prompt)
