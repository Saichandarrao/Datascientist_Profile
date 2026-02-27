import streamlit as st
from utils import load_css
load_css()

st.title("About Me")

st.write(
    "I’m a Data Scientist specializing in healthcare claims auditing and AI-driven automation. "
    "I build LLM/ML solutions to extract and classify documents, improve audit accuracy, "
    "and reduce manual review time. I also have strong experience in SQL development and ETL."
)

st.markdown("### Highlights")
st.write("- Built end-to-end AI claims auditing system reducing manual review effort by **30–40%**.")
st.write("- Developed **OCR (Tesseract)** + preprocessing pipeline for scanned/electronic PDFs.")
st.write("- Built **BERT-based document classification** and improved accuracy to ~**90%**.")
st.write("- Strong SQL performance tuning, indexing, and audit-traceability design.")
st.write("- Comfortable with AWS/Azure and Agile practices.")