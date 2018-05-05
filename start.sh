#! /bin/bash

source ../venv/bin/activate

export CONFIG_NAME="production"

python manage.py gunicorn -H 0.0.0.0 -d True

