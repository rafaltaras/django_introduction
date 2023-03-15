# maths/models.py
from django.db import models

# Create your models here.

class Math(models.Model):
   operation = models.CharField(max_length=5)
   a = models.IntegerField()
   b = models.IntegerField()
   created = models.DateTimeField(auto_now_add=True)