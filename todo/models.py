# todo/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
