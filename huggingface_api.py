# huggingface_api.py
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}  # replace with your valid token

def get_semantic_similarity(resume_text, jd_text):
    try:
        payload = {
            "inputs": {
                "source_sentence": resume_text,
                "sentences": [jd_text]
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            result = response.json()
            score = result[0] if isinstance(result, list) else 0.0
            return round(score * 100, 2)
        else:
            print("❌ Hugging Face API Error:", response.status_code, response.text)
            return 0.0

    except Exception as e:
        print("❌ Exception in Hugging Face API:", str(e))
        return 0.0
