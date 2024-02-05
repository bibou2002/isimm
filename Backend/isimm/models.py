from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    