import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/paraphrase-MiniLM-L6-v2"
HEADERS = {
    "Authorization": "Bearer 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",  # ✅ Replace with your valid token
    "Content-Type": "application/json"
}

def get_semantic_similarity(resume_text, jd_text):
    try:
        def get_embedding(text):
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
            print("🔍 API Response Code:", response.status_code)
            print("🔍 API Response Body:", response.text)
            if response.status_code == 200:
                return np.mean(response.json(), axis=0)
            else:
                return None

        resume_vec = get_embedding(resume_text[:512])
        jd_vec = get_embedding(jd_text[:512])

        if resume_vec is not None and jd_vec is not None:
            similarity = cosine_similarity([resume_vec], [jd_vec])[0][0]
            return round(similarity * 100, 2)
        else:
            return 0.0
    except Exception as e:
        print("❌ Semantic Similarity Error:", str(e))
        return 0.0
