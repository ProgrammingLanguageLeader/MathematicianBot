web: gunicorn wsgi:app --timeout 30 --workers 1 --log-file=-
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
