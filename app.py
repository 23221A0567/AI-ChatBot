from flask import Flask, render_template, request, jsonify
import joblib

from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ==========================
# Load Files
# ==========================

vectorizer = joblib.load("model/vectorizer.pkl")
question_vectors = joblib.load("model/question_vectors.pkl")
chat_data = joblib.load("model/chat_data.pkl")


# ==========================
# Home
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Chat API
# ==========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "").strip()

    if user_message == "":
        return jsonify({
            "reply": "Please enter your question."
        })

    # Greetings

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if user_message.lower() in greetings:

        return jsonify({
            "reply":
            "Hello 👋<br><br>Welcome to AI Student Chatbot.<br><br>How can I help you today?"
        })

    # ==========================
    # Convert User Question
    # ==========================

    user_vector = vectorizer.transform([user_message])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    confidence = similarity[0][best_match]

    print("-----------------------------------")
    print("Question :", user_message)
    print("Confidence :", confidence)
    print("-----------------------------------")

    # Unknown Question

    if confidence < 0.35:

        return jsonify({
            "reply":
            """
Sorry 😔<br><br>

I couldn't understand your question.<br><br>

Please ask about:<br>

✅ Admissions<br>
✅ Courses<br>
✅ Fees<br>
✅ Hostel<br>
✅ Placements<br>
✅ Library<br>
✅ Scholarships
"""
        })

    answer = chat_data.iloc[best_match]["Answer"]

    return jsonify({
        "reply": answer
    })


# ==========================

if __name__ == "__main__":
    app.run(debug=True)