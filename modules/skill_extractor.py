import pandas as pd

def load_skills():

    skills = pd.read_csv("data/skills.csv")

    return skills["skill"].str.lower().tolist()


def extract_skills(text, skills_list):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))