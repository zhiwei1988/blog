#!/Users/zhiwei/virtual-environment/flasky/bin/python
# -*- coding:utf-8 -*-

from flask_script import Manager
from app import create_app

blog_server = create_app()
manager = Manager(blog_server)

if __name__ == '__main__':
    manager.run()