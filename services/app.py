import os
import io
from PIL import Image
import base64
from base64 import b64encode
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename

from backend.AI import AI_process

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

HOST="0.0.0.0"
PORT=5000

AI = AI_process()

app = Flask(__name__)

def create_img_url(image, extension="JPEG"):
    # image_io = io.BytesIO()
    # image.save(image_io, 'PNG')
    # dataurl = 'data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii')
    # image_io.seek(0)

    buffered = io.BytesIO()
    image.save(buffered, format=extension)
    buffered.seek(0)
    img_str = base64.b64encode(buffered.getvalue())
    img_jpg = img_str.decode('utf-8')

    return img_jpg

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('home')) #render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/technical_explanation')
def technical_explanation():
    return render_template('technical_explanation.html')
 
@app.route('/demonstration', methods=['GET', 'POST'])
def demonstration():
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
            origin_image = Image.open(file).convert('RGB')

            predicted_mask = AI.process(origin_image)

            origin_img_jpg = create_img_url(origin_image)
            predicted_mask_img_jpg = create_img_url(predicted_mask)

            return render_template('demonstration.html', origin_image_data=origin_img_jpg, mask_image_data=predicted_mask_img_jpg)
        
    return render_template("demonstration.html")
 
if __name__ == '__main__':
    app.run(HOST, port=PORT, ssl_context="adhoc")