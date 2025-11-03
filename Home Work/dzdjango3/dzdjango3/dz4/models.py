from django.db import models


class Dz4(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
