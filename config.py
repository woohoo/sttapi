from os import path

# Directory to store audio files while processing
AUDIO_PATH = path.join(path.dirname(path.realpath(__file__)), "audio")

# Let maximum allowed file size will be 10 Mb
MAX_CONTENT_LENGTH = 10 * 1024 * 1024

# allowed extensions for processing files
ALLOWED_EXTENSIONS = set(['wav'])


def apply_flask_config(app):
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
    app.config['UPLOAD_FOLDER'] = AUDIO_PATH
