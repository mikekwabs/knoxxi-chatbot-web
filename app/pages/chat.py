import streamlit as st
from components.chat_message import message
from components.sidebar import render_sidebar
from components.utils import send_message

def chat_ui():
    st.title("💬 Knoxxi Chatbot")
    st.caption("Describe, analyze, and interpret images using MedGemma 4B")

    if "history" not in st.session_state:
        st.session_state["history"] = []

    temperature, max_tokens = render_sidebar()

    user_input = st.chat_input("Type your question or instruction here...")
    image_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

    if user_input:
        # Display user message
        st.session_state["history"].append({"role": "user", "content": user_input})
        message("user", user_input)

        with st.spinner("Thinking..."):
            try:
                result = send_message(user_input, image_file, temperature, max_tokens)
                st.session_state["history"].append({"role": "assistant", "content": result["text"]})
                message("assistant", result["text"])
                st.caption(f"🕓 {result['latency']:.2f}s | {result['model']}")
            except Exception as e:
                st.error(f"Error: {e}")

    # Display chat history
    for msg in st.session_state["history"]:
        message(msg["role"], msg["content"])
