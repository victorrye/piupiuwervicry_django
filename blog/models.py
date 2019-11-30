from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import requests


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to = "piupiuwervicry_django\media\images", default='piupiuwervicry_django\media\images\defaultpic.png')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='piupiuwervicry_django\django_treinamento\piupiuwervicry_django\media\images\defaultpic.png', upload_to='piupiuwervicry_django\django_treinamento\piupiuwervicry_django\media\images')
    birthday = models.DateTimeField()
    joinedday = models.DateTimeField()
    livingplace = models.CharField(max_length=50)
    firstandlastname = models.CharField(max_length=50, default='Generic Name')
    image = models.ImageField(upload_to = "piupiuwervicry_django\media\images", default='piupiuwervicry_django\media\images\defaultpic.png')

    def __str__(self):
        return f'{self.user.username} Profile'