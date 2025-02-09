from vector_store import create_vector_store
from models import llm
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
# Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Use a free sentence transformer embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store embeddings in a local vector database (FAISS or ChromaDB)
vector_store = Chroma.from_documents(all_splits, embeddings)

def retrieve(question):
    return vector_store.similarity_search(question)

def generate(question):
    retrieved_docs = retrieve(question)
    context = "\n".join(doc.page_content for doc in retrieved_docs)
    prompt = f"Answer based on context:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    return llm.invoke(prompt)
