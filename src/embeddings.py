import os
import requests
from langchain.embeddings.base import Embeddings
class JinaAIEmbeddings(Embeddings):
    def __init__(self):
        self.api_url ="https://api-inference.huggingface.co/models/jinaai/jina-embeddings-v2-base-en"
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}
    def embed_documents(self, texts):
        payload = {"inputs": texts}
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.json()
    def embed_query(self, text):
        return self.embed_documents([text])[0]

def get_embeddings():
    return JinaAIEmbeddings()