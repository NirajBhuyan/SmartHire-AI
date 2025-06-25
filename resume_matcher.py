import streamlit as st
from utils.pdf_parser import extract_text_from_pdf

# Define a basic skill list (expand later or use a skill ontology API)
skill_keywords = [
    "python", "machine learning", "data science", "tensorflow", "pytorch",
    "scikit-learn", "nlp", "deep learning", "data analysis", "sql",
    "excel", "power bi", "tableau", "aws", "azure", "communication",
    "problem-solving", "numpy", "pandas", "matplotlib", "statistics"
]

def extract_skills(text):
    text = text.lower()
    return [kw for kw in skill_keywords if kw in text]

def match_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    percent = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0
    return matched, missing, percent

def get_semantic_score(resume_text, jd_text):
    return 0.0  # No heavy model yet
