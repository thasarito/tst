from django.db import models
import math
# Create your models here.
class Dictionary(models.Model):
    name = models.CharField(max_length=128)
    readas = models.CharField(max_length=128)
    meaning = models.TextField()
    src = models.URLField()
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)

    def percentUp(self):
    	return math.log(self.up+self.down+1) + self.up/(self.up+self.down+1)
