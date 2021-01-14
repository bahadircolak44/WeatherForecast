#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate --no-input
echo "from django.contrib.auth.models import User; "\
"from django_q.models import Schedule;"\
"Schedule.objects.create(func='api.tasks.show',schedule_type='M');"\
"User.objects.create_superuser('test', 'bahdrcolak@gmail.com', 'test')"\
" if not User.objects.filter(username='test').exists() else ''"\
 | python manage.py shell | python manage.py qcluster &
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000


