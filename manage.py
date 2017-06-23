#!/Users/zhiwei/virtual-environment/flasky/bin/python
# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

blog_server = create_app()
migrate = Migrate(blog_server, db)
manager = Manager(blog_server)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
