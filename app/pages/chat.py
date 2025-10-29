import streamlit as st
from components.chat_message import message
from components.utils import send_message


def chat_ui():
    st.title("💬 Knoxxi Chatbot")
    st.caption("Describe, analyze, and interpret images using MedGemma 4B")

    # Initialize state
    if "history" not in st.session_state:
        st.session_state["history"] = []

    # --- Display existing history once ---
    # for msg in st.session_state["history"]:
    #     message(msg["role"], msg["content"])

        st.markdown("""
    <style>
    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        padding-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state["history"]:
        message(msg["role"], msg["content"])
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Input area ---
    user_input = st.chat_input("Type your question or instruction here...")
    image_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

    if user_input:
        # Append user input to history first (for persistence)
        st.session_state["history"].append({"role": "user", "content": user_input})

        # Render it immediately
        message("user", user_input)

        # Placeholder for MedGemma response
        with st.spinner("Thinking..."):
            try:
                result = send_message(user_input, image_file, 0.7, 2048)
                response_text = result["text"]

                # Append assistant response to history
                st.session_state["history"].append({"role": "assistant", "content": response_text})

                # Render single MedGemma response card
                message("assistant", response_text)
                st.caption(f"🕓 {result['latency']:.2f}s | {result['model']}")

            except Exception as e:
                st.error(f"Error: {e}")
