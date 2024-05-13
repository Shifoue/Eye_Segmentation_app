import os
import io
from PIL import Image
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename
from base64 import b64encode

from backend.AI import AI_process

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

HOST="0.0.0.0"
PORT=5000

AI = AI_process()

app = Flask(__name__)

def create_img_url(image):
    image_io = io.BytesIO()
    image.save(image_io, 'PNG')
    dataurl = 'data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii')

    return dataurl

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
            origin_image = Image.open(file)

            predicted_mask = AI.process(origin_image)

            origin_img_url = create_img_url(origin_image)
            predicted_mask_img_url = create_img_url(predicted_mask[0])

            #return redirect(url_for('download_file', name=filename))
            return render_template('image.html', image_data=origin_img_url)
        
    return render_template("upload.html")
 
if __name__ == '__main__':
    app.run(HOST, port=PORT, ssl_context="adhoc")