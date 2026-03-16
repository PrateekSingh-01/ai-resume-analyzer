import streamlit as st
from modules.parser import extract_text_from_pdf

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume (PDF)")

if resume:

    text = extract_text_from_pdf(resume)

    st.subheader("Extracted Resume Text")

    st.write(text[:1000])