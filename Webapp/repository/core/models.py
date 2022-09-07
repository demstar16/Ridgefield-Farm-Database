from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(null=True, max_length=100)
    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Paddock(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(User, related_name='authors', blank=False)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    filedata = models.FileField(upload_to='files/')
    paddocks = models.ManyToManyField(Paddock, related_name='paddocks', blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name