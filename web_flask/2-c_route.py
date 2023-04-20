#!/usr/bin/python3

"""This is a module that contains the flask app instance"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Renders the index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Renders the hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')

    return "C %s" % text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
