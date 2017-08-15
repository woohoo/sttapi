# Speech-To-Text API

Simple API that provide possibility to upload audio file and get recognized text

### Prerequisites

If you really want to try this you need virtualenv and swig to build sphinx recognizer.
If you want to add functionality look at SpeechRecognition library for Python

To install swig on MacOS:
```
brew install swig
```

To install virtualenv
```
pip install virtualenv
```
### Installing

First, clone this project to directory, ex 'my-project'

```
cd my-project 
virtualenv venv
. venv/bin/activate
pip install Flask
pip install --upgrade pocketsphinx
deactivate
```

### Running

```
. venv/bin/activate
python app.py
```

## What can do next

* API Access by tokens
* Fallback to another providers (thanks to SpeechRecognition library)
* Fine tune recognition lib
* Idea: try recognize audio with several libs => check with some grammatic lib and chooses best result
* Make callback endpoint => suitable for large files
