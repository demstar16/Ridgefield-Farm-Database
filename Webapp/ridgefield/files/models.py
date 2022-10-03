from django.db import models
from accounts.models import User


# Create your models here.
class Paddock(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    filedata = models.FileField(upload_to='files/')
    paddocks = models.ManyToManyField(Paddock, related_name='paddocks', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name

    def cull_backups(self):
        backups = self.past_versions
        if backups.count > 3:
            backups.earliest().delete()

class PastFile(models.Model):
    filedata = filedata = models.FileField(upload_to='files/')
    replaced = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fileref = models.ForeignKey(File, on_delete=models.CASCADE, related_name="past_versions")

    class Meta:
        ordering = ['-replaced']

    def __str__(self):
        return f'[{self.replaced}] {self.fileref.name}'
