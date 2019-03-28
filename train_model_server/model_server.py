import os
from flask import Flask, flash, request, redirect, render_template,send_file,send_from_directory
from werkzeug.utils import secure_filename
import model
import time


UPLOAD_FOLDER = 'upload_files'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['pickle','csv','tsv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File(s) successfully uploaded')
            flash('Start training new model...')
            model.train_model(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Download New model at http://127.0.0.1:5000/download')
            return redirect('/')
        else:
            flash('False file format')
            return redirect(request.url)



@app.route('/download', methods=['POST'])
def index():
    response = send_from_directory(directory='model', filename='model.h5',as_attachment=True)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
