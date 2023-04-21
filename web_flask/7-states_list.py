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

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Lists all states"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
