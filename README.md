# 🤖 AI Resume & Job Matcher

An AI-powered web application that analyzes a resume against a job description and calculates how well the candidate matches the position.

## 🚀 Features

- Upload and analyze resumes
- Extract important skills from resumes
- Analyze job descriptions
- Calculate an AI-powered resume/job similarity score
- Identify matching skills
- Identify missing skills
- Generate personalized recommendations
- Simple interactive Streamlit interface

## 🧠 How It Works

1. User uploads a resume.
2. The application extracts the resume text.
3. User provides a job description.
4. AI analyzes the similarity between the resume and job description.
5. The system identifies required skills.
6. Matching and missing skills are displayed.
7. The application provides recommendations to improve the resume.

## 🛠️ Technologies

- Python
- Streamlit
- Scikit-learn
- Sentence Transformers
- PyPDF2
- Pandas
- Natural Language Processing (NLP)
- Git & GitHub

## 📊 AI Matching

The application uses a Sentence Transformer model to convert resume and job-description text into numerical embeddings.

Cosine similarity is then used to calculate the similarity between the resume and job description.

## 📁 Project Structure

```text
AI-Resume-Job-Matcher/
│
├── app.py
├── matcher.py
├── recommendations.py
├── skills.py
├── .gitignore
├── README.md
└── venv/