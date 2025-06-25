import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}

def get_semantic_similarity(resume_text, jd_text):
    try:
        if not resume_text.strip() or not jd_text.strip():
            print("❌ Empty resume or JD text.")
            return 0.0

        payload = {
            "inputs": {
                "source_sentence": resume_text,
                "sentences": [jd_text]
            }
        }

        res = requests.post(API_URL, headers=HEADERS, json=payload)

        if res.status_code == 200:
            result = res.json()
            if isinstance(result, list) and isinstance(result[0], float):
                return round(result[0] * 100, 2)
            else:
                print("⚠️ Unexpected format:", result)
                return 0.0
        else:
            print(f"❌ API Error {res.status_code}: {res.text}")
            return 0.0

    except Exception as e:
        print(f"❌ Exception in HuggingFace API: {str(e)}")
        return 0.0
