#!/usr/bin/python3
"""WSGI flask script to display “Hello HBNB!”"""
from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/')
def index():
    """a method to return hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
