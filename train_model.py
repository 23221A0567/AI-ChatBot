import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

print("================================")
print("Loading Dataset...")
print("================================")

# Load Dataset
data = pd.read_csv("dataset/college_chatbot.csv", encoding="utf-8")

# Clean Data
data.columns = data.columns.str.strip()
data = data.dropna()

print(data.head())

# Questions
questions = data["Question"].astype(str)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

question_vectors = vectorizer.fit_transform(questions)

# Save Files
joblib.dump(vectorizer, "model/vectorizer.pkl")
joblib.dump(question_vectors, "model/question_vectors.pkl")
joblib.dump(data, "model/chat_data.pkl")

print("\n================================")
print("Training Completed Successfully")
print("================================")
print("Saved Files:")
print("✔ vectorizer.pkl")
print("✔ question_vectors.pkl")
print("✔ chat_data.pkl")
print("================================")