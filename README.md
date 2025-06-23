
# 🤖 SmartHire AI

**SmartHire AI** is an AI-powered Resume Matcher and Career Recommendation tool built with Streamlit.  
It analyzes your resume against job descriptions, matches skills, calculates semantic relevance, and offers career-enhancing insights.

---

## 🚀 Features

- 📄 Upload Resume (PDF/DOCX) & Job Description
- ✅ Extract skills and keywords from both documents
- 🎯 Highlight Matched and Missing Skills
- 🤖 Semantic Similarity using BERT embeddings
- 📊 Visual charts (Pie & Bar) for skill insights
- 📥 CSV Log of all analysis results
- ☁️ Deployed with Streamlit Cloud

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for UI
- **PDFPlumber / python-docx** for file parsing
- **Scikit-learn / SentenceTransformers** for AI logic
- **Pandas / Matplotlib** for logging & visualization

---

## 📁 Folder Structure

```
SmartHire-AI/
├── app.py                      # Main Streamlit App
├── resume_matcher.py          # Skill Matching Logic
├── logger.py                  # CSV Logger
├── utils/
│   └── pdf_parser.py          # Resume/Job parsing
├── output/
│   └── match_log.csv          # Auto-generated analysis logs
├── .streamlit/
│   └── config.toml            # Custom Theme
├── requirements.txt           # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/SmartHire-AI.git
cd SmartHire-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🙌 Credits

Developed by [Niraj Pratim Bhuyan](https://github.com/NirajBhuyan)  
Built with ❤️ using Streamlit + AI

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)
