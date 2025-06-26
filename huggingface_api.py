from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the model once
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def get_semantic_similarity(resume_text, jd_text):
    try:
        # Optional: Trim long text
        resume_text = resume_text[:500]
        jd_text = jd_text[:500]

        # Encode to embeddings
        embeddings = model.encode([resume_text, jd_text])
        score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

        return round(score * 100, 2)

    except Exception as e:
        print("❌ Local model error:", str(e))
        return 0.0
