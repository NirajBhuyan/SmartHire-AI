import streamlit as st
import os
import pandas as pd
from logger import log_results
#import logging

#from recommendations import recommend_skills
from utils.pdf_parser import extract_text

try:
    from resume_matcher import extract_skills, match_skills
    #,get_semantic_score
except Exception as e:
    import traceback
    st.error("❌ Failed to import resume_matcher")
    st.text(traceback.format_exc())

import matplotlib.pyplot as plt

# ✅ Logging setup
#logging.basicConfig(level=logging.DEBUG)
#st.write("📋 Logging started...")
#logging.debug("✅ Checkpoint: App started")

st.set_page_config(
    page_title="SmartHire AI",
    layout="centered",  # modern wide layout
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
            # Save uploaded files temporarily
            resume_ext = resume_file.name.split('.')[-1].lower()
            jd_ext = jd_file.name.split('.')[-1].lower()

            resume_path = f"temp_resume.{resume_ext}"
            jd_path = f"temp_jd.{jd_ext}"

            with open(resume_path, "wb") as f:
                f.write(resume_file.read())
            with open(jd_path, "wb") as f:
                f.write(jd_file.read())

            # Text Extraction
            resume_text = extract_text(resume_path)
            jd_text = extract_text(jd_path)
            st.success("✅ Resume Extracted")
            #st.text(resume_text[:300])  # show preview
            st.success("✅ JD Extracted")
            #st.text(jd_text[:300])

            # Skill Matching
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)
            matched_skills, missing_skills, match_percent = match_skills(resume_skills, jd_skills)
            #semantic_score = get_semantic_score(resume_text, jd_text)
            #st.write("✅ Checkpoint 11: Skills matched and semantic score calculated")

            log_results(match_percent, semantic_score, matched_skills, missing_skills)
            #st.write("✅ Checkpoint 12: Results logged")

            # 📊 Metrics
            st.markdown("## 🧠 Analysis Results")
            col1, col2 = st.columns(2)
            col1.metric("Skill Match %", f"{match_percent}%")
            col2.metric("Semantic Similarity", f"{semantic_score}%")

            # Expanders
            with st.expander("📄 View Extracted Resume Text"):
                st.text(resume_text)

            with st.expander("🎯 Matched & Missing Skills"):
                st.markdown(f"**Matched Skills:** {', '.join(matched_skills) or 'None'}")
                st.markdown(f"**Missing Skills:** {', '.join(missing_skills) or 'None'}")

            # Charts
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
            st.error(f"❌ Error during processing: {e}")
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


