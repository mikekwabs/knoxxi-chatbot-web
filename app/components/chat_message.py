import streamlit as st
import textwrap

def message(role, content, is_dark=False):
    """Render a chat message with Markdown formatting inside styled bubbles."""

    if role == "user":
        bubble_color = "#2b6cb0" if is_dark else "#DCF8C6"
        text_color = "#f8f9fa" if is_dark else "#000000"
        label = "You:"
    else:
        bubble_color = "#2d2d2d" if is_dark else "#F1F0F0"
        text_color = "#f8f9fa" if is_dark else "#000000"
        label = "MedGemma:"

    # Wrap text inside an HTML container for padding but allow Markdown rendering
    st.markdown(
        f"""
        <div style="
            background-color:{bubble_color};
            color:{text_color};
            padding:12px;
            border-radius:10px;
            margin:6px 0;
        ">
        <b>{label}</b><br>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Render the message text separately — so Markdown (bold, italic, lists, etc.) works
    st.markdown(content, unsafe_allow_html=False)
