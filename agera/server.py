# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.cors import CORS

from agera.apps import api

from agera.settings import (
    DEBUG,
    SECRET_KEY,
)


def init_others(app):
    pass


def init_config(app):
    app.config.update({
        "PERMANENT_SESSION_LIFETIME": 60*15,
        "SESSION_REFRESH_EACH_REQUEST": True,
    })

    app.debug = DEBUG
    app.secret_key = SECRET_KEY


def init_module(app):
    api.init(app)


def create_app():
    app = Flask(__name__)
    init_others(app)
    init_config(app)
    init_module(app)
    return app


app = create_app()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7300)
