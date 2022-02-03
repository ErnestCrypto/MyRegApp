# Creating models for login authentication
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=300,)
    telephone = models.IntegerField()
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='images/')
