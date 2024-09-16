from langchain.document_loaders import TextLoader, PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.txt'):
            loader = TextLoader(file_path)
            documents.extend(loader.load())
        elif filename.endswith('.pdf'):
            loader = PDFPlumberLoader(file_path)
            documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(documents)
    return split_docs