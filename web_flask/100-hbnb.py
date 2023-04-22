#!/usr/bin/python3

"""This module contains the app instance for the AirBnB Web"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.teardown_appcontext
def request_cleanup(exception=None):
    """Removes current Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display hbnb page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return Markup(render_template('100-hbnb.html', states=states, amenities=amenities, places=places))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
