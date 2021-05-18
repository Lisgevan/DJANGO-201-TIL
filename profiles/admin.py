from django.contrib import admin
from . import models

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
          pass

admin.site.register(models.Profile, ProfileAdmin)