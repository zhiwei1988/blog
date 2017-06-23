# -*- coding=utf-8 -*-

from datetime import datetime
from . import db, login_manager
from markdown import markdown
import bleach
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, index=True, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
                                                       tags=allowed_tags, strip=True))


db.event.listen(Post.body, 'set', Post.on_changed_body)


class User(UserMixin, db.Model):
    '''
    Flask-SQLAlchemy 要求每个模型都要定义主键，这一列经常命名为 id
    UserMixin类帮助实现flask-login要求必须实现的几个用户函数
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    _password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('passwod is not a readable attribute')

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    '''
    flask-login 要求实现的回调函数，使用指定的标识符加载用户
    :param user_id:
    :return:
    '''
    return User.query.get(int(user_id))


