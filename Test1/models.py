from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=150)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

