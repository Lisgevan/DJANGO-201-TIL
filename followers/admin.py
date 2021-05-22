from django.contrib import admin
from . import models

# Register your models here.

class FollowerAdmin(admin.ModelAdmin):
          pass

admin.site.register(models.Follower, FollowerAdmin)