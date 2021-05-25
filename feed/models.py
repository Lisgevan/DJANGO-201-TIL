from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.text[0:100]} - by - {self.author}'