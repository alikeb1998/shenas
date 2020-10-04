import admin as admin
from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User


# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    nationalCode = models.CharField(max_length=16, null=False, default="0312044151")
    shenasnameCode = models.CharField(max_length=16, null=False, default="0312044151")
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField()

    def __str__(self):
        return self.name


class PersonallyImage(models.Model):
    model_pic = models.ImageField(upload_to='', default='none/no-img.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class NationalCardImage(models.Model):
    model_pic = models.ImageField(upload_to='', default='none/no-img.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class ShenasnameImage(models.Model):
    model_pic = models.ImageField(upload_to='', default='none/no-img.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class PersonallyImage_inline(admin.TabularInline):
    model = PersonallyImage
    extra = 1


class NatioanlCardImage_inline(admin.TabularInline):
    model = NationalCardImage
    extra = 1


class ShenasnameImage_inline(admin.TabularInline):
    model = ShenasnameImage
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = (PersonallyImage_inline, NatioanlCardImage_inline, ShenasnameImage_inline)
