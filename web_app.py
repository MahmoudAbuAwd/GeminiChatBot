import streamlit as st
from datetime import datetime
import json
from chatbot.gemini_chatbot import GeminiChatbot

def initialize_session_state():
    if 'chatbot' not in st.session_state:
        try:
            st.session_state.chatbot = GeminiChatbot()
            st.session_state.messages = []
        except ValueError as e:
            st.error(f"Configuration Error: {str(e)}")
            st.stop()

def main():
    st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
    initialize_session_state()
    
    st.title("🤖 Mahmoud Chatbot")
    
    # Chat interface
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ask about Mahmoud AbuAwd..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.send_message(prompt)
                st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()