#!/usr/bin/env python3
""" 1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """ Returns a string at the root route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
