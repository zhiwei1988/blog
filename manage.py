# -*- coding:utf-8 -*-

from flask_script import Manager, Shell
from app.models import User, Post, Tag
from flask_migrate import Migrate, MigrateCommand
from gunicorn_server import Gunicorn
import multiprocessing
from app import create_app, db

blog_server = create_app()
migrate = Migrate(blog_server, db)
manager = Manager(blog_server)

def make_shell_context():
    return dict(app=blog_server, db=db, user=User, post=Post, tag=Tag)

# 为shell命令添加上下文
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

workers = multiprocessing.cpu_count() * 2 + 1
manager.add_command('gunicorn', Gunicorn(blog_server, workers))

if __name__ == "__main__":
    manager.run()
