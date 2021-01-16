#!/usr/bin/env bash

set -e
python manage.py makemigrations
python manage.py migrate --no-input
echo "from django.contrib.auth.models import User;"\
  "from api.models import WorldCities;"\
  "User.objects.create_superuser(username='test', email='bcolak@gmail.com', password='test')"\
  " if not User.objects.filter(username='test').exists() else '';"\
  " WorldCities.generate()"\
  " if not WorldCities.objects.all().exists() else '';"\
 | python manage.py shell
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000


