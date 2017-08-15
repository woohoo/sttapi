from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from recognizer import recognize
from helpers.make_result import make_error, make_success
from helpers.filetool import allowed_file_extension
from config import apply_flask_config
from os import path

app = Flask(__name__)
apply_flask_config(app)


@app.route('/recognize', methods=['POST'])
def upload():
    """
    Handles /recognize endpoint
    Checks that we got proper file, process it
    and return json result to client
    :return:
    """
    if 'file' not in request.files:
        return make_error("Cannot find file")
    file = request.files['file']
    if file.filename == '':
        return make_error("No selected file")

    if file and allowed_file_extension(file.filename):
        filename = secure_filename(file.filename)
        file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        text, result = recognize(filename)
        return make_success(text) if result else make_error(text)


# DO NOT run Flask like this in production. Use uWSGI + nginx
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )