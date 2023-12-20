from django.db import models


# Create your models here.

class Grammar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example1 = models.CharField(max_length=400)
    example2 = models.CharField(max_length=400)

