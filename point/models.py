from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=100)
    point = models.CharField(max_length=100)

# Create your models here.
