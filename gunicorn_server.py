# -*- coding:utf-8 -*-

from flask_script import Command, Option
from gunicorn.six import iteritems

class Gunicorn(Command):
    """
    Runs production server with gunicorn
    """

    def __init__(self, app, workers=4, host='127.0.0.1', port=8000, worker_class="sync", daemon=False):
        super(Gunicorn, self).__init__()
        self.port = port
        self.host = host
        self.workers = workers # 工作进程数
        self.worker_class = worker_class # 工作方式
        self.daemon = daemon # 是否以守护进程的方式运行
        self.app = app

    def get_options(self):
        return (
            Option('-H', '--host',
                   dest='host',
                   type=str,
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),

            Option('-c', '--workers-class',
                   dest='worker_class',
                   type=str,
                   default=self.worker_class),

            Option('-d', '--daemon',
                   dest='daemon',
                   type=bool,
                   default=self.daemon)
        )

    def run(self, *args, **kargs):
        from gunicorn.app.base import Application

        class FlaskApplication(Application):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super(FlaskApplication, self).__init__() # 这必须放置 options 初始化之后，否则会抛异常

            def load_config(self):
                config = dict([(key, value) for key, value in iteritems(self.options)
                               if key in self.cfg.settings and value is not None])
                for key, value in iteritems(config):
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        my_option = {
            'bind': '{0}:{1}'.format(kargs['host'], kargs['port']),
            'workers': kargs['workers'],
            'worker_class': kargs['worker_class'],
            'daemon': kargs['daemon']
        }

        flask_app = FlaskApplication(self.app, my_option)
        flask_app.run()
