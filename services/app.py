import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename

from backend.AI import AI_process

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

HOST="0.0.0.0"
PORT=5000

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predicted_mask = AI.process(file)

            return redirect(url_for('download_file', name=filename))
        
    return render_template("upload.html")
 
if __name__ == '__main__':
    app.run(HOST, port=PORT, ssl_context="adhoc")

    AI = AI_process()