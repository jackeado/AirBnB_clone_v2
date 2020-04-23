#!/usr/bin/python3
"""Minimal flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route index"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def enroute():
    """Route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ Route /c """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoncool(text):
    """ Route Python"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Route Number"""
    return "%d is a number" % n


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
