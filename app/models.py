# -*- coding=utf-8 -*-

from datetime import datetime
from . import db, login_manager
from markdown import markdown
import bleach
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# 要在两张表之间建立多对多的关系，需要引入第3张表，这个表称为关联表
# 通过 assignations 可以将 posts 与 tags 间的多对多关系分解为两者跟与 assignations 之间的一对多关系
# 关联表就是一个简单的表，不是模型，SQLAlchemy 会自动接管这个表
assignations = db.Table('assignations',
                        db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                        db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                        )


class Post(db.Model):
    # 类变量 __tablename__ 定义在数据库中使用的表名。 如果没有定义 __tablename__ ， Flask-SQLAlchemy 会使用一个默认名字，
    # 但默认的表名没有遵守使用复数形式进行命名的约定， 所以最好由我们自己来指定表名。
    __tablename__ = 'posts'
    id = db.Column(db.Integer, index=True, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.Text)
    summary = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))  # 定义外键，这一列的值是categorys表中行的id值
    tags = db.relationship('Tag',
                           secondary='assignations',
                           backref=db.backref('posts', lazy='dynamic'),
                           lazy='dynamic')

    body_html = ""

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)
        if self.category is None:
            self.category = Category.query.filter_by(name='None').first()

    # @staticmethod
    # def on_changed_body(target, value, oldvalue, initiator):
    #     allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
    #                     'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
    #                     'h1', 'h2', 'h3', 'p']
    #     target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
    #                                                    tags=allowed_tags, strip=True))

    @staticmethod
    def add_category():
        posts = Post.query.all()
        for post in posts:
            if post.category is None:
                post.category = Category.query.filter_by(name='None').first()


# db.event.listen(Post.body, 'set', Post.on_changed_body)


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


class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    # 向Post中添加category属性，定义反向关系，在Post中可代替category_id访问Category模型
    # 此时获取到的是模型对象，而不是外键的值
    # posts 属性返回与此分类相关联的post组成的列表
    posts = db.relationship('Post', backref='category')


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String, unique=True)
