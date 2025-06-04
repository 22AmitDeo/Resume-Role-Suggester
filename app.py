import flask 
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['resume']
        text = extract_text(file)
        # (Do scoring...)
        return render_template('results.html', matches=matches)
    return render_template('upload.html')
