from django.contrib import admin
from .models import User, Role, Paddock, Tag, File

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Paddock)
admin.site.register(Tag)
admin.site.register(File)
