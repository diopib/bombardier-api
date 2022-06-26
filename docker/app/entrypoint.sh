#!/bin/sh
set -e


python manage.py migrate --noinput

python manage.py collectstatic --noinput

# start the webservice
gunicorn bombardier_api.wsgi -b 0.0.0.0:8000

exec "$@"
