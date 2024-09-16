from langchain_community.vectorstores import Chroma
from src.embeddings import get_embeddings
def get_vector_store(documents):
    embeddings = get_embeddings()
    return Chroma.from_documents(documents, embeddings)

