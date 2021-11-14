import datetime

import django
from celery.schedules import crontab
from celery import shared_task

import string
import random  # define the random module

from rest_framework import status
from rest_framework.response import Response

from task.models import Task
from test_celery.celery import app


@app.task
def create_task():
    obj_count = 3
    if not django.conf.settings.DEBUG:
        obj_count = 5
    for i in range(0, obj_count):
        title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        description = 'sample description'
        Task.objects.create(title=title, description=description, scheduled_date=datetime.datetime.now())
    return 'Task created...!'
