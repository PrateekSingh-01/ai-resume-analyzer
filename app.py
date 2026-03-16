import streamlit as st
from modules.parser import extract_text_from_pdf
from modules.preprocessing import clean_text
from modules.skill_extractor import load_skills, extract_skills

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume (PDF)")

if resume:

    skills_list = load_skills()

    raw_text = extract_text_from_pdf(resume)

    cleaned_text = clean_text(raw_text)

    detected_skills = extract_skills(cleaned_text, skills_list)

    st.subheader("Detected Skills")

    st.write(detected_skills)

    raw_text = extract_text_from_pdf(resume)

    cleaned_text = clean_text(raw_text)

    st.subheader("Extracted Resume Text")

    st.write(cleaned_text[:1000])