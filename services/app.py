import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from flask_talisman import Talisman
from werkzeug.utils import secure_filename

from backend.AI import AI_process

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

HOST="0.0.0.0"

app = Flask(__name__)
talisman = Talisman(app)

# Content Security Policy (CSP) Header
csp = {
    'default-src': [
        '\'self\'',
        'https://code.jquery.com',
        'https://cdn.jsdelivr.net'
    ]
}
# HTTP Strict Transport Security (HSTS) Header
hsts = {
    'max-age': 31536000,
    'includeSubDomains': True
}

# Enforce HTTPS and other headers
talisman.force_https = True
talisman.force_file_save = True
talisman.x_xss_protection = True
talisman.session_cookie_secure = True
talisman.session_cookie_samesite = 'Lax'
talisman.frame_options_allow_from = 'https://www.google.com'
 
# Add the headers to Talisman
talisman.content_security_policy = csp
talisman.strict_transport_security = hsts

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
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #predicted_mask = AI.process(file)

            return redirect(url_for('download_file', name=filename))
        
    return render_template("upload.html")
 
if __name__ == '__main__':
    app.run(HOST, port=5000)

    #AI = AI_process()