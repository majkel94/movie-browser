from django.db import models

from django.contrib.auth import get_user_model


class FavMovie(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name='movies',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=4)
    imdbid = models.CharField(max_length=16)
    type = models.CharField(max_length=32)
    poster = models.CharField(max_length=256)
