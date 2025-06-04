import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_roles(resume_text, job_roles_path="job_roles.csv", top_n=3):
    """
    Compute similarity between resume and job roles.
    Returns top N matches as (role, score) tuples.
    """
    try:
        df = pd.read_csv(job_roles_path)
        job_roles = df['role'].tolist()
        job_skills = df['skills'].tolist()

        # Resume + job skill text corpus
        documents = [resume_text] + job_skills

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Cosine similarity: resume vs all job roles
        similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        # Pair roles with scores and return sorted
        matches = sorted(zip(job_roles, similarity_scores), key=lambda x: x[1], reverse=True)
        return matches[:top_n]
    except Exception as e:
        print(f"[Error] Matching failed: {e}")
        return []
