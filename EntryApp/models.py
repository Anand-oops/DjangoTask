from django.db import models

# Create your models here.
class Entry(models.Model):
    Name = models.TextField()
    Age = models.PositiveSmallIntegerField(default=0)