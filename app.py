import streamlit as st
from langchain_community.document_loaders import TextLoader
from src.rag import RAGChatbot
import os
from src.ui_components import display_chat_message, display_relevant_documents
def load_documents():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "data", "texte.txt")
        print(f"Attempting to load file from: {file_path}")
        
        if os.path.exists(file_path):
            print(f"File exists. Size: {os.path.getsize(file_path)} bytes")
        else:
            print("File does not exist!")
            return []

        loader = TextLoader(file_path)
        documents = loader.load()
        print(f"Successfully loaded {len(documents)} documents")
        return documents
    except Exception as e:
        print(f"Error loading documents: {str(e)}")
        return []
def main():
    st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")
    st.title("🤖 RAG Chatbot")  
    if 'chatbot' not in st.session_state:
        documents = load_documents()
        st.session_state.chatbot = RAGChatbot(documents)
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        display_chat_message(message["role"], message["content"])
    if prompt := st.chat_input("Ask a question:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        display_chat_message("user", prompt)  
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.get_response(prompt)
            relevant_docs = st.session_state.chatbot.get_relevant_documents(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        display_chat_message("assistant", response)
        display_relevant_documents(relevant_docs)  
    st.sidebar.title("About")
    st.sidebar.info("This chatbot uses RAG (Retrieval-Augmented Generation) "
         "to provide informative responses based on the loaded documents. "
        "It uses Gemini 1.5 as the language model and Jina AI embeddings."
    )

                
if __name__ == "__main__":
    main()
