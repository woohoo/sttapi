import speech_recognition as sr
from os import path
from helpers.filetool import remove_file
from config import AUDIO_PATH


def recognize(file_name):
    """
    Convert audio file to text and deletes file
    :param file_name: name of the audio file e.g. hello.wav
    :return: (result text or error, boolean result of execution)
    """
    audio_file = path.join(AUDIO_PATH, file_name)
    result = True
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as file:
        audio = r.record(file)

    try:
        text = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        result = False
        text = "Audio could not be recognized"
    except sr.RequestError as e:
        result = False
        text = "Recognize server error: {0}".format(e)
    finally:
        remove_file(audio_file)
    return text, result
