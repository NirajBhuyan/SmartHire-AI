import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}  # replace with your valid token

def get_semantic_similarity(resume_text, jd_text):
    try:
        payload = {
            "inputs": {
                "source_sentence": resume_text[:500],   # Optional: Trim to reduce size
                "sentences": [jd_text[:500]]
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        print("🔍 HuggingFace response:", response.status_code, response.text)  # Add this line

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and isinstance(result[0], float):
                return round(result[0] * 100, 2)
            else:
                print("⚠️ Unexpected response format:", result)
                return 0.0
        else:
            print("❌ Hugging Face API Error:", response.status_code, response.text)
            return 0.0

    except Exception as e:
        print("❌ Exception in Hugging Face API:", str(e))
        return 0.0
