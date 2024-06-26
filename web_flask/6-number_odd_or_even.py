#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBnB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    """ Return text in python page"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Return number page"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Return number template page"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Return text in page number"""
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_or_even="even" if n % 2 == 0 else "odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
