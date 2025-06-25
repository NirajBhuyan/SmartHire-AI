import requests
import streamlit as st

def get_semantic_similarity(text1, text2):
    token = st.secrets["huggingface"]["api_token"]
    api_url = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "inputs": {
            "source_sentence": text1,
            "sentences": [text2]
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        score = response.json()[0]
        return round(score * 100, 2)
    else:
        print(f"Error from HuggingFace API: {response.status_code}, {response.text}")
        return 0.0
