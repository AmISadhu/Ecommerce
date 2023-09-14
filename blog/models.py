from django.db import models
from account.models import User


class Tag(models.Model):
    ...


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(validators=[])
    text = models.TextField()
    short_description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")


class Comment(models.Model):
    ...
