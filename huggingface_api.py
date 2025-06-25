import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}

def get_semantic_similarity(resume_text, jd_text):
    try:
        print("📡 Calling HuggingFace API...")
        payload = {
            "inputs": {
                "source_sentence": resume_text,
                "sentences": [jd_text]
            }
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        print(f"✅ Response received: {response.status_code}")

        if response.status_code == 200:
            score = response.json()[0]  # It should return a list with a float value
            print("✅ Response JSON:", data)
            return round(score * 100, 2)
        else:
            print("⚠️ API returned error:", response.status_code, response.text)
            return 0.0
    except Exception as e:
        print("Exception in get_semantic_similarity:", str(e))
        return 0.0
