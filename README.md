# 🎯 Interactive Resume Analyzer for Job Fit

A Flask-based web application that analyzes PDF resumes and matches them to the most relevant job roles using NLP and cosine similarity on TF-IDF vectors.

---

## 🧰 Tech Stack

- **Backend**: Python, Flask  
- **NLP**: spaCy, scikit-learn, TF-IDF, cosine similarity  
- **PDF Parsing**: pdfminer.six  
- **Frontend**: HTML, CSS (Flask templates)  
- **Others**: Pandas, Git

---

## 📸 Demo

> Upload your resume → Get top job role matches with match scores

---

## 🚀 Features

- 📄 Upload a PDF resume
- 🧠 Extracts and cleans text using spaCy
- 🧮 Compares your resume to predefined job role skillsets
- 📊 Shows top matching job roles with confidence scores
- ✅ Easy to extend (add more roles or integrate GPT/LLMs)

---

## 🔧 How to Run Locally

```bash
git clone https://github.com/22AmitDeo/resume-analyzer.git
cd resume-analyzer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

python app.py
```
Then open your browser and go to: http://127.0.0.1:5000/

---

## 📁 Project Structure

```
resume-analyzer/
├── app.py
├── job_roles.csv
├── requirements.txt
├── utils/
│   ├── parser.py
│   ├── nlp_processing.py
│   └── matcher.py
├── uploads/
├── static/
│   └── plot.png
└── templates/
    ├── upload.html
    └── results.html
```

---
## 📌 Future Improvements

- Use OpenAI or LLMs to parse resumes contextually
- Add visualization (bar chart of match scores)
- Extend to recommend missing skills

---

## 🧑‍💻 Author

**Amit Kumar Deo**  
📧 [amitkumardeo95@gmail.com](mailto:amitkumardeo95@gmail.com)  
🔗 [GitHub](https://github.com/22AmitDeo) • [Portfolio](https://www.datascienceportfol.io/amitkumardeo95)

