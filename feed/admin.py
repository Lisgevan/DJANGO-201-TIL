from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
          pass

admin.site.register(models.Post, PostAdmin)
