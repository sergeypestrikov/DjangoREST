from django.db import models
from user_app.models import User


class Project(models.Model):
    title = models.CharField(max_length=64)
    users = models.ManyToManyField(User)
    repo = models.URLField(max_length=128, null=True)


class Task(models.Model):
    title = models.CharField(max_length=64)
    users = models.ManyToManyField(User)
    project = models.ManyToManyField(Project)
    text = models.TextField(max_length=256)
    datetime = models.DateTimeField(auto_created=True, auto_now=True)
    actual = models.BooleanField(blank=True, null=True)