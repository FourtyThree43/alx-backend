# alx-backend

- [0x02. i18n](#0x02-i18n)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Environment](#environment)
- [Files Descriptions](#files-descriptions)


## 0x02. i18n
* This repo is for learning about i18n (internationalization) and how to implement it in Python.

### Resources
* [Flask-Babel](https://flask-babel.tkte.ch/)
* [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
* [pytz](http://pytz.sourceforge.net/)
* [Flask-BabelEx](https://pythonhosted.org/Flask-BabelEx/)
* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)
* [Flask-Babel with Jinja2](https://pythonhosted.org/Flask-Babel/#jinja2-extension)

### Learning Objectives
* Learn how to parametrize Flask templates to display different languages
	**Parametrizing Flask Templates for Different Languages**: This involves using variables in Flask templates that will be filled with text in the appropriate language. The specific language can be determined by various methods such as user settings or URL parameters. Flask uses Jinja2 templating, and you can use placeholders for your text like `{{ text }}` which will be replaced with the actual text when rendering the template.

* Learn how to infer the correct locale based on URL parameters, user settings or request headers
	**Inferring Correct Locale**: This is about determining the user's preferred language. This can be done in several ways:
    	- **URL Parameters**: The preferred language can be specified as a parameter in the URL. For example, `www.example.com/en` for English or `www.example.com/fr` for French.
    	- **User Settings**: If users have a profile where they can set their preferred language, this setting can be used to determine the locale.
    	- **Request Headers**: Web browsers include an `Accept-Language` header in HTTP requests which can be used to infer the locale.

* Learn how to localize timestamps
	**Localizing Timestamps**: This refers to displaying timestamps according to the local conventions of the user's locale, including the date format and timezone. Python provides libraries like `pytz` and `babel` that can be used to localize timestamps.

### Environment
* Language: Python 3.7.5
* OS: Ubuntu 18.04 LTS
* Framework: Flask 1.1.1
* Framework: Babel 2.0.0
* Template: Jinja2 2.10.3
* Style guidelines: PEP 8 (version 1.7) for Python 3.5


### Files Descriptions
* 0-app.py - a basic Flask app that has a single `/` route and a single `templates/0-index.html`
* 1-app.py - a basic Flask app that has a single `/` route and a single `templates/1-index.html`
* 2-app.py - a basic Flask app that has a single `/` route and a single `templates/2-index.html`
* 3-app.py - a basic Flask app that has a single `/` route and a single `templates/3-index.html` translated to [`en`|`fr`]

* 4-app.py - a basic Flask app that has a single `/` route and a single `templates/4-index.html` ttranslated to `fr` with `locale` in URL
* 5-app.py - a basic Flask app that has a single `/` route and a single `templates/5-index.html` translated to `en` or `fr` with `locale` in URL parameter `locale` with User mock login and `get_user` function
* 6-app.py - a basic Flask app that has a single `/` route and a single `templates/6-index.html` translated to `en` or `fr` with `locale` in URL parameter `locale` with User mock login and `get_user` function and `get_locale` function
* 7-app.py - a basic Flask app that has a single `/` route and a single `templates/7-index.html` translated to `en` or `fr` with `locale` in URL parameter `locale` with User mock login and `get_user` function and `get_locale` function and `babel.timezoneselector` decorator
