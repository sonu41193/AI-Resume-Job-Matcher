import re

#Skills that system can recognize

SKILLS = ["python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "streamlit",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "google cloud",
    "generative ai",
    "large language models",
    "llm",
    "nlp",
    "natural language processing",
    "computer vision",
    "opencv",
    "statistics",
    "excel",
    "power bi",
    "tableau",
    "api",
    "flask",
    "django",

] 

def extract_skills(text):
    text = text.lower()

    found_skills = []
    
    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern,text):
            found_skills.append(skill)

    return sorted(found_skills)
