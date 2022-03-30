from django.db import models
from profiles.models import Profile


class Image(models.Model):
    url = models.CharField(max_length=8000)

    def __str__(self):
        return self.url


class Post(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=8000)
    created_at = models.DateTimeField(auto_now_add=True)


