import streamlit as st
import os

# -----------------------------
# Page Config (IMPORTANT)
# -----------------------------
st.set_page_config(
    page_title="Saichandar Rao Uppuganti",
    layout="wide",
    initial_sidebar_state="expanded"   # starts opened by default
)

# -----------------------------
# Load CSS (if you have style.css)
# -----------------------------
CSS_FILE = "style.css"
if os.path.exists(CSS_FILE):
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar Open Helper (Always visible on page)
# -----------------------------
st.info("✅ If the left menu (sidebar) is hidden, click the small **`>`** arrow on the far left to open it again.")

# -----------------------------
# Main Content
# -----------------------------
# Paths (update if needed)
PROFILE_IMG = "assets/profile.jpg"  # keep image inside assets/profile.jpg

name = "Saichandar Rao Uppuganti"
tagline = "Data Scientist | Healthcare Claims Auditing | LLM & ML | SQL | AWS/Azure"
summary = (
    "Data Scientist with experience in healthcare claims auditing, building machine learning and LLM-based "
    "solutions to improve audit accuracy, reduce review time, and enable data-driven decisions. Strong in SQL "
    "development, ETL pipelines (SSIS/Python), and cloud (AWS/Azure)."
)

# Top layout: text (left) + image (right)
left, right = st.columns([2, 1])

with left:
    st.markdown(f"<h1 style='margin-bottom: 0px;'>{name}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top: 6px; font-size: 16px; opacity: 0.9;'>{tagline}</p>", unsafe_allow_html=True)
    st.write(summary)

    # Buttons row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("LinkedIn", "https://www.linkedin.com/")
    with c2:
        st.link_button("GitHub", "https://github.com/")
    with c3:
        st.link_button("Email", "mailto:yourname@email.com")

    st.markdown("## Core Focus")

    # Simple "pill" style using markdown (works with/without CSS)
    st.markdown(
        """
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <div style="padding:10px 14px; border-radius:18px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12);">
                LLM / GPT Solutions
            </div>
            <div style="padding:10px 14px; border-radius:18px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12);">
                Healthcare Claims Auditing
            </div>
            <div style="padding:10px 14px; border-radius:18px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12);">
                ML Model Training & Validation
            </div>
            <div style="padding:10px 14px; border-radius:18px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12);">
                SQL / T-SQL / Optimization
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    if os.path.exists(PROFILE_IMG):
        st.image(PROFILE_IMG, use_container_width=True)
    else:
        st.warning("Profile image not found. Put your photo at: **assets/profile.jpg**")

# Footer note
st.caption("Use the left sidebar to navigate: About • Experience • Projects • Skills • Resume • Contact")
