from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField()
    
class User(models.Model):
    text=models.CharField(max_length=40)

    def __str__(self):
        return self.title