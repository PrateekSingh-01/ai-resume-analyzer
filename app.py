import streamlit as st

from modules.parser import extract_text_from_pdf
from modules.preprocessing import clean_text
from modules.skill_extractor import load_skills, extract_skills
from modules.similarity import calculate_similarity
from modules.skill_gap import find_missing_skills
from modules.suggestions import generate_suggestions


st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description.")

# Upload resume
resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_desc = st.text_area("Paste Job Description")


if resume:

    # Step 1: Extract text from resume
    raw_text = extract_text_from_pdf(resume)

    # Step 2: Clean the text
    cleaned_text = clean_text(raw_text)

    # Step 3: Load skill database
    skills_list = load_skills()

    # Step 4: Detect skills in resume
    detected_skills = extract_skills(cleaned_text, skills_list)

    st.subheader("Detected Skills")
    st.write(detected_skills)


    # Only run these steps if job description is provided
    if job_desc:

        # Step 5: Extract job skills
        job_skills = extract_skills(job_desc, skills_list)

        # Step 6: Find missing skills
        missing_skills = find_missing_skills(detected_skills, job_skills)

        st.subheader("Missing Skills for this Job")
        st.write(missing_skills)

        # Step 7: Calculate ATS match score
        score = calculate_similarity(cleaned_text, job_desc)

        st.subheader("ATS Match Score")
        st.write(f"{score}%")

        # Step 8: Generate suggestions
        suggestions = generate_suggestions(missing_skills)

        st.subheader("Suggestions to Improve Resume")

        for s in suggestions:
            st.write(f"• {s}")