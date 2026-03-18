from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Small training dataset
training_data = [
    ("python machine learning tensorflow deep learning", "Machine Learning Engineer"),
    ("data analysis pandas numpy visualization statistics", "Data Scientist"),
    ("html css javascript react frontend ui", "Frontend Developer"),
    ("java spring backend api microservices", "Backend Developer"),
    ("aws docker kubernetes devops ci cd", "DevOps Engineer"),
]

texts = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)


def predict_role(resume_text):

    vector = vectorizer.transform([resume_text])

    prediction = model.predict(vector)

    return prediction[0]