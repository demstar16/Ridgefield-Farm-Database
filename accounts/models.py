from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True,null=True, blank=True, verbose_name='Registration time')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'create_time': self.create_time,
            'is_active': self.is_active
        }
