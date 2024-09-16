from langchain.chains import RetrievalQA
from src.vector_store import get_vector_store
from src.llm import get_llm
class RAGChatbot:
    def __init__(self, documents):
        self.vector_store = get_vector_store(documents)
        self.llm = get_llm()
        self.qa_chain = RetrievalQA.from_chain_type(
        llm=self.llm,
        chain_type="stuff",
        retriever=self.vector_store.as_retriever()
    )
def get_response(self, query):
    return self.qa_chain.run(query)

def get_relevant_documents(self, query):
    return self.vector_store.similarity_search(query)    