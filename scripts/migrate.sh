#!/bin/sh
makemigrations.sh
echo 'Running migrate.sh'
python manage.py migrate --noinput