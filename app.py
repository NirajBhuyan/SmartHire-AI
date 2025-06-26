import streamlit as st
import os
import pandas as pd
from logger import log_results
from utils.pdf_parser import extract_text
from huggingface_api import get_semantic_similarity
import traceback

try:
    from resume_matcher import extract_skills, match_skills
except Exception as e:
    st.error("❌ Failed to import resume_matcher")
    st.text(traceback.format_exc())

import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SmartHire AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .title-text {
            font-size:40px !important;
            font-weight:700;
            color: #4CAF50;
            font-family: 'Segoe UI', sans-serif;
        }
        .subheader-text {
            font-size:22px !important;
            color: #333333;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🤖 SmartHire AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader-text'>AI-powered Resume Matcher & Career Recommender</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📂 Resume Matcher", "📊 Match History"])

with tab1:
    resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
    jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

    if resume_file and jd_file:
        try:
            resume_ext = resume_file.name.split('.')[-1].lower()
            jd_ext = jd_file.name.split('.')[-1].lower()

            resume_path = f"temp_resume.{resume_ext}"
            jd_path = f"temp_jd.{jd_ext}"

            with open(resume_path, "wb") as f:
                f.write(resume_file.read())
            with open(jd_path, "wb") as f:
                f.write(jd_file.read())

            resume_text = extract_text(resume_path)
            jd_text = extract_text(jd_path)
            st.success("✅ Resume Extracted")
            st.success("✅ JD Extracted")

            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)
            matched_skills, missing_skills, match_percent = match_skills(resume_skills, jd_skills)
            match_percent = round(match_percent, 2)
            semantic_score = round(get_semantic_similarity(resume_text, jd_text), 2)
            #st.metric("Semantic Similarity", f"{semantic_score}%")

            log_results(match_percent, semantic_score, matched_skills, missing_skills) 

            st.markdown("## 🧠 Analysis Results")
            col1, col2 = st.columns(2)
            col1.metric("Skill Match %", f"{match_percent:.2f}%")
            col2.metric("Semantic Similarity", f"{semantic_score: .2f}%")
            
            with st.expander("📄 View Extracted Resume Text"):
                st.text(resume_text)

            with st.expander("🎯 Matched & Missing Skills"):
                st.markdown(f"**Matched Skills:** {', '.join(matched_skills) or 'None'}")
                st.markdown(f"**Missing Skills:** {', '.join(missing_skills) or 'None'}")

            fig1, ax1 = plt.subplots()
            ax1.pie([len(matched_skills), len(missing_skills)], labels=['Matched', 'Missing'],
                    colors=['#4CAF50', '#FF5722'], autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            st.pyplot(fig1)

            fig2, ax2 = plt.subplots()
            ax2.bar(['Resume Skills', 'JD Skills', 'Matched'], 
                    [len(resume_skills), len(jd_skills), len(matched_skills)],
                    color=['#2196F3', '#9C27B0', '#4CAF50'])
            st.pyplot(fig2)

        except Exception as e:
            st.error("❌ Error during processing:")
            st.exception(e)
            st.text(traceback.format_exc())
            st.stop()

with tab2:
    if not os.path.exists("output"):
        os.makedirs("output")
    
    st.markdown("## 📋 Match History Log")
    
    if os.path.exists("output/match_log.csv"):
        log_df = pd.read_csv("output/match_log.csv")
        st.dataframe(log_df)
    else:
        st.info("No logs found. Upload a resume to see results here.")
