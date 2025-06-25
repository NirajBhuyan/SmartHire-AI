import streamlit as st
st.write("📦 Entered resume_matcher.py")

from utils.pdf_parser import extract_text_from_pdf

import spacy
import spacy.cli
import importlib.util
from sentence_transformers import SentenceTransformer, util

st.write("🔄 Checking spaCy model...")

# Download spaCy model (safe on Streamlit)

try:
    nlp = spacy.load("en_core_web_sm")
    st.success("✅ spaCy model loaded")
except OSError:
  #  import subprocess
  #  subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
  #  nlp = spacy.load("en_core_web_sm")
  #  st.success("✅ spaCy model loaded successfully")
    st.error("❌ spaCy model not found! Please manually add 'en_core_web_sm' to requirements.txt")
    st.stop()  # Prevent app from running further

#try:
#    if not spacy.util.is_package("en_core_web_sm"):
#        spacy.cli.download("en_core_web_sm")
#        print("✅ spaCy model downloaded (if needed)")
#    nlp = spacy.load("en_core_web_sm")
#    print("✅ spaCy model loaded")
#except Exception as e:
#    st.error("❌ Failed to load spaCy model")
#    st.text(str(e))

# Load BERT model only once
st.write("🔄 Loading BERT model...")
try:
    bert_model = SentenceTransformer('all-MiniLM-L6-v2')
    st.success("✅ BERT model loaded")
except Exception as e:
    st.error("❌ Failed to load BERT model")
    st.text(str(e))

# Define a basic skill list (expand later or use a skill ontology API)
skill_keywords = [
    "python", "machine learning", "data science", "tensorflow", "pytorch",
    "scikit-learn", "nlp", "deep learning", "data analysis", "sql",
    "excel", "power bi", "tableau", "aws", "azure", "communication",
    "problem-solving", "numpy", "pandas", "matplotlib", "statistics"
]
def extract_skills(text):
    doc = nlp(text.lower())
    extracted = set()
    for token in doc:
        if token.text in skill_keywords:
            extracted.add(token.text)
    return list(extracted)

def match_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    percent = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0
    return matched, missing, percent

def get_semantic_score(resume_text, jd_text):
    try:
        resume_emb = bert_model.encode(resume_text, convert_to_tensor=True)
        jd_emb = bert_model.encode(jd_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(resume_emb, jd_emb)
        return round(float(score.item()) * 100, 2)
    except Exception as e:
        print(f"Error calculating semantic score: {e}")
        return 0.0
