import streamlit as st
from pathlib import Path
from utils import load_css

st.set_page_config(page_title="Saichandar Rao Uppuganti", layout="wide")

PAGES = {
    "Home": "Profile.py",
    "About": "pages/1_About.py",
    "Experience": "pages/2_Experience.py",
    "Projects": "pages/3_Projects.py",
    "Skills": "pages/4_Skills.py",
    "Resume": "pages/5_Resume.py",
    "Contact": "pages/6_Contact.py",
}

# Always-visible navigation
selected = st.radio(
    "Navigation",
    list(PAGES.keys()),
    horizontal=True
)

# Redirect to selected page
st.switch_page(PAGES[selected])

st.set_page_config(
    page_title="Saichandar Rao Uppuganti | Portfolio",
    page_icon="📄",
    layout="wide"
)

# Load custom CSS
load_css()

# ---------- HERO SECTION ----------
colA, colB = st.columns([1.6, 1])

with colA:
    st.markdown("## Saichandar Rao Uppuganti")
    st.caption("Data Scientist | Healthcare Claims Auditing | LLM & ML | SQL | AWS/Azure")

    st.write(
        "Data Scientist with experience in healthcare claims auditing, "
        "building machine learning and LLM-based solutions to improve audit accuracy, "
        "reduce review time, and enable data-driven decisions. "
        "Strong in SQL development, ETL pipelines (SSIS/Python), and cloud (AWS/Azure)."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("LinkedIn", "https://linkedin.com/in/uppuganti")
    with c2:
        st.link_button("GitHub", "https://github.com/yourusername")  # change this
    with c3:
        st.link_button("Email", "mailto:uppuganti2000@gmail.com")

    st.markdown("### Core Focus")

    # Use CSS pill class instead of inline styling
    st.markdown('<span class="pill">LLM / GPT Solutions</span>', unsafe_allow_html=True)
    st.markdown('<span class="pill">Healthcare Claims Auditing</span>', unsafe_allow_html=True)
    st.markdown('<span class="pill">ML Model Training & Validation</span>', unsafe_allow_html=True)
    st.markdown('<span class="pill">SQL / T-SQL / Optimization</span>', unsafe_allow_html=True)
    st.markdown('<span class="pill">ETL: SSIS + Python</span>', unsafe_allow_html=True)
    st.markdown('<span class="pill">AWS / Azure</span>', unsafe_allow_html=True)

    resume_path = Path("assets/resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            st.download_button("Download Resume (PDF)", f, file_name="Saichandar_Resume.pdf")

with colB:
    img_path = Path("assets/profile.jpg")
    if img_path.exists():
        st.image(str(img_path), use_container_width=True)
    else:
        st.markdown('<div class="card">Add your photo at assets/profile.jpg</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------- FEATURED WORK ----------
st.markdown("## Featured Work")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
      <h3>AI-Driven Claims Auditing</h3>
      <p>End-to-end pipeline for document extraction, validation, and classification.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
      <h3>BERT Document Classifier</h3>
      <p>Categorized claim documents before audit processing; improved accuracy.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
      <h3>Healthcare Data Dashboard</h3>
      <p>Power BI + SQL + SSIS pipeline to track data breaches and reporting KPIs.</p>
    </div>

    """, unsafe_allow_html=True)
