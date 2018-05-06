# blog
zhiwei's personal blog

## 运行

### 以守护进程的方式运行

`export CONFIG_NAME=‘production'`

`python manage.py gunicorn -H 0.0.0.0 -d True`

## 数据库操作

### 插入行

每次启动 shell 会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复 导入，我们可以做些配置，让 Flask-Script 的 shell 命令自动导入特定的对象。

`python manage.py shell`

向users表中添加一个新用户

```
user_tan = user(email='xxx@gmail.com', password='xxx')

db.session.add(user_tan)

db.session.commit()
```

## 使用 Flask-Migrate 实现数据库迁移

> 在开发程序的过程中，你会发现有时需要修改数据库模型，而且修改之后还需要更新数据库。
>
> 仅当数据库表不存在时， Flask-SQLAlchemy 才会根据模型进行创建。因此，更新表的唯一 方式就是先删除旧表，不过这样做会丢失数据库中的所有数据。
>
> 更新表的更好方法是使用数据库迁移框架。源码版本控制工具可以跟踪源码文件的变化， 类似地，数据库迁移框架能跟踪数据库模式的变化，然后增量式的把变化应用到数据库中。

在需要修改数据库结构前先创建迁移仓库（仅第一次使用时需要执行）

`python manage.py db init`

> 数据库迁移仓库中的文件要和程序的其他文件一起纳入版本控制。

每次数据库结构发生变化就用此命令创建迁移脚本

`python manage.py db migrate -m 'add test' `

将修改应用到已有数据库，且不影响已有的数据

`python manage.py db upgrade `