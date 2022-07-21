from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    category = models.TextField(max_length=10, default="")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    parent = models.ForeignKey(
        'self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    like = models.IntegerField(default=0)
