from django.db import models
from accounts.models import User

# Create your models here.
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
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    filedata = models.FileField(upload_to='files/')
    paddocks = models.ManyToManyField(Paddock, related_name='paddocks', blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name