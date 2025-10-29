import streamlit as st

def message(role, content):
    if role == "user":
        st.markdown(
            f"""
            <div style="background-color:#DCF8C6;padding:10px;border-radius:10px;margin:5px 0;">
            <b>You:</b><br>{content}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background-color:#F1F0F0;padding:10px;border-radius:10px;margin:5px 0;">
            <b>MedGemma:</b><br>{content}
            </div>
            """,
            unsafe_allow_html=True
        )
