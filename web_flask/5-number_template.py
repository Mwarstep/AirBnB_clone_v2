#!/usr/bin/python3
"""Starts a Flask Web App listening on 0.0.0.0 port 5000
Routes:
    /: will display “Hello HBNB!”
    /hbnb: will display “HBNB”
    /c/<text>: will display “C ”, followed by <text>
    /python/(<text>): will display “Python ”, followed by <text>
    /number/<n>: will display "n is a number" if n is an integer
    /number_template/<n>: will display a HTML page in n is an integer
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Will display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Will display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Will display 'C' followed by <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Will display 'Python' followed by <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Will Display 'n is a number' if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Will Display HTML Page if n is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
