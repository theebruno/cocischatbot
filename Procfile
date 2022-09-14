release: python manage.py migrate
release: python manage.py makemigrations --no-input
release: python manage.py collectstatic --no-input
web: gunicorn core.wsgi --log-file=-
