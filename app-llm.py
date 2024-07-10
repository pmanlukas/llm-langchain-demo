from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-pro")


st.title("ChatGPT-like clone")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        messages = [
            (m["role"], m["content"]) for m in st.session_state.messages
        ]
        
        stream = llm.stream(messages)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})