import streamlit as st
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Saichandar Rao Uppuganti",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS (if exists)
# -----------------------------
if os.path.exists("style.css"):
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation (Multi-page style)
# -----------------------------


# -----------------------------
# Main Content
# -----------------------------
PROFILE_IMG = "assets/profile.jpg"

name = "Saichandar Rao Uppuganti"
tagline = "Data Scientist | Healthcare Claims Auditing | LLM & ML | SQL | AWS/Azure"
summary = (
    "Data Scientist with experience in healthcare claims auditing, building machine learning "
    "and LLM-based solutions to improve audit accuracy, reduce review time, and enable data-driven "
    "decisions. Strong in SQL development, ETL pipelines (SSIS/Python), and cloud (AWS/Azure)."
)

left, right = st.columns([2, 1])

with left:
    st.markdown(f"<h1 style='margin-bottom:0;'>{name}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top:8px; opacity:0.85;'>{tagline}</p>", unsafe_allow_html=True)
    st.write(summary)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("LinkedIn", "https://www.linkedin.com/")
    with c2:
        st.link_button("GitHub", "https://github.com/saichandarrao")
    with c3:
        st.link_button("Email", "mailto:uppuganti2000@gmail.com")

    st.markdown("## Core Focus")

    st.markdown(
        """
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <div style="padding:10px 16px; border-radius:18px; background:rgba(255,255,255,0.08);">
                LLM / GPT Solutions
            </div>
            <div style="padding:10px 16px; border-radius:18px; background:rgba(255,255,255,0.08);">
                Healthcare Claims Auditing
            </div>
            <div style="padding:10px 16px; border-radius:18px; background:rgba(255,255,255,0.08);">
                ML Model Training & Validation
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    if os.path.exists(PROFILE_IMG):
        st.image(PROFILE_IMG, use_container_width=True)
    else:
        st.warning("Add your image at assets/profile.jpg")

# -----------------------------
# ✅ UPDATED FEATURES SECTION (AI / Work / Automation)
# -----------------------------
st.markdown("---")
st.markdown("## Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("🤖 AI / LLM Involvement")
    st.caption(
        "Worked on LLM-based solutions like document understanding, extraction, summarization, "
        "and automation to improve productivity and accuracy."
    )

with f2:
    st.markdown("📊 Real-world Workflows")
    st.caption(
        "Built end-to-end data workflows for healthcare claims auditing, data analysis, SQL reporting, "
        "and identifying duplicate/retro patterns."
    )

with f3:
    st.markdown("⚙️ Automation & ETL Pipelines")
    st.caption(
        "Developed automation pipelines using Python/SSIS, validations, logging, and job scheduling "
        "to support production-ready systems."
    )


