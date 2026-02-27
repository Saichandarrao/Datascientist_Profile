import streamlit as st
from utils import load_css
load_css()

st.title("Projects")

st.subheader("Healthcare Data Breach Visualization Dashboard (Mar 2023 – May 2024)")
st.caption("SSIS • SQL Server • Power BI • Reporting • ETL Automation")
st.write("- Built an end-to-end analysis solution to track healthcare data breaches using real datasets.")
st.write("- Cleaned data in Excel and built SSIS pipelines to load into SQL Server.")
st.write("- Created optimized stored procedures and indexed tables for performance.")
st.write("- Automated refresh + scheduling using SQL Server Agent.")
st.write("- Built interactive Power BI dashboard to show breach trends by type, location, and frequency.")