from django.db import models

# Create your models here.
class Dictionary(models.Model):
    name = models.CharField(max_length=128)
    readas = models.CharField(max_length=128)
    meaning = models.TextField()
    url = models.URLField()
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
