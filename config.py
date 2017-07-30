# -*- coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "i love jiang wei nan"

    # 每次请求结束后自动提交数据库变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 默认值为True，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 开启调试模式，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}