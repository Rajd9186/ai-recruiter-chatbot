from langchain_community.vectorstores import FAISS
from db.embeddings import get_embeddings
from utils.markdown_parser import load_markdown

_vectorstore = None

def get_vectorstore():
    global _vectorstore

    if _vectorstore is None:
        text = load_markdown("data/cv.md")
        embeddings = get_embeddings()
        _vectorstore = FAISS.from_texts([text], embeddings)

    return _vectorstore
