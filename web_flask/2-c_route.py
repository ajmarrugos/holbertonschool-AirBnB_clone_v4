#!/usr/bin/python3
"""Python Script that starts a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Allows the root route '/' to return text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_01():
    """Allows the route '/hbnb' to return text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index_02(text):
    """Allows the route '/c/' to return given text inside the page"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
