#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """ displays a HTML page with a list of states """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', list_states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """ closes the current session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
