from django.contrib import admin
from .models import Paddock, Tag, File, PastFile
# Register your models here.

admin.site.register(Paddock)
admin.site.register(Tag)
admin.site.register(File)
admin.site.register(PastFile)