from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
