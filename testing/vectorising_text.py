from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "Data analyst with skills in Python, SQL, and Power BI"
job_descs = [
    "Looking for data analyst proficient in Python and Power BI",
    "Hiring a software developer with Java and Spring skills",
]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume] + job_descs)

# Calculate similarity of resume with each job description
cosine_similarities = cosine_similarity(vectors[0:1], vectors[1:])

# Print similarity scores
for i, score in enumerate(cosine_similarities[0]):
    print(f"Similarity with Job {i+1}: {score:.2f}")
