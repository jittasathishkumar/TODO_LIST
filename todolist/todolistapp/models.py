from django.db import models
from django.utils import timezone


class todoclass(models.Model):
    title=models.CharField(max_length=60)
    Details=models.CharField(max_length=60)
    date=models.DateTimeField()
    