import streamlit as st

def render_sidebar():
    #st.sidebar.image("app/assets/logo.png", width=180)
    st.sidebar.title("⚙️ Settings")

    temperature = st.sidebar.slider("Temperature", 0.1, 1.5, 0.7, 0.1)
    max_tokens = st.sidebar.slider("Max Tokens", 64, 512, 256, 8)

    st.sidebar.markdown("---")
    st.sidebar.caption("💡 Adjust temperature for creativity.")
    return temperature, max_tokens
