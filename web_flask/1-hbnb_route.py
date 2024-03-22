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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
