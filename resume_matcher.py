from utils.pdf_parser import extract_text_from_pdf

import spacy
import spacy.cli

from sentence_transformers import SentenceTransformer, util

# Download spaCy model (safe on Streamlit)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load BERT model only once
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Paths to the uploaded files
resume_path = "data/resume.pdf"
jd_path = "data/job_description.pdf"

# Extracted text
resume_text = extract_text_from_pdf(resume_path)
jd_text = extract_text_from_pdf(jd_path)

# Preview Output
print("✅ Resume Sample:\n", resume_text[:500], "\n")
print("✅ Job Description Sample:\n", jd_text[:500])


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

# Extract skills from resume and JD
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

# Match analysis
matched_skills = list(set(resume_skills) & set(jd_skills))
missing_skills = list(set(jd_skills) - set(resume_skills))
match_percent = round(len(matched_skills) / len(jd_skills) * 100, 2) if jd_skills else 0

# Output
print("\n✅ Extracted Resume Skills:", resume_skills)
print("✅ Extracted JD Skills:", jd_skills)
print("✅ Matched Skills:", matched_skills)
print("⚠️ Missing Skills:", missing_skills)
print(f"📊 Match Score: {match_percent}%")



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
