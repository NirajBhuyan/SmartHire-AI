import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HEADERS = {"Authorization": "Bearer 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"}  # Make sure this is valid

def get_semantic_similarity(resume_text, jd_text):
    try:
        print("📡 Sending request to HuggingFace API...")

        payload = {
            "inputs": {
                "source_sentence": resume_text,
                "sentences": [jd_text]
            }
        }

        # Ensure resume_text and jd_text are strings
        if not resume_text.strip() or not jd_text.strip():
            print("❌ Empty text for resume or JD.")
            return 0.0

        # Send POST request
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        print(f"📥 API Response Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✅ HuggingFace Response JSON:", result)

            # Validate response content
            if isinstance(result, list) and len(result) > 0 and isinstance(result[0], float):
                return round(result[0] * 100, 2)
            else:
                print("⚠️ Unexpected response format:", result)
                return 0.0
        else:
            print(f"⚠️ API Error: {response.status_code} - {response.text}")
            return 0.0

    except Exception as e:
        print("❌ Exception in get_semantic_similarity:", str(e))
        return 0.0
