import datetime
from random import choices
from django.db import models


class Todo(models.Model):
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)