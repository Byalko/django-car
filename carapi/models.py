from django.db import models

# Create your models here.

class Car(models.Model):
    user_id = models.PositiveIntegerField(blank=False, null=False)
    number = models.CharField(max_length=10, unique=True)
    condition = models.CharField(max_length=20, default="Normal")
    registration = models.CharField(max_length=30,default="2000/01/01")
    hijaked = models.BooleanField(default=True)