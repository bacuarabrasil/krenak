import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "krenak_api.settings")

celery_app = Celery("krenak_api")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
