from django.db import models

# Create your models here.
from django.db.models.manager import BaseManager


class Task(models.Model):
    title = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)
    scheduled_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
