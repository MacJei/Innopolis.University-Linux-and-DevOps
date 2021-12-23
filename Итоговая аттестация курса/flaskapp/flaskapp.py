"""Создать веб-приложение используя flask"""
from flask_login import login_user, login_required, logout_user
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_autoindex import AutoIndex
from flask import Flask, render_template, request, send_file
import os


UPLOAD_FOLDER = 'directory'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

files_index = AutoIndex(app, os.path.abspath(UPLOAD_FOLDER),
                        add_url_rules=False)

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin")
}

full_path = os.path.abspath(UPLOAD_FOLDER)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/files', methods=['GET'])
def autoindex(path=full_path):
    if request.method == 'GET':
        return files_index.render_autoindex(path)


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return "Privet, %s!" % auth.current_user()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html')

@app.route('/upload')
@auth.login_required
def show_upload_page():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
@auth.login_required
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        with open(os.path.join(UPLOAD_FOLDER, f.filename), "wb") as fp:
            fp.write(request.data)
        return 'file uploaded successfully'


@app.route("/files/<path:path>")
@auth.login_required
def download_file(path):
    return send_file(os.path.join(full_path, path), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
