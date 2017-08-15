from flask import jsonify


def make_error(text):
    """
    makes json like response that handles error
    :param text: error text
    :return: json string
    """
    res = {
        "text": text,
        "success": False
    }
    return jsonify(res)


def make_success(text):
    """
    makes json like response that handles success result
    :param text: execution result
    :return: json string
    """
    res = {
        "text": text,
        "success": True
    }
    return jsonify(res)
