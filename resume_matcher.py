import spacy
import spacy.cli
from sentence_transformers import SentenceTransformer, util

# Download spaCy model (safe on Streamlit)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load SentenceTransformer model once
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Skill keywords (expand as needed)
skill_keywords = [
    "python", "machine learning", "data science", "tensorflow", "pytorch",
    "scikit-learn", "nlp", "deep learning", "data analysis", "sql",
    "excel", "power bi", "tableau", "aws", "azure", "communication",
    "problem-solving", "numpy", "pandas", "matplotlib", "statistics"
]

def extract_skills(text):
    """Extract skills from input text using predefined keywords."""
    doc = nlp(text.lower())
    extracted = set()
    for token in doc:
        if token.text in skill_keywords:
            extracted.add(token.text)
    return list(extracted)

def match_skills(resume_skills, jd_skills):
    """Compare skills and return matched, missing, and percentage match."""
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    percent = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0
    return matched, missing, percent

def get_semantic_score(resume_text, jd_text):
    """Use BERT embeddings to calculate semantic similarity."""
    try:
        resume_emb = bert_model.encode(resume_text, convert_to_tensor=True)
        jd_emb = bert_model.encode(jd_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(resume_emb, jd_emb)
        return round(float(score.item()) * 100, 2)
    except Exception as e:
        print(f"Error calculating semantic score: {e}")
        return 0.0
