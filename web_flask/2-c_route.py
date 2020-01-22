#!/usr/bin/python3
""" Script which starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_flask():
    """ Route returning the specified string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Route returning the specified string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_deez(text):
    """ Displays C, then text variable """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
