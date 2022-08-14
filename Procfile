release: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input
web: gunicorn config.wsgi:application