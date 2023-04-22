#!/usr/bin/python3

"""This module contains the app instance for the AirBnB Web"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def request_cleanup(exception=None):
    """Removes current Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Lists all states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_filter(id):
    """Get all cities based on a state id"""
    states = storage.all(State)

    for state in states.values():
        if state.id == id:
            states = state
    return render_template('9-states.html', states=states, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
