# blog
zhiwei's personal blog

## 运行

### 以守护进程的方式运行

`export CONFIG_NAME=‘production'`

`python manage.py gunicorn -H 0.0.0.0 -d True`
