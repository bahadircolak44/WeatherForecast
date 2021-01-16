#!/usr/bin/env bash

set -e
python manage.py makemigrations
python manage.py migrate --no-input
echo "from django.contrib.auth.models import User; "\
"User.objects.create_superuser('test', 'bahdrcolak@gmail.com', 'test')"\
" if not User.objects.filter(username='test').exists() else ''"\
 | python manage.py shell | python manage.py qcluster &
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000