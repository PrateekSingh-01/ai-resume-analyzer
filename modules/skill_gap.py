def find_missing_skills(resume_skills, job_skills):

    resume_set = set(resume_skills)

    job_set = set(job_skills)

    missing = job_set - resume_set

    return list(missing)