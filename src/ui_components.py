def display_chat_message(role, content):
    with st.chat_message(role):
        st.markdown(content) 
def display_relevant_documents(documents):
    with st.expander("Relevant Documents"):
        for i, doc in enumerate(documents):
            st.markdown(f"**Document {i + 1}:**")
            st.text(doc.page_content[:200] + "...")
            st.markdown("---") 