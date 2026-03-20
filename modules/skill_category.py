def categorize_skills(skills):

    categories = {
        "AI / Machine Learning": [
            "machine learning", "deep learning", "tensorflow", "pytorch",
            "nlp", "scikit", "ai"
        ],
        "Data Science": [
            "pandas", "numpy", "data", "statistics"
        ],
        "Backend Development": [
            "java", "spring", "flask", "fastapi", "api"
        ],
        "DevOps": [
            "docker", "kubernetes", "aws", "linux", "git"
        ],
        "Frontend": [
            "html", "css", "javascript", "react"
        ]
    }

    category_count = {}

    for category, keywords in categories.items():
        count = 0

        for skill in skills:
            skill = skill.lower().strip()

            for keyword in keywords:
                if keyword in skill or skill in keyword:
                    count += 1
                    break

        if count > 0:
            category_count[category] = count

    return category_count