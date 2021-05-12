web: sh -c 'cd api && gunicorn krenak_api.wsgi:application'
release: sh -c 'cd api && python manage.py migrate'