import streamlit as st
from utils import load_css
load_css()
st.title("Professional Experience")

st.subheader("Medintelx — Data Scientist (Aug 2025 – Present)")
st.caption("Python • Transformers • Prompt Engineering • OCR (Tesseract) • Streamlit • SQL • SSIS • Azure")
st.write("- Designed and implemented an end-to-end AI-driven claims auditing system reducing manual review effort by **30–40%**.")
st.write("- Built Python pipeline to process scanned/electronic PDFs using OCR + preprocessing for improved extraction accuracy.")
st.write("- Developed BERT-based document classification model to categorize claim documents before audit processing.")
st.write("- Improved document classification accuracy to ~**90%** through fine-tuning on labeled datasets.")
st.write("- Implemented structured prompt engineering (few-shot prompting, JSON schema constraints) to improve consistency and reduce hallucinations.")
st.write("- Added logging, retries, and validation layers for production-grade reliability.")
st.write("- Built AI-driven SQL function generation tool using GPT to speed up developer productivity.")

st.divider()

st.subheader("Svastha Infotech — AWS SQL Developer (Feb 2025 – Jul 2025)")
st.caption("SQL • SSIS • SSMS • SSRS • AWS • T-SQL • C# • MSBI")
st.write("- Wrote complex SQL queries, stored procedures, triggers, views, and indexes using DDL/DML.")
st.write("- Tuned query performance using execution plans and indexing strategies.")
st.write("- Performed normalization/de-normalization to improve query performance.")
st.write("- Built SSIS packages to import/export data from CSV/flat files/Excel into SQL Server.")
st.write("- Designed SSRS reports (matrix, tabular, charts) for analytics delivery.")
st.write("- Supported SQL Server migration (2019 → 2022) and ensured stable operations.")

st.divider()

st.subheader("Movate — Cloud Engineer (Jul 2022 – Nov 2022)")
st.caption("AWS • EC2 • S3 • EBS • IAM • GitLab • Python • CloudFormation • Docker/Kubernetes")
st.write("- Worked with core AWS services including EC2, S3, EBS, IAM and monitoring using CloudWatch.")
st.write("- Assisted infrastructure automation using IaC tools (Terraform/CloudFormation).")
st.write("- Supported EC2/EBS operations, VPC/security group activities, and troubleshooting.")
st.write("- Contributed to containerized deployments and reliability monitoring workflows.")