import requests
import os

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN', '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')}"
}

def get_semantic_similarity(resume_text, jd_text):
    try:
        if not resume_text.strip() or not jd_text.strip():
            return 0.0

        payload = {
            "inputs": {
                "source_sentence": resume_text,
                "sentences": [jd_text]
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and isinstance(result[0], float):
                return round(result[0] * 100, 2)
            else:
                print("⚠️ Unexpected format:", result)
                return 0.0
        else:
            print(f"❌ Hugging Face API Error: {response.status_code} - {response.text}")
            return 0.0

    except Exception as e:
        print("❌ Exception in get_semantic_similarity:", str(e))
        return 0.0
