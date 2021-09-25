#!/usr/bin/env python3

import os

from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = b'\xbe\x08\xed\x13\xe0\xc4\xf3\x06\x02I\xefp\xebX\xfb.'



def render_form():
    return """
    <!doctype html>
    <html>
        <head><title>UPload new File</title></head>
        <body>
            <form method='POST' enctype='multipart/form-data'>
                <input type='file' name='file' />
                <input type='submit' value='Upload' />
            </form>
        </body>
    </html>
    """



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            app.logger.warning('No file part')
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            app.logger.warning('No selected file')
            flash('No selected file')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        app.logger.warning('A new file uploaded: %s' % filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        app.logger.warning('%s save success' % save_path)

        return redirect(url_for('download_file', name=filename))

    return render_form()
           


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)


def create_app():
    return app

if __name__ == '__main__':
    app.run(port=5000)
