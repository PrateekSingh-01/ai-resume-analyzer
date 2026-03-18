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


if resume:

    # -----------------------------
    # Resume Processing
    # -----------------------------

    raw_text = extract_text_from_pdf(resume)
    cleaned_text = clean_text(raw_text)

    skills_list = load_skills()
    detected_skills = extract_skills(cleaned_text, skills_list)


    # -----------------------------
    # Detected Skills
    # -----------------------------

    st.subheader("Detected Skills")

    for skill in detected_skills:
        st.write(f"✔ {skill}")


    # -----------------------------
    # Skill Visualization
    # -----------------------------

    st.subheader("Skill Visualization")

    skill_df = pd.DataFrame(detected_skills, columns=["Skill"])

    skill_counts = skill_df.groupby("Skill").size().reset_index(name="Count")

    st.bar_chart(skill_counts.set_index("Skill"))


    # -----------------------------
    # Role Prediction
    # -----------------------------

    st.subheader("Predicted Job Role")

    skill_text = " ".join(detected_skills)

    predicted_role = predict_role(skill_text)

    st.write(f"💼 {predicted_role}")


    # -----------------------------
    # Job Description Analysis
    # -----------------------------

    if job_desc:

        job_skills = extract_skills(job_desc, skills_list)

        missing_skills = find_missing_skills(detected_skills, job_skills)

        st.subheader("Missing Skills for this Job")

        st.write(missing_skills)


        # -----------------------------
        # ATS Score
        # -----------------------------

        score = calculate_similarity(cleaned_text, job_desc)

        st.subheader("ATS Match Score")

        st.progress(score / 100)

        st.write(f"{score}% match with job description")


        # -----------------------------
        # Resume Suggestions
        # -----------------------------

        suggestions = generate_suggestions(missing_skills)

        st.subheader("Suggestions to Improve Resume")

        for s in suggestions:
            st.write(f"• {s}")


        # -----------------------------
        # Resume Strength Score
        # -----------------------------

        resume_score = calculate_resume_score(score, detected_skills)

        rating = get_rating(resume_score)

        st.subheader("Resume Strength Score")

        st.write(f"{resume_score} / 100")

        st.write(rating)

        if resume_score >= 80:
          st.success("Excellent resume for this role!")
        elif resume_score >= 60:
          st.info("Good resume, but there is room for improvement.")
        else:
          st.warning("Your resume needs improvement for this role.")