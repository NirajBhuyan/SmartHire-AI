# logger.py

import pandas as pd
from datetime import datetime
import os

def log_results(match_percent, semantic_score, matched_skills, missing_skills, file_path='output/match_log.csv'):
    # Create log directory if not exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Prepare data
    data = {
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Match %": [match_percent],
        "Semantic Score": [semantic_score],
        "Matched Skills": [", ".join(matched_skills)],
        "Missing Skills": [", ".join(missing_skills)]
    }

    df = pd.DataFrame(data)

    # Append to existing file or create new
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)
