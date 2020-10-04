from django.contrib import admin
from . import models

admin.site.register(models.User, models.UserAdmin)
admin.site.register(models.PersonallyImage)
admin.site.register(models.userProfile)