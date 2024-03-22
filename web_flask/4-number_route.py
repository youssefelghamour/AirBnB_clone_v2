#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ function for / route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ function for /hbnb route """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ function for /c/<text> route """
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text=None):
    """ function for /python/<text> route """
    if text is None:
        text = "is cool"
    text = text.replace('_', ' ')
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ function for /number/<n> route """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
