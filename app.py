import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from utils.parser import extract_resume_text
from utils.nlp_processing import clean_text
from utils.matcher import match_roles

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file part", 400
        file = request.files['resume']
        if file.filename == '':
            return "No selected file", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Extract + clean resume text
            raw_text = extract_resume_text(filepath)
            cleaned_text = clean_text(raw_text)

            # Match roles
            matches = match_roles(cleaned_text)

            return render_template('results.html', matches=matches)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
