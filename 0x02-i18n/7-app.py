#!/usr/bin/env python3
""" 7. Infer appropriate time zone
"""
from typing import Any, Dict, Optional, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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
users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
    },
}


def get_user() -> Any:
    """ Returns a user dictionary or None if the ID cannot be found """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """ Finds a user if any, and set it as a global on flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Determines the best match with our supported languages """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone() -> Union[str, None]:
    """ Determines the best match with our supported timezones """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """ Returns a string at the root route """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
