import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Plataforma de Evaluaciones — SCE + CEG",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar menú y footer de Streamlit para pantalla limpia
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "prototype" / "index.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=900, scrolling=True)
