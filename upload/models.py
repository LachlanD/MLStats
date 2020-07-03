from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)

class Artist(models.Model):
    name = models.CharField(max_length = 200, primary_key = True)

class Week(models.Model):
    theme = models.CharField(max_length = 100)
    description = models.TextField()

class Song(models.Model):
    title = models.CharField(max_length = 200)
    artist = models.ForeignKey(Artist, on_delete = models.PROTECT)
    submitter = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    week = models.ForeignKey(Week, on_delete = models.CASCADE)

class Vote(models.Model):
    submitter = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    song = models.ForeignKey(Song, on_delete = models.PROTECT)
    votes = models.IntegerField()
    week = models.ForeignKey(Week, on_delete = models.CASCADE)
