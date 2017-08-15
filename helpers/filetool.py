import os
from config import ALLOWED_EXTENSIONS


def remove_file(path):
    """
    Remove file if exists
    :param path - full path to file
    """
    try:
        os.remove(path)
    except OSError:
        pass


def allowed_file_extension(filename):
    """
    Checks that file extension in allowed set
    :param filename: name of file e.g. hello.wav
    :return: boolean result
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS