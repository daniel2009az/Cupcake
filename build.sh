#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -r requirements.txt
python -m pip install psycopg2-binary
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser --noinput
