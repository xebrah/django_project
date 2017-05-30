from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    name = models.CharField(max_length=160)
    email = models.CharField(max_length=140)
    username = models.CharField(max_length=60)
    time_created = models.DateTimeField(auto_now_add = True)
    time_updated = models.DateTimeField(auto_now = True)
 
