def calculate_resume_score(ats_score, detected_skills):

    skill_score = min(len(detected_skills) * 5, 50)

    total_score = (ats_score * 0.5) + skill_score

    total_score = min(int(total_score), 100)

    return total_score


def get_rating(score):

    if score >= 90:
        return "⭐⭐⭐⭐⭐ Excellent Resume"
    elif score >= 70:
        return "⭐⭐⭐⭐ Strong Resume"
    elif score >= 50:
        return "⭐⭐⭐ Average Resume"
    elif score >= 30:
        return "⭐⭐ Needs Improvement"
    else:
        return "⭐ Weak Resume"