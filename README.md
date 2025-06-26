# 🤖 SmartHire-AI
SmartHire-AI is a real-time AI-powered web application that analyzes resumes and job descriptions to calculate skill match percentage and semantic similarity. It helps job seekers and recruiters assess compatibility between candidate profiles and job requirements using Natural Language Processing (NLP).

## 🚀 Features

- 📄 Upload Resume (PDF/DOCX)
- 📝 Upload Job Description (PDF/DOCX)
- ✅ Extracts raw text from both documents
- 🧠 Calculates:
  - **Skill Match Percentage**
  - **Semantic Similarity Score** using transformer-based embeddings
- 📊 Visualizes results via pie charts and bar graphs
- 📁 Match History Logging to CSV
- 🌐 Deployed using [Streamlit Cloud](https://streamlit.io/cloud)

## 🧠 NLP & AI Stack

- **Hugging Face Transformers**
  - Model used: [`paraphrase-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2)
  - Library: [`sentence-transformers`](https://www.sbert.net/)
  - Purpose: Computes semantic similarity between resume and job description using sentence embeddings.

- **spaCy** (optional/local usage)
  - For keyword-based skill extraction

- **Matplotlib & Pandas**: For visualization and match history logging

## 🛠 Tech Stack

- Python 3.8+
- Streamlit
- Hugging Face Transformers (`sentence-transformers`)
- Pandas, Matplotlib
- pdfplumber, python-docx

## 📦 Setup Instructions

```bash
git clone https://github.com/your-username/SmartHire-AI.git
cd SmartHire-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🧪 Sample Files

- Sample Resume: `Resume test.docx`
- Sample JD: `JD test.docx`


## 👨‍💻 Author

- **Niraj Pratim Bhuyan**  
  [LinkedIn](https://www.linkedin.com/in/yourprofile) | [GitHub](https://github.com/NirajBhuyan)
