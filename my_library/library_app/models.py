from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    users = models.ManyToManyField(User, blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(5)],
                                blank=True,
                                null=True
                                )
    # registered = models.DateTimeField
