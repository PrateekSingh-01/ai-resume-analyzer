import streamlit as st
import pandas as pd

from modules.parser import extract_text_from_pdf
from modules.preprocessing import clean_text
from modules.skill_extractor import load_skills, extract_skills
from modules.similarity import calculate_similarity
from modules.skill_gap import find_missing_skills
from modules.suggestions import generate_suggestions
from modules.role_predictor import predict_role
from modules.resume_score import calculate_resume_score, get_rating


st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description.")


# Upload resume
resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_desc = st.text_area("Paste Job Description")


# Default variables
detected_skills = []


if resume:

    # -----------------------------
    # Resume Processing
    # -----------------------------
    raw_text = extract_text_from_pdf(resume)
    cleaned_text = clean_text(raw_text)

    skills_list = load_skills()
    detected_skills = extract_skills(cleaned_text, skills_list)

    st.divider()

    # -----------------------------
    # Skills Section (2 Columns)
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Detected Skills")

        if detected_skills:
            for skill in detected_skills:
                st.write(f"✔ {skill}")
        else:
            st.info("No skills detected.")

    with col2:
        st.subheader("Skill Visualization")

        if detected_skills:
            skill_df = pd.DataFrame(detected_skills, columns=["Skill"])
            skill_counts = skill_df.groupby("Skill").size().reset_index(name="Count")

            st.bar_chart(skill_counts.set_index("Skill"))
        else:
            st.info("No skills available for visualization.")

    st.divider()

    # -----------------------------
    # Role Prediction
    # -----------------------------
    st.subheader("Predicted Job Role")

    skill_text = " ".join(detected_skills)

    predicted_role = predict_role(skill_text)

    st.write(f"💼 {predicted_role}")

    st.divider()

    # -----------------------------
    # Job Description Analysis
    # -----------------------------
    if job_desc:

        job_skills = extract_skills(job_desc, skills_list)

        missing_skills = find_missing_skills(detected_skills, job_skills)

        st.subheader("Missing Skills for this Job")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"❌ {skill}")
        else:
            st.success("Your resume already contains the required skills!")

        # -----------------------------
        # ATS Score
        # -----------------------------
        score = calculate_similarity(cleaned_text, job_desc)

        st.subheader("ATS Match Score")

        st.progress(score / 100)

        st.write(f"{score}% match with job description")

        st.divider()

        # -----------------------------
        # Suggestions
        # -----------------------------
        suggestions = generate_suggestions(missing_skills)

        st.subheader("Suggestions to Improve Resume")

        if suggestions:
            for s in suggestions:
                st.write(f"• {s}")
        else:
            st.success("No major improvements needed.")

        # -----------------------------
        # Resume Strength Score
        # -----------------------------
        resume_score = calculate_resume_score(score, detected_skills)

        rating = get_rating(resume_score)

        st.subheader("Resume Strength Score")

        st.progress(resume_score / 100)

        st.write(f"{resume_score} / 100")

        st.write(rating)

    else:
        st.info("Paste a job description to see ATS score and resume evaluation.")


else:
    st.info("Upload a resume to start analysis.")