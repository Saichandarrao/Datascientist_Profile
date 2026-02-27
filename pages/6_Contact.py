import streamlit as st
from utils import load_css
load_css()

st.title("Contact")

st.write("📧 Email: uppuganti2000@gmail.com")
st.write("🔗 LinkedIn: https://linkedin.com/in/uppuganti")
st.write("💻 GitHub: https://github.com/yourusername")  # change this

st.divider()

st.subheader("Message (Demo Form)")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit")

if submit:
    st.success("Thanks! This is a demo form (it doesn’t send email yet).")