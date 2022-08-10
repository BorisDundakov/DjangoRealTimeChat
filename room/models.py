from random import randint

from django.db import models

from django.contrib.auth.models import User


# Create your models here.
# Creating the tables for the database
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        ordering = ('date_added',)
