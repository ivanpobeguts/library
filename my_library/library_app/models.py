from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    # registered = models.DateTimeField
