from flask import Flask, render_template, request, send_file
from converter import convert_pdf_to_docx, convert_docx_to_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['pdf_file']
    converted_file = convert_pdf_to_docx(uploaded_file)
    return send_file(converted_file, as_attachment=True)

@app.route('/convert_word', methods=['POST'])
def convert_word():
    uploaded_file = request.files['word_file']
    converted_file = convert_docx_to_pdf(uploaded_file)
    return send_file(converted_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
