import os

from celery import Celery

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "basxconnect_demo.settings.production"
)
app = Celery("basxconnect_demo")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
