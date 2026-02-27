import streamlit as st
from pathlib import Path

st.title("Resume")

resume_path = Path("assets/resume.pdf")

if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.download_button("Download Resume", f, file_name="Saichandar_Resume.pdf")

    st.info("Tip: Streamlit cannot reliably embed PDFs on all devices. Download button is the most stable.")
else:
    st.warning("Add your resume at assets/resume.pdf")