#!/usr/bin/env python3

from flask import Flask, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def home():
    greeting = _("Hello, World!")
    return greeting

if __name__ == '__main__':
    app.run(debug=True)
