#!/usr/bin/env python3
""" 4. Force locale with URL parameter
"""
from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Gets the best match for supported languages """
    query_lang = request.args.get('locale')
    if query_lang and query_lang in app.config['LANGUAGES']:
        return query_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """ Returns a string at the root route """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
