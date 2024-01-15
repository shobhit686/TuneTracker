from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
