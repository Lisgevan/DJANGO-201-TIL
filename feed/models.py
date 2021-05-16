from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text[0:100]