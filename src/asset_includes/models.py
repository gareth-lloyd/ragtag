from django.db import models
from basic.blog.models import Post 

class Asset(models.Model):
    asset_location = models.TextField(blank=False)
    weight = models.IntegerField(blank=False, default=1)
    posts = models.ManyToManyField(Post)

    class Meta:
        ordering = ['weight']
