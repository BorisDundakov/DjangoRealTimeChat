from django.db import models


# Create your models here.
# Creating the tables for the database
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
