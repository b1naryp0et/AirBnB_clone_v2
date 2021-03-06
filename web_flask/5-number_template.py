#!/usr/bin/python3
""" Script which starts a Flask web application """

from flask import Flask, render_template
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


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def py_text(text):
    """ Returns python, then text string """
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def check_num(n):
    """ Displays text upon int """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def rend_temp(n):
    """ Display template """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
