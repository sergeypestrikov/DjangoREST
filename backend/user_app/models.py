from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    option = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}'

    objects = UserManager()

    USERNAME_FIELD = 'email'
