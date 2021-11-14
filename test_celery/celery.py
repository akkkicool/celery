from __future__ import absolute_import, unicode_literals
import os

import django.conf
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')

app = Celery('test_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

from celery.schedules import crontab

from django.conf import settings

cron_time = settings.CRON_TIME_DURATION

app.conf.beat_schedule = {
    'create-task': {
        'task': 'task.task.create_task',
        'schedule': crontab(hour=cron_time),
    },
}
