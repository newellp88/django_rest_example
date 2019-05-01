from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=36)
    summary = models.CharField(max_length=10000)
    ip_address = models.GenericIPAddressField()
    submission_date = models.DateField()
    company = models.CharField(max_length=20)
    reviewer = models.CharField(max_length=50)
    rating = models.IntegerField(default=1,
                                 validators=[
                                     MinValueValidator(1),
                                     MaxValueValidator(5)
                                 ])

