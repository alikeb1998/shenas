from django.db import models


class MyImage(models.Model):
    model_pic = models.ImageField(upload_to='', default='none/no-img.jpg')


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nationalCode = models.CharField(max_length=16)
    shenasnameCode = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    personallyImage = models.ImageField()
    nationalCardImage = models.FileField
    accepted = models.BooleanField()
