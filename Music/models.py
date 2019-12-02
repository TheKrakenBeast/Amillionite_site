from django.contrib.auth.models import User
from django.db.models import CharField, Model
from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
