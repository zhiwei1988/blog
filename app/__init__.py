# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
