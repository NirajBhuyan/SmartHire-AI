import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}  # your actual token

def get_semantic_similarity(resume_text, jd_text):
    try:
        payload = {
            "inputs": {
                "source_sentence": resume_text[:500],  # Optional trimming
                "sentences": [jd_text[:500]]
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        # 👇 Print full raw response
        print("🔍 Response Code:", response.status_code)
        print("🔍 Raw Response Text:", response.text)

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and isinstance(result[0], float):
                return round(result[0] * 100, 2)
            else:
                print("⚠️ Unexpected response format:", result)
                return 0.0
        else:
            print("❌ API Error:", response.status_code, response.text)
            return 0.0

    except Exception as e:
        print("❌ Exception:", str(e))
        return 0.0
