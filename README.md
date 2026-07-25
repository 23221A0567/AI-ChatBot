# 🎓 AI Student Chatbot

An AI-powered chatbot developed using **Python, Flask, Machine Learning, and NLP** to answer common student queries related to admissions, courses, fees, hostel, placements, library, and other college-related information.

---

## 📌 Project Overview

The AI Student Chatbot is designed to help students get instant answers to frequently asked questions without manually contacting the college administration.

The chatbot uses Natural Language Processing (NLP) techniques to understand user questions and provide the most relevant response from the dataset.

---

## 🎯 Objectives

- Provide instant answers to student queries.
- Reduce manual workload for the college administration.
- Improve student support using AI.
- Demonstrate the use of Machine Learning and NLP in education.

---

## 🚀 Features

- 🤖 AI-powered chatbot
- 💬 Interactive chat interface
- 🎓 Admission information
- 💰 Fees details
- 🏠 Hostel information
- 📚 Course details
- 💼 Placement information
- 📖 Library information
- 🔍 Smart question matching using NLP
- 🌐 Web-based interface
- 📱 Responsive design

---

## 🛠 Technologies Used

### Programming Language
- Python

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### Libraries
- Pandas
- Joblib
- NumPy

---

## 📂 Project Structure

```
AI_Student_Chatbot
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset
│   └── college_chatbot.csv
│
├── model
│   ├── vectorizer.pkl
│   ├── question_vectors.pkl
│   └── chat_data.pkl
│
├── static
│   ├── style.css
│   └── script.js
│
└── templates
    └── index.html
```

---

## ⚙ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Student_Chatbot.git
```

Move into the project folder

```bash
cd AI_Student_Chatbot
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python train_model.py
```

---

## Run the Project

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Sample Questions

- What is the admission process?
- What is the hostel fee?
- What courses are offered?
- Which companies visit the campus?
- What are the library timings?
- Is there any scholarship?
- What is the placement percentage?

---

## Working

1. User enters a question.
2. The chatbot converts the question into TF-IDF vectors.
3. Cosine Similarity finds the most relevant question from the dataset.
4. The chatbot returns the corresponding answer.
5. The response is displayed on the web interface.

---

## Advantages

- Easy to use
- Fast response
- AI-based FAQ system
- User-friendly interface
- Reduces manual effort
- Easy to update dataset
- Supports educational institutions

---

## Limitations

- Answers only questions available in the dataset.
- Does not access live college databases.
- Does not support multiple languages in the current version.

---

## Future Enhancements

- Voice input support
- Multi-language support
- Student login system
- Database integration
- Chat history
- AI using Large Language Models (LLMs)
- College ERP integration

---

## Applications

- Colleges
- Universities
- Educational Institutions
- Student Help Desk
- Online Admission Support

---

## Author

**Bunny Kunavarapu**

B.Tech – Computer Science and Engineering

Bonam Venkata Chalamayya Engineering College

---

## License

This project is developed for educational and academic purposes.

---

## Acknowledgements

- Flask Documentation
- Scikit-learn Documentation
- Pandas Documentation
- Python Documentation

---

⭐ If you like this project, consider giving it a star on GitHub.