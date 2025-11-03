from django.db import models


class Dz(models.Model):
    album_name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    style = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='dz/images/')
    url = models.URLField(blank=True)
